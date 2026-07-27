# Hyper Backup - Versions, Sources & Restore

**Category:** Data Protection

[← Back to Hyper Backup](README.md)

---

**Endpoint:** `/webapi/entry.cgi`

Restore points (**versions**), the folder/app **sources** a task backs up, and the
**restore / file-browse** surface. Read methods verified on DSM 7.x by capturing the
Hyper Backup UI, including the Backup Explorer browse + download + progress APIs.

---

## SYNO.Backup.Version

#### Method: `list`

**HTTP Method:** GET — restore points for a task.

**Parameters:**
- `api` (required): `SYNO.Backup.Version`
- `version` (required): `2`
- `method` (required): `list`
- `task_id` (required): Task ID
- `_sid` (required): Session ID
- `offset` (optional): paging offset (default `0`)
- `limit` (optional): page size; `-1` for all
- `filter_name` (optional): quoted JSON string, e.g. `"success"`
- `sort_direction` (optional): quoted JSON string, `"desc"` / `"asc"`
- `repo_id` (optional): Repository id
- `target_id` (optional): quoted JSON string — the **repository directory name** (not a numeric id)
- `additional` (optional): JSON array — e.g. `["version_operate_property","skip_check_key","source","status"]`

**Response:**
```json
{
  "success": true,
  "data": {
    "total": 42,
    "backup_data_type": "data",
    "support_lock": true,
    "permit_delete": { "permitted": true },
    "version_info_list": [
      {
        "version_id": "42",
        "name": "2025/01/15 02:00:00",
        "status": "success",
        "complete_time": 1736900000,
        "complete_time_local": "2025/01/15 02:12:30",
        "start_time_local": "2025/01/15 02:00:00",
        "locked": false,
        "permit_delete": true,
        "has_history": true,
        "modify": "0",
        "source": { "backup_apps": ["File Station", "Hyper Backup"] }
      }
    ]
  }
}
```

**Response Fields:**

| Field | Type | Description |
|-------|------|-------------|
| `version_id` | string | Restore-point id (use in restore/explore calls) |
| `name` | string | Version label (its start timestamp) |
| `status` | string | `success`, `fail`, … |
| `complete_time` | integer | Completion (Unix time) |
| `locked` | bool | Version locked against deletion |
| `source.backup_apps` | array | Apps included in this version |

---

#### Method: `summary`

**HTTP Method:** GET — aggregate counts/size across a task's versions.

**Parameters:** `api`, `version`=`1`, `method`=`summary`, `task_id`, `_sid`.

**Response:** `{ "success": true, "data": { ... } }` (totals used by the version-list header).

---

## SYNO.Backup.Version.History

Per-version change history (`[v1-2]`). Present on DSM 7; methods not yet captured here
(expect a `list` keyed by `task_id` + `version_id`).

---

## SYNO.Backup.Source.Folder

#### Method: `list`

**HTTP Method:** GET — the shared-folder tree shown in a task's **Folders** picker
(lazy-loaded per node).

