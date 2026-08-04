#!/usr/bin/env bash
# Enumerate every API a DSM appliance exposes, and diff it against this repo's docs.
#
# WHY THIS EXISTS
#
# "Is this API documented?" was a memory exercise. It is now a diff.
#
# `SYNO.API.Info?query=all` returns every API the appliance serves, with version
# ranges and CGI paths. It needs NO AUTHENTICATION, so this is safe to run against
# any reachable DSM and needs no credentials in CI or in anyone's shell history.
#
# WHAT IT DOES NOT DO
#
# It does not return METHODS. DSM exposes no method enumeration, and discovering
# methods by probing is unsafe — see docs/guides/api-discovery.md for why, and for
# the safe alternatives. This tool deliberately stops at the boundary where guessing
# would start.
set -euo pipefail

HOST="${1:-}"
OUT="${2:-reference}"

if [ -z "$HOST" ]; then
  cat >&2 <<'USAGE'
usage: tools/api-inventory.sh <host[:port]> [output-dir]

  tools/api-inventory.sh nas.example.com:5001
  tools/api-inventory.sh 192.168.1.10:5000 reference

Writes:
  <output-dir>/api-inventory-dsm-<version>.json   every API, with version range and path
  and prints a coverage summary against docs/.
USAGE
  exit 2
fi

command -v jq >/dev/null || { echo "jq is required" >&2; exit 1; }

# -k because DSM commonly serves its own self-signed certificate on the direct port.
# This call carries no credentials and reads public metadata, so an unverified
# connection leaks nothing — but do not copy this flag into calls that authenticate.
echo "== querying $HOST"
RAW=$(curl -sk -m 20 "https://${HOST}/webapi/query.cgi?api=SYNO.API.Info&version=1&method=query&query=all")

echo "$RAW" | jq -e '.success == true' >/dev/null || {
  echo "query failed: $(echo "$RAW" | head -c 200)" >&2
  exit 1
}

mkdir -p "$OUT"
FILE="$OUT/api-inventory.json"
echo "$RAW" | jq -S '.data | to_entries | map({key: .key, value: {minVersion: .value.minVersion, maxVersion: .value.maxVersion, path: .value.path, requestFormat: (.value.requestFormat // null)}}) | from_entries' > "$FILE"

TOTAL=$(jq 'length' "$FILE")
echo "   $TOTAL APIs written to $FILE"

# ── coverage ────────────────────────────────────────────────────────────────
# An API counts as "documented" if its name appears anywhere under docs/. That is
# deliberately generous: it means the real coverage is no better than this number,
# never worse. Method-level coverage is lower again, because SYNO.API.Info cannot
# tell us what methods exist to count against.
if [ -d docs ]; then
  jq -r 'keys[]' "$FILE" | sort -u > /tmp/.live.$$
  grep -rhoE 'SYNO\.[A-Za-z0-9._]+' docs/ 2>/dev/null | sort -u > /tmp/.docs.$$
  LIVE=$(wc -l < /tmp/.live.$$)
  BOTH=$(comm -12 /tmp/.live.$$ /tmp/.docs.$$ | wc -l)
  GAP=$(comm -23 /tmp/.live.$$ /tmp/.docs.$$ | wc -l)
  STALE=$(comm -13 /tmp/.live.$$ /tmp/.docs.$$ | grep -c '\.' || true)

  echo
  echo "== coverage"
  printf '   live on appliance    %5d\n' "$LIVE"
  printf '   documented and live  %5d  (%d%%)\n' "$BOTH" "$((100 * BOTH / LIVE))"
  printf '   live, undocumented   %5d\n' "$GAP"
  printf '   documented, ABSENT   %5d  <- either package-dependent or wrong\n' "$STALE"

  comm -23 /tmp/.live.$$ /tmp/.docs.$$ > "$OUT/undocumented.txt"
  comm -13 /tmp/.live.$$ /tmp/.docs.$$ | grep '\.' > "$OUT/documented-but-absent.txt" || true
  echo "   lists written to $OUT/"
  rm -f /tmp/.live.$$ /tmp/.docs.$$
fi
