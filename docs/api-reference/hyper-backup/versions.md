# Hyper Backup - Versions, Sources & Restore

**Category:** Data Protection

[← Back to Hyper Backup](README.md)

---

**Endpoint:** `/webapi/entry.cgi`

Restore points (**versions**), the folder/app **sources** a task backs up, and the
**restore / file-browse** surface. Read methods verified on DSM 7.x by capturing the
Hyper Backup UI; the per-file browse/restore methods are noted where still uncaptured.

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

## Restore & file-browse (recovery path)

Browsing the files **inside** a version and restoring/downloading an individual file is
driven by the APIs below. These are **present on DSM 7** (confirmed via
[`SYNO.API.Info`](../dsm-core/authentication.md)) but their methods/params are **not
documented publicly** anywhere — the natural next capture target. Capture them against a
**throwaway task**, never a production one.

| API | Ver | Role | Status |
|-----|-----|------|--------|
| `SYNO.SDS.Backup.Client.Explore.Version` | 1-2 | list a task's versions to explore | methods uncaptured |
| `SYNO.SDS.Backup.Client.Explore.Folder` | 1-2 | browse folders inside a version | **uncaptured (capture target)** |
| `SYNO.SDS.Backup.Client.Explore.File` | 1-2 | browse/select files inside a version | **uncaptured (capture target)** |
| `SYNO.SDS.Backup.Client.Fuse.Target` | 1 | FUSE-mount a version as a filesystem | methods uncaptured |
| `SYNO.Backup.Restore` | 1-2 | restore action | partially seen |
| `SYNO.Backup.Share.Restore` | 1-2 | restore whole shares from a version | `list` seen |
| `SYNO.Backup.App2.Restore` | 1-2 | restore application data | methods uncaptured |

Captured from the Restore wizard (Folders-and-Packages path, read-only steps only):

- **`SYNO.Backup.Version list` v2** — `filter_name="success"`, `sort_direction="desc"`, `limit=-1` → all versions (see above).
- **`SYNO.Backup.Version summary` v1**.
- **`SYNO.Backup.Share.Restore` — `list` v1** — lists the shares restorable from the chosen version.

> **Offline alternative:** a multi-version archive (`.hbk`) is a directory of plain SQLite
> indexes + an LZ4 chunk store. [`cloakster/hyperbackup-tools`](https://github.com/cloakster/hyperbackup-tools)
> maps the schema (per-share/version `version_list` table; `candidate_chunk.db`; Pool
> `.index` over LZ4 buckets) and **enumerates** an archive without DSM — but does not yet
> reassemble file bytes.
