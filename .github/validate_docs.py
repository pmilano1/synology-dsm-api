#!/usr/bin/env python3
"""
Documentation validator for synology-dsm-api.

Enforces the repo's documentation rules on every PR:
  1. FORMAT   — API-reference pages follow the house per-API template.
  2. LINKS    — every relative Markdown link resolves (no dead links).
  3. SECRETS  — no credentials/keys/tokens committed.
  4. PII      — no real setup identifiers (denylist in .github/pii-denylist.txt).
  5. HYGIENE  — files end with a newline; no trailing whitespace; no tabs.

Exit code 0 = clean, 1 = violations found. No third-party dependencies.
"""
import os, re, sys, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, "docs")

violations = []          # (severity, file, line, message)
def add(sev, f, line, msg):
    violations.append((sev, os.path.relpath(f, ROOT), line, msg))

# ---------------------------------------------------------------- secrets
SECRET_PATTERNS = [
    (r"AKIA[0-9A-Z]{16}", "AWS access key id"),
    (r"-----BEGIN [A-Z ]*PRIVATE KEY-----", "private key block"),
    (r"ghp_[A-Za-z0-9]{36}", "GitHub personal access token"),
    (r"xox[baprs]-[A-Za-z0-9-]{10,}", "Slack token"),
    (r"(?i)aws_secret_access_key\s*[=:]\s*[A-Za-z0-9/+]{40}", "AWS secret key"),
    (r"hvs\.[A-Za-z0-9]{20,}", "Vault service token"),
]

# ---------------------------------------------------------------- pii denylist
def load_denylist():
    path = os.path.join(ROOT, ".github", "pii-denylist.txt")
    pats = []
    if os.path.exists(path):
        for ln in open(path, encoding="utf-8"):
            ln = ln.split("#", 1)[0].strip()
            if ln:
                pats.append(ln)
    return pats
PII_PATTERNS = load_denylist()

# ---------------------------------------------------------------- helpers
def md_files():
    return sorted(glob.glob(os.path.join(DOCS, "**", "*.md"), recursive=True))

LINK_RE = re.compile(r"\]\(([^)]+?)(?:#[^)]*)?\)")

def is_api_reference(f):
    rel = os.path.relpath(f, DOCS)
    return rel.startswith("api-reference" + os.sep) and os.path.basename(f) != "README.md"

# ---------------------------------------------------------------- checks
def check_links(f, text):
    d = os.path.dirname(f)
    for m in LINK_RE.finditer(text):
        link = m.group(1).strip()
        if link.startswith(("http://", "https://", "mailto:", "#")) or not link.endswith(".md"):
            continue
        target = os.path.normpath(os.path.join(d, link))
        if not os.path.exists(target):
            line = text[: m.start()].count("\n") + 1
            add("LINKS", f, line, f"dead link -> {link}")

def check_secrets(f, text):
    for pat, label in SECRET_PATTERNS:
        for m in re.finditer(pat, text):
            line = text[: m.start()].count("\n") + 1
            add("SECRETS", f, line, f"possible {label}")

def check_pii(f, text):
    for pat in PII_PATTERNS:
        for m in re.finditer(pat, text):
            line = text[: m.start()].count("\n") + 1
            add("PII", f, line, f"setup PII matches /{pat}/ : {m.group(0)!r}")

def check_hygiene(f, text):
    if text and not text.endswith("\n"):
        add("HYGIENE", f, text.count("\n") + 1, "file must end with a newline")
    for i, ln in enumerate(text.split("\n"), 1):
        if ln.rstrip("\n") != ln.rstrip():
            add("HYGIENE", f, i, "trailing whitespace")
        if "\t" in ln:
            add("HYGIENE", f, i, "tab character (use spaces)")

# A conforming per-method heading: "#### Method: `name`" (or "#### Methods:").
CONFORMING_METHOD_RE = re.compile(r"^####\s+Methods?:", re.M)

