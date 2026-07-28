# Hyper Backup - Tasks

**Category:** Data Protection

[← Back to Hyper Backup](README.md)

---

**Endpoint:** `/webapi/entry.cgi`

Methods and payloads below were **verified against a live NAS running DSM 7.x**
by capturing the Hyper Backup UI's own requests, except where marked *community-confirmed*
(method name from [`N4S4/synology-api`](https://github.com/N4S4/synology-api) `core_backup.py`,
not yet wire-captured here). The UI batches several reads inside a
[`SYNO.Entry.Request`](../dsm-core/README.md) compound; each still works called directly.

---

## SYNO.Backup.Task

#### Method: `list`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.Backup.Task`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID
- `sort_by` (optional): quoted JSON string, e.g. `"name"`
- `additional` (optional): JSON array — e.g. `["last_bkp_time","last_bkp_result","get_source","is_modified","progress_title_type"]`
- `node` (optional): quoted JSON string, e.g. `"module_root"`

**Response:**
```json
{
  "success": true,
  "data": {
    "is_restoring": false,
    "is_downloading": false,
    "is_data_restoring": false,
    "is_lun_restoring": false,
    "is_snapshot_restoring": false,
    "task_list": [
      {
        "name": "Backup Task 1",
        "repo_id": 1,
        "data_type": "data",
        "data_enc": false,
        "is_modified": false,
        "last_bkp_time": "2025/01/15 02:00:00",
        "last_bkp_end_time": "2025/01/15 02:12:30",
        "last_bkp_result": "done",
        "ext3ShareList": [],
        "source": { "app_config": [], "app_list": ["..."] }
      }
    ]
  }
}
```

**Response Fields:**

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Task name |
| `repo_id` | integer | Repository id (see [Repositories](repositories.md)) |
| `data_type` | string | `data` (folders/packages), `lun`, etc. |
| `last_bkp_result` | string | `done`, `fail`, `interrupt`, … |
| `last_bkp_time` / `last_bkp_end_time` | string | Start / end of last run (`YYYY/MM/DD HH:MM:SS`) |
| `is_modified` | bool | Task edited since last backup |
| `is_restoring` / `is_downloading` | bool | Top-level activity flags |

---

#### Method: `get`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.Backup.Task`
- `version` (required): `1`
- `method` (required): `get`
- `task_id` (required): Task ID
- `_sid` (required): Session ID
- `additional` (optional): JSON array — `["repository","schedule"]`

**Response:** (secrets in `repository` are masked/redacted — never store real values)
```json
{
  "success": true,
  "data": {
    "name": "Backup Task 1",
    "repo_id": 1,
    "data_type": "data",
    "data_enc": false,
    "repository": {
      "repo_id": 1,
      "target_type": "cloud_image",
      "transfer_type": "aws_s3",
      "bucket": "example-bucket",
      "container": "example-bucket",
      "key": "AKIA…REDACTED",
      "secret": "########",
      "request_style": "virtual_host_style",
      "verify_ssl_cert": true
    },
    "schedule": { }
  }
}
```
`transfer_type` observed: `aws_s3`. `target_type`: `cloud_image` (multi-version `.hbk`
image on S3). Other `transfer_type`s correspond to the destinations in
[Repositories](repositories.md).

---

#### Method: `status`

**HTTP Method:** GET

Live run-state of a task (this is the real method — earlier drafts guessed `GetStatus`).

**Parameters:**
- `api` (required): `SYNO.Backup.Task`
- `version` (required): `1`
- `method` (required): `status`
- `task_id` (required): Task ID
- `_sid` (required): Session ID
- `blOnline` (optional): `true`/`false` — probe the target's online state
- `additional` (optional): JSON array — e.g. `["last_bkp_time","next_bkp_time","last_bkp_result","is_modified","last_bkp_progress","last_bkp_success_version"]`

**Response:**
```json
{
  "success": true,
  "data": {
    "last_bkp_result": "done",
    "last_bkp_error": "",
    "last_bkp_error_code": 4401,
    "last_bkp_time": "2025/01/15 02:00:00",
    "last_bkp_end_time": "2025/01/15 02:12:30",
    "last_bkp_success_time": "2025/01/15 02:12:30",
    "last_bkp_success_version": "42",
    "next_bkp_time": "2025/01/16 02:00",
    "is_modified": false,
    "schedule": { "schedule": { "date": "2025/1/16", "hour": 19, "min": 40, "date_type": 0 } }
  }
}
```

---

#### Method: `get_support_cloud`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.Backup.Task`
- `version` (required): `1`
- `method` (required): `get_support_cloud`
- `_sid` (required): Session ID

**Response:**
```json
{ "success": true, "data": { "allow_all": true, "allow_list": [] } }
```

---

#### Method: `correct_synorbd`

**HTTP Method:** GET

Maintenance call fired on app load (reconciles the local `.synorbd` bookkeeping DB). No
parameters beyond `api`/`version`/`method`/`_sid`.

**Parameters:**
- `api` (required): `SYNO.Backup.Task`
- `version` (required): `1`
- `method` (required): `correct_synorbd`
- `_sid` (required): Session ID

**Response:**
```json
{ "success": true }
```

---

#### Method: `backup` *(community-confirmed)*

**HTTP Method:** POST — run the task now (the real "Back Up Now"; earlier drafts guessed `Run`).

**Parameters:**
- `api` (required): `SYNO.Backup.Task`
- `version` (required): `1`
- `method` (required): `backup`
- `task_id` (required): Task ID
- `_sid` (required): Session ID
- `X-SYNO-TOKEN` header (required): CSRF token (state-changing call)

**Response:**
```json
{ "success": true }
```

---

#### Methods: `cancel`, `suspend`, `resume`, `discard`, `delete` *(community-confirmed)*

**HTTP Method:** POST — same shape as `backup`.

**Parameters:**
- `api` (required): `SYNO.Backup.Task`
- `version` (required): `1`
- `method` (required): one of `cancel`, `suspend`, `resume`, `discard`, `delete`
- `task_id` (required): Task ID
- `_sid` (required): Session ID
- `X-SYNO-TOKEN` header (required): CSRF token (state-changing call)

| Method | Effect |
|--------|--------|
| `cancel` | Stop the running backup |
| `suspend` | Pause a running backup (resumable; partial data kept) |
| `resume` | Continue a suspended backup |
| `discard` | Discard a suspended/partial backup |
| `delete` | Delete the task |

**Response:**
```json
{ "success": true }
```

> Method names in this block are from `N4S4/synology-api` and were **not** fired against
> the live production task during capture. Verify against a throwaway task before relying
> on them for automation.
