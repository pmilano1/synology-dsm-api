# Hyper Backup - Integrity Check

**Category:** Data Protection

[← Back to Hyper Backup](README.md)

---

**Endpoint:** `/webapi/entry.cgi`

The **Detect corruption / Check backup integrity** action (UI: task menu → *Check backup
integrity*) verifies a task's data at the destination. It runs through
[`SYNO.Backup.Target`](repositories.md#syno-backup-target); dedicated integrity endpoints
are noted below.

---

## SYNO.Backup.Target — integrity probe

#### Method: `error_detect` *(community-confirmed)*

**HTTP Method:** POST — start an integrity/connectivity check of the task's target.

**Parameters:**
- `api` (required): `SYNO.Backup.Target`
- `version` (required): `1`
- `method` (required): `error_detect`
- `task_id` (required): Task ID
- `_sid` (required): Session ID
- `X-SYNO-TOKEN` header (required): CSRF token

**Response:**
```json
{ "success": true }
```
Progress is polled via [`SYNO.Backup.Task status`](tasks.md#method-status), whose
`last_bkp_result` / `last_detect_time` reflect the check.

---

#### Method: `error_detect_cancel` *(community-confirmed)*

**HTTP Method:** POST — cancel a running integrity check.

**Parameters:**
- `api` (required): `SYNO.Backup.Target`
- `version` (required): `1`
- `method` (required): `error_detect_cancel`
- `task_id` (required): Task ID
- `_sid` (required): Session ID
- `X-SYNO-TOKEN` header (required): CSRF token

**Response:**
```json
{ "success": true }
```

---

## Related endpoints (present, methods uncaptured)

From [`SYNO.API.Info`](../dsm-core/authentication.md), these integrity-adjacent APIs exist
on DSM 7 but their methods were not wire-captured here — document them when captured
against a throwaway task:

| API | Ver | Role |
|-----|-----|------|
| `SYNO.Backup.Target.Config` | 1-2 | Target-side config used by detection/repair |
| `SYNO.Backup.Repository.Certificate` | 1-2 | Destination TLS certificate handling |

> **Note:** in `SYNO.Backup.Target get`, `last_detect_time` is empty until an integrity
> check has run at least once (a fresh task reports *"Integrity check: Not performed yet"*).
