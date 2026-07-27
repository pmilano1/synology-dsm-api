# Best Practices

[← Back to Documentation](../../README.md)

Practical guidance for calling the DSM Web API reliably. See also
[Error Handling](error-handling.md).

---

## Authentication & sessions

- **Log in once, reuse the `sid`.** Authenticate via `SYNO.API.Auth` (`method=login`,
  `format=sid`) and reuse the returned `sid` as `_sid` on every subsequent call. Don't
  re-login per request.
- **Get a `SynoToken` for writes.** Add `enable_syno_token=yes` at login and send the
  returned token as the `X-SYNO-TOKEN` header on any state-changing call. Read calls work
  with `_sid` alone; writes without the token typically fail with **error 119**.
- **Log out** (`SYNO.API.Auth` `method=logout`) when done with a session, especially in
  scripts, to avoid leaking sessions.
- **Scope the session name** to the app you're driving (e.g. `session=Backup`,
  `session=FileStation`) so DSM applies the right permissions.

## Discovering the API surface

- **Enumerate before you guess.** `SYNO.API.Info?query=all` returns every registered
  endpoint with its `path` and `minVersion`/`maxVersion`. Use it to confirm an API exists
  and which versions are valid, instead of hardcoding assumptions.
- **Respect the version range.** Call an API at a version within `[minVersion, maxVersion]`;
  newer versions often add fields/params.

## Request construction

- **URL-encode every parameter.** JSON-valued params (arrays/objects, and even quoted
  strings like `sort_by="name"`) must be encoded; a stray `&`/quote silently corrupts the
  request.
- **Wrap objects where required.** Some `set`/`create` calls require their payload nested
  under a wrapper key (e.g. `SYNO.Core.Share set` needs `shareinfo={…}`); passing fields
  flat is rejected.
- **Batch with `SYNO.Entry.Request`.** Multiple calls can be sent as one `compound` array
  (`mode=sequential`, `stop_when_error`), which is how the DSM UI commits related writes
  atomically.

## Reliability

- **Check `success` first**, then read `data`. On `success:false`, branch on `error.code`
  (see [Error Handling](error-handling.md)).
- **Retry idempotent reads** with backoff — a NAS behind a reverse proxy can time out
  transiently. Do **not** blindly retry writes.
- **Paginate** list endpoints with `offset`/`limit` (use `limit=-1` only when you truly
  want everything) and read `total` to know when to stop.
- **Prefer HTTPS** and pin/verify the certificate where you can; self-signed DSM certs
  require an explicit trust decision in clients.

## Safety

- **Never hardcode credentials** in scripts or commit them; source them from a secrets
  store or environment.
- **Redact secrets from responses** before logging/sharing — several APIs echo
  destination credentials (masked) or account metadata.
- **Test destructive methods on a throwaway object** (task, share, folder) before running
  them against production data.
