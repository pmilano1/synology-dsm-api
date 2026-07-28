# Agent (PC) Image Backup & Restore — Practical Recipes

End-to-end recipes for driving **Active Backup for Business** agent/PC **image backups** (`backup_type: 2`, entire-device) over the Web API. Verified against **DS918+, DSM 7.3 (build 86003), ABB package 3.2, Agent 3.2.0-5053**.

See also: [Error Handling Guide](error-handling.md), [SYNO.ActiveBackup.Task](../api-reference/activebackup/core/task.md), [SYNO.ActiveBackup.Version](../api-reference/activebackup/core/version.md).

## Endpoints & Authentication

The ABB Web API is served from `/webapi/auth.cgi` and `/webapi/entry.cgi`. Two ways to reach DSM:

| Endpoint | Use for | Notes |
|----------|---------|-------|
| Reverse proxy (e.g. `https://nas.example.com`) | Control-plane API calls | Self-signed → `verify=False`; add retries (proxy may time out) |
| Direct DSM host `https://<nas-ip>:5801` | Same API; needed if a call is host/session-bound | DSM HTTPS moved off `5001`; agent data-plane uses port `5510` |

Log in against the `ActiveBackup` session and reuse the `sid` as `_sid`:

```bash
# 1) login  -> data.sid
curl -sk "https://<host>/webapi/auth.cgi" \
  --data-urlencode "api=SYNO.API.Auth" \
  --data-urlencode "version=6" \
  --data-urlencode "method=login" \
  --data-urlencode "account=admin" \
  --data-urlencode "passwd=********" \
  --data-urlencode "session=ActiveBackup" \
  --data-urlencode "format=sid"
```

Both an `admin` DSM account and a delegated ABB user (e.g. `peterm`) authenticate successfully; either can drive the calls below.

## Identify tasks, devices, and results

`SYNO.ActiveBackup.Task` `list_with_device` is the most useful read — it returns each task with its `device_info` and a `last_result` block:

```json
{
  "last_result": {
    "status": 2,
    "time_start": 1784066187,
    "time_end": 1784070089,
    "transfered_bytes": 207000000000,
    "error_count": 0,
    "warning_count": 0
  }
}
```

`last_result.status` values:

| status | meaning |
|--------|---------|
| 2 | success |
| 3 | failed |
| 4 | partial / completed with warnings |

`last_result` is `null` until a backup has completed at least once. Use `SYNO.ActiveBackup.Device` `list` for the device inventory (`device_id`, `device_uuid`, `host_name`, `login_user`, `login_time`).

> **Note:** Reconnecting the Windows agent under a *different* DSM account creates a **new** `device_id` + auto-task (same `device_uuid`), owned by that account. The storage folder is `PC-<HOSTNAME>-<user>-Default`, so the owning user keeps folders distinct.

## Trigger a manual backup

```
GET SYNO.ActiveBackup.Task  method=backup  version=1  task_ids=[<id>]
```

- `task_ids` **must be a JSON array** (`[12]`), not a bare int. A bare int returns `120 { name: task_ids }`.
- Returns `{"success": true}` — but see the gotcha below.

> **Gotcha — silent no-op backups:** an auto-created agent task with **no backup source selected** (`custom_volume: null` and an empty partition map) accepts `backup` with `success: true` but the agent instantly "completes" with `partition_map: null, selected_paths: [], total_size: 0` and stays idle — `last_result` never populates. Fix: open the task in the ABB console and **select a source (Entire device / a volume)** so the partition map is written, then trigger again.

## Monitor a running backup

Server-side log (`SYNO.ActiveBackup.Log`):

```
GET SYNO.ActiveBackup.Log  method=list_log   version=1     # events
GET SYNO.ActiveBackup.Log  method=list_result version=1     # per-run results
```

`log_type` values seen in practice:

| log_type | meaning |
|----------|---------|
| 1001 | device / task added |
| 1101 | backup started |
| 1102 | backup completed |
| 1104 | backup cancelled |
| 5001 | device online |

> The generic `SYNO.ActiveBackup.Log` `list` method does **not** exist (returns `103`). Use `list_log` / `list_result`.

Agent-side, the live transfer is visible in `C:\ProgramData\ActiveBackupforBusinessAgent\log\log.txt` — look for `backup-upload-worker.cpp … Processing to image '0.img', offset <N>` lines (the offset advances over sparse/deduped regions faster than real bytes, so it isn't a clean throughput meter).

## Restore points (versions)

```
GET SYNO.ActiveBackup.Version  method=list  version=1  task_id=<id>
```

Each version includes `version_id`, `status` (3 = complete, 4 = complete-with-warnings), `folder_name` (e.g. `ActiveBackup_2026-07-14_171627`), `locked`, `version_uuid`, `task_unikey`, and a `scope` JSON (`include_boot_partition`, `custom_volume`, `source_type`).

- `method=lock` / `delete` take `task_id`. **Locking** a version exempts it from retention/GFS — use it to permanently protect specific restore points.

## File-Level Restore (browse & download individual files)

> **Status: the mount/browse-session trigger is undocumented and not yet captured.** Everything below is confirmed by live probing except the one call that opens the browse session. **All three file-restore methods — `list_node`, `get_volume_info`, and `restore` — return error `1001` until that session exists.** Ruled out by testing against a live DSM 7.3 / ABB 3.2 restore point: repeated `list_node` does **not** self-mount (stays `1001` across polls); `Version.restore` is *not* the prepare step (it also needs `paths` **and** still returns `1001`); no `path`/volume format (`/`, `/1`, `/C:`, `/0/`, `/volume1`, …) clears it. A parallel research pass found **no public source** documenting the sequence (Synology only exposes it via the Recovery Portal SPA; the 3.2 SPK ships AES-encrypted, so its JS can't be extracted). **The reliable way to obtain the exact call is a HAR/network capture of the Recovery Portal doing one file browse** (DevTools → Network → filter `entry.cgi`) — that reveals the literal mount method, params, and `path`/volume-id format. Fill this section in from a capture; do not assume a sequence until then.

**Classic vs AEM agent.** Determine which browse API applies by the task's `workload_uuid`:

| `workload_uuid` | Backup type | Browse API |
|-----------------|-------------|------------|
| empty (`""`) | classic agent backup | `SYNO.ActiveBackup.Version` → `list_node` |
| present | AEM (endpoint-managed) | `SYNO.ActiveBackup.AEM.Version` → `create` / `get_volume_info` / `list_entry` |

`SYNO.ActiveBackup.Version` `list_node` required params (all validated): `task_id`, `device_id`, `version_id`, `path`, `sort_by` (+ `sort_direction`, `offset`, `limit`).

**Known blocker:** for a classic image backup, `list_node` (and AEM `get_volume_info`) return error **`1001`** for any path until a **browse session / mount** is established first. `get_volume_info` does not exist on the core `SYNO.ActiveBackup.Version` API (`103`) — it is AEM-only.

Error codes seen while probing the browse:

| code | meaning |
|------|---------|
| 120  | missing or wrong-**type** parameter (`errors.reason`) |
| 103  | method not available on that API / version |
| 1001 | operation failed — restore point not mounted / no browse session |

**Reliable fallback (always works):** DSM → Active Backup for Business → **Restore Portal**, which mounts the version server-side and serves a file browser. Target path for a Windows agent backup:
`Users\<windows-user>\AppData\Roaming\...`.