**Parameters:**
- `api` (required): `SYNO.Backup.Source.Folder`
- `version` (required): `1`
- `method` (required): `list`
- `node` (required): quoted JSON string — `"fm_root"` for volume/share roots, or a folder `id` to expand it
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "folder": [
      {
        "id": "/example_share",
        "text": "example_share",
        "path": "/volume1/example_share",
        "volume": "/volume1",
        "leaf": false,
        "checked": false,
        "disabled": false,
        "encryptedShare": false,
        "dataEncrypted": false
      }
    ]
  }
}
```

---

## SYNO.Backup.App2.Backup

#### Method: `list`

**HTTP Method:** GET — backup-capable applications/packages (the **Application** tab).

**Parameters:**
- `api` (required): `SYNO.Backup.App2.Backup`
- `version` (required): `2`
- `method` (required): `list`
- `_sid` (required): Session ID
- `app_config` (optional): JSON array (default `[]`)
- `support_app_share` (optional): `true`/`false`
- `detailed_app_info` (optional): `true`/`false`

**Response:**
```json
{
  "success": true,
  "data": [
    {
      "id": "FileStation",
      "name": "File Station",
      "version": "1.4.4-2221",
      "is_running": true,
      "online_backup": true,
      "is_beta": false,
      "summary_disp": "Back up settings, files, and sharing links.",
      "depend": { "folder_list": [] }
    }
  ]
}
```

---

## Backup Explorer — browse & download individual files (recovery path)

The **`SYNO.SDS.Backup.Client.Explore.*`** family is what DSM's **Backup Explorer**
(Hyper Backup → *Backup Explorer*) uses to browse the file tree **inside** a version and
download individual files. It is **undocumented anywhere public** — captured here live
(DSM 7.x, Hyper Backup 4.2.2) from the DSM client JS + the wire. This is the headless
file-level recovery path (e.g. pulling one lost file out of an old restore point) with no
whole-share restore.

Every call takes a common **Explorer param bundle** (send it on all of them):

```
task_id=1
version_id="141"                     # ⚠️ JSON-quoted string
backend="HyperBackup-backend"        # ⚠️ REQUIRED — omitting it fails downloads with 4400
filter_keyword=""  filter_type="any"  filter_size_option="any"
filter_size=0  filter_date_from=0  filter_date_to=0
```

#### `SYNO.SDS.Backup.Client.Explore.Version` — `list` (v1)

Versions available to explore for a task. Params: `task_id` (+ bundle), `offset`,
`limit`, `filter_name="success"`. Response `data.version_info_list[]` with `version_id`,
`name`, `timestamp`, `status`, `locked`.

#### `SYNO.SDS.Backup.Client.Explore.Target` — `get` (v1)

Opens the explore session / returns target capability (`data_enc`, `support_filter`,
`support_multi_version`, `uni_key`, …). Params: `task_id` + bundle + `additional=["support_filter","account_meta","from_cache"]`.

#### `SYNO.SDS.Backup.Client.Explore.Folder` — `list` (v1)

Sub-folders at a path inside a version.

**Parameters:** `task_id`, `version_id`, `backend` (+ filter bundle), `_sid`, plus:
- `node` — the folder to expand. **Raw relative path, no leading slash** (e.g. `docker` or `docker/stacks/myapp`). Special token **`@pathRoot`** lists the backup root (the shared folders). *(The DSM UI JSON-quotes `node`; unquoted also works.)*
- `limit` (optional) — e.g. `10001`

**Response:** array of `{name, path, type:"Folder", size, mtime, is_bad, browseable}`.
`path` is the full relative path — pass it back as the next `node` to descend.

#### `SYNO.SDS.Backup.Client.Explore.File` — `list` (v1)

Files (and folders) at a path. Same params as `Folder list` (`node` = the folder).
Response entries carry `type` (`File`/`Folder`) — filter to `File` for downloadable files.

#### `SYNO.SDS.Backup.Client.Explore.File` — `download` (v1)

Downloads one file's bytes. **Synchronous** — a single call returns the file body
(DSM fetches from the remote/cloud target inline; verified with a 6 MB file). Content-type
is the file, not JSON.

**Parameters:**
- `api`=`SYNO.SDS.Backup.Client.Explore.File`, `method`=`download`, `version`=`1`
- `task_id`, `version_id` (quoted), **`backend="HyperBackup-backend"`** + the filter bundle
- `source_path` — the file's full relative path (raw, no leading slash), e.g. `docker/stacks/myapp/config.yaml`
- `download_id` — any client-generated unique string (`Date.now()+random`); not server-issued
- `support_utf8_name=true`
- `_sid` + `X-SYNO-TOKEN` header

**Response:** the raw file bytes. On bad params → `{"error":{"code":4400}}` (JSON) — the
usual cause is a missing **`backend`** param.

#### `SYNO.SDS.Backup.Client.Explore.Job` — `list` (v1) — download progress / monitor

Tracks in-flight downloads. The client's **JobTray** polls this every **2 s** with the
`download_id`(s) it issued, to render progress and offer cancel.

**Parameters:**
- `api`=`SYNO.SDS.Backup.Client.Explore.Job`, `method`=`list`, `version`=`1`
- `backend="HyperBackup-backend"`
- `download_ids` — JSON array of the `download_id`(s) passed to `Explore.File download`
- `_sid`

**Response:**
```json
{ "success": true, "data": { "job_list": [
  { "id": "…", "unique": "…", "name": "config.yaml",
    "processed_size": 1048576, "total_size": 6239978,
    "status": "download", "can_cancel": true }
] } }
```

**Progress** = `processed_size / total_size` (`status`: `download`; `total_size` starts 0 while the server prepares/fetches from the cloud target, then fills in). A completed
or tiny download leaves `job_list` empty. To poll a download to completion: issue the
`download` call, then `Explore.Job list` with its `download_id` every ~2 s until the job
drops out of `job_list`. Cancel is a further `Explore.Job` method (`can_cancel` gates it).

> The `Explore.File download` HTTP response still streams the bytes directly; `Explore.Job`
> is the **side-channel progress** the UI uses (so a large/slow cloud fetch can show a bar
> and be cancelled). `isPreparingDownload` is just the client guard that blocks starting a
> second download while `download_ids` is non-empty (`wait_another_file_downloaded`).

### Minimal headless recovery (verified)

```bash
# 1) auth -> sid + synotoken (see best-practices)
# 2) find versions
curl ... api=SYNO.SDS.Backup.Client.Explore.Version method=list version=1 task_id=1 backend='"HyperBackup-backend"' <filter bundle>
# 3) browse:  Explore.Folder/File list with node="docker/stacks/myapp"
# 4) download one file (returns bytes):
curl ... -o config.yaml \
  api=SYNO.SDS.Backup.Client.Explore.File method=download version=1 \
  task_id=1 version_id='"141"' backend='"HyperBackup-backend"' \
  source_path=docker/stacks/myapp/config.yaml download_id=$(date +%s%N) \
  filter_keyword='""' filter_type='"any"' filter_size_option='"any"' \
  filter_size=0 filter_date_from=0 filter_date_to=0 support_utf8_name=true