# A #### subheading that documents an API method but does NOT use the house
# "#### Method:" template — the styles that used to dodge the gate, e.g.
#   #### `SYNO.SDS.Backup.Client.Explore.File` — `download` (v1)
#   #### `SYNO.Backup.Version` list (v2)
# Matches an h4 that names a SYNO.* API, or a backtick verb tagged with a
# version marker like "(v1)". Non-method h4s ("#### Overview") never match.
DODGING_METHOD_HEADING_RE = re.compile(
    r"^####\s+(?!Methods?:)(?P<h>.*(?:SYNO\.[A-Za-z0-9.]+|`\w+`\s*\(v\d+\)).*)$",
    re.M,
)

# Indicators that a page documents API methods at all (even purely in prose or
# tables). Any one of these turns on the per-method template requirements.
METHOD_INDICATORS = [
    CONFORMING_METHOD_RE,                              # #### Method: headings
    re.compile(r"\*\*HTTP Method:\*\*"),               # per-method HTTP verb label
    re.compile(r"^####\s+`?SYNO\.", re.M),             # dodging SYNO.x subheading
    re.compile(r"[?&]method=\w"),                      # method= in a query string / curl
    re.compile(r"`method`\s*\(required\)"),            # `method` (required) param row
    re.compile(r"method=`?[a-z_][a-z_0-9]*`?", re.I),  # method=<verb> in prose/code
    DODGING_METHOD_HEADING_RE,                         # SYNO.x — `verb` (vN) subheading
]

def _documents_methods(text):
    return any(p.search(text) for p in METHOD_INDICATORS)

def check_format(f, text):
    """House template for API-reference pages (structural, robust checks only).

    Every API-reference page needs a top-level heading, a **Category:** line and
    a back-link. If a page documents API methods (in ANY style), then it must use
    the house per-method template: each method under a `#### Method:` heading with
    **HTTP Method:** / **Parameters:** / **Response:** sections. Pages that clearly
    document methods but use an alternative heading style (e.g. an h4 naming the
    SYNO.* API directly) FORMAT-fail regardless of that style.
    """
    if not text.lstrip().startswith("# "):
        add("FORMAT", f, 1, "must start with a top-level '# ' heading")
    if "**Category:**" not in text:
        add("FORMAT", f, 1, "missing '**Category:**' line")
    if "[← Back" not in text:
        add("FORMAT", f, 1, "missing a back-link '[← Back to ...]'")

    # Conceptual / overview API-ref pages that document no methods are exempt from
    # the per-method template (README.md is already excluded by is_api_reference).
    if not _documents_methods(text):
        return

    # Every documented method must use the '#### Method:' house heading.
    if not CONFORMING_METHOD_RE.search(text):
        add("FORMAT", f, 1,
            "documents API methods but has no '#### Method:' heading — every method "
            "must use the house '#### Method: `<name>`' template")
    # Flag each method heading that dodges the template with an alternative style,
    # even on pages that also have some conforming headings (mixed pages).
    for m in DODGING_METHOD_HEADING_RE.finditer(text):
        line = text[: m.start()].count("\n") + 1
        add("FORMAT", f, line,
            "method heading not in house format — use '#### Method: `<name>`' "
            f"(found: '#### {m.group('h').strip()[:60]}')")
    # A method-documenting page must show each per-method section at least once.
    if "**HTTP Method:**" not in text:
        add("FORMAT", f, 1, "documents Method(s) but has no '**HTTP Method:**' line")
    if "**Parameters:**" not in text and "**Parameters**" not in text:
        add("FORMAT", f, 1, "documents Method(s) but has no '**Parameters:**' section")
    if "**Response:**" not in text and "**Response**" not in text:
        add("FORMAT", f, 1, "documents Method(s) but has no '**Response:**' section")

    # ---- per-method structural enforcement (SYNO.Backup.App2.Backup is the golden template) ----
    # Each '#### Method:' block, bounded by the next heading (levels 1-4), must carry its
    # OWN **HTTP Method:** / **Parameters:** / **Response:**, and **Parameters:** must be a
    # bulleted list (one `- ` param per line), not prose. This is what makes every method
    # render identically to the App2.Backup reference rather than "close enough".
    heading_starts = [h.start() for h in re.finditer(r"^#{1,4}\s", text, re.M)]
    for mm in re.finditer(r"^####\s+Methods?:\s*`?(?P<name>[^`\n]*)`?.*$", text, re.M):
        blk_start = mm.start()
        later = [h for h in heading_starts if h > blk_start]
        block = text[blk_start:(min(later) if later else len(text))]
        line = text[:blk_start].count("\n") + 1
        name = (mm.group("name") or "").strip() or "?"
        if "**HTTP Method:**" not in block:
            add("FORMAT", f, line, f"method `{name}` block has no '**HTTP Method:**' line")
        if "**Parameters:**" not in block and "**Parameters**" not in block:
            add("FORMAT", f, line, f"method `{name}` block has no '**Parameters:**' section")
        else:
            # content may sit inline on the label line or on the following line(s);
            # either way the first non-empty content must be a bullet, else it's prose.
            pm = re.search(r"\*\*Parameters:?\*\*[ \t]*(?P<inline>[^\n]*)\n+(?P<first>[^\n]*)", block)
            if pm:
                inline = pm.group("inline").strip()
                content = inline if inline else pm.group("first").strip()
                if content and not content.startswith(("- ", "* ", "|")):
                    pl = line + (0 if inline else block[: pm.start("first")].count("\n"))
                    add("FORMAT", f, pl,
                        f"method `{name}` **Parameters:** must be a bulleted list of params, not prose")
        if "**Response:**" not in block and "**Response**" not in block:
            add("FORMAT", f, line, f"method `{name}` block has no '**Response:**' section")

    # API section headings must be h2 ('## SYNO.x'), matching the reference — an h3 naming a
    # SYNO.* API is the wrong level and reads inconsistently next to the h2 sections.
    for m3 in re.finditer(r"^###\s+`?(?P<h>SYNO\.[A-Za-z0-9.]+)", text, re.M):
        line = text[: m3.start()].count("\n") + 1
        add("FORMAT", f, line,
            f"API section heading '{m3.group('h')}' must be an h2 '## ', not '### '")

# ---------------------------------------------------------------- run
def main():
    files = md_files()
    if not files:
        print("no markdown files found under docs/", file=sys.stderr)
        return 1

    # With --scoped, FORMAT + HYGIENE are enforced only on the file args that follow
    # (the PR's changed docs — a ratchet so new/edited docs must comply while the
    # existing backlog is not a blocker). SECRETS / PII / LINKS always run repo-wide.
    # Without --scoped, every check runs on every file (a full local audit).
    args = sys.argv[1:]
    scoped = "--scoped" in args
    changed = {os.path.normpath(os.path.abspath(a)) for a in args if a != "--scoped"}
    if scoped:
        print(f"FORMAT/HYGIENE scoped to {len(changed)} changed file(s); "
              f"SECRETS/PII/LINKS repo-wide.\n")

    for f in files:
        text = open(f, encoding="utf-8", errors="replace").read()
        check_links(f, text)
        check_secrets(f, text)
        check_pii(f, text)
        if not scoped or os.path.normpath(os.path.abspath(f)) in changed:
            check_hygiene(f, text)
            if is_api_reference(f):
                check_format(f, text)

    if not violations:
        print(f"✓ docs validation passed — {len(files)} files, 0 violations")
        return 0

    by_sev = {}
    for sev, f, line, msg in violations:
        by_sev.setdefault(sev, []).append((f, line, msg))
    print(f"✗ docs validation failed — {len(violations)} violation(s) across {len(files)} files\n")
    for sev in ("SECRETS", "PII", "LINKS", "FORMAT", "HYGIENE"):
        rows = by_sev.get(sev)
        if not rows:
            continue
        print(f"── {sev} ({len(rows)}) ──")
        for f, line, msg in sorted(rows):
            print(f"   {f}:{line}: {msg}")
        print()
    return 1

if __name__ == "__main__":
    sys.exit(main())