```

#### `SYNO.SDS.Backup.Client.Explore.File` — `restore` (v1) — put a file back (async)

Restores an in-backup file **onto the NAS** at a chosen destination (vs `download`, which
streams bytes to the client). Runs as an **async job**.

**Parameters:** the Explorer bundle (`task_id`, `version_id`, `backend`, filters) plus:
- `source_path` — the file's path inside the backup
- `dest_path` — where to write it on the NAS
- `overwrite` — `true`/`false` (a `restore_unsafe_warn`/`ERR_SHARE_READ_ONLY` may gate it)

**Response:** returns a **`restore_id`**; the UI then opens a progress panel. Poll progress
with a **`status` method keyed by `restore_id`** every ~2 s (same cadence as the download
`Explore.Job` poller). Task-level `Task.status` flags `is_restoring` / `is_data_restoring`
/ `is_snapshot_restoring` / `is_lun_restoring` also reflect an in-flight restore.

> **Async pattern (mirrors download):** kick off `restore` → get `restore_id` → poll the
> `status` method until done. Not fired against a production task here; verify `dest_path`
> semantics + the exact `status` API on a throwaway task before automating.

### Whole-share restore (alternative)

For restoring entire shares/apps into place (not file-by-file), the DSM Restore wizard
uses `SYNO.Backup.Restore` / `SYNO.Backup.Share.Restore` (`list` observed) /
`SYNO.Backup.App2.Restore`. `SYNO.SDS.Backup.Client.Fuse.Target` FUSE-mounts a version as
a filesystem.

> **Offline alternative:** a multi-version archive (`.hbk`) is a directory of plain SQLite
> indexes + an LZ4 chunk store — [`cloakster/hyperbackup-tools`](https://github.com/cloakster/hyperbackup-tools)
> maps the schema and enumerates an archive without DSM, but does not reassemble file bytes.
