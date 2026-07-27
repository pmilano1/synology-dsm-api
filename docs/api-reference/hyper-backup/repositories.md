# Hyper Backup - Repositories & Targets

**Category:** Data Protection

[← Back to Hyper Backup](README.md)

---

**Endpoint:** `/webapi/entry.cgi`

A **repository** is the backup destination record (S3, rsync, local, etc.) referenced by
a task via `repo_id`. A **target** is that destination's live state (online, size,
capability). Read methods verified on DSM 7.x; `list`/`error_detect` are
*community-confirmed* from [`N4S4/synology-api`](https://github.com/N4S4/synology-api).

---

## SYNO.Backup.Repository

#### Method: `get`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.Backup.Repository`
- `version` (required): `1`
- `method` (required): `get`
- `task_id` (required): Task ID (or `repo_id`)
- `_sid` (required): Session ID

**Response:** (destination credentials are masked — never store real values)
```json
{
  "success": true,
  "data": {
    "repo_id": 1,
    "target_type": "cloud_image",
    "transfer_type": "aws_s3",
    "bucket": "example-bucket",
    "container": "example-bucket",
    "key": "AKIA…REDACTED",
    "secret": "########",
    "request_style": "virtual_host_style",
    "verify_ssl_cert": true
  }
}
```

**Response Fields:**

| Field | Type | Description |
|-------|------|-------------|
| `repo_id` | integer | Repository id (referenced by tasks) |
| `target_type` | string | `cloud_image` (multi-version `.hbk`), `local`, `network`, … |
| `transfer_type` | string | Destination driver: `aws_s3`, `rsync`, `webdav`, `azure`, … |
| `bucket` / `container` | string | Bucket/container name (cloud targets) |
| `request_style` | string | `virtual_host_style` / `path_style` (S3) |
| `verify_ssl_cert` | bool | Validate the destination's TLS cert |

---

#### Method: `list` *(community-confirmed)*

**HTTP Method:** GET — enumerate all repositories.

**Parameters:** `api`, `version`=`1`, `method`=`list`, `_sid`.

**Response:** array of repository objects (same shape as `get`).

---

## SYNO.Backup.Target

#### Method: `get`

**HTTP Method:** GET — live state/capability of a task's destination.

**Parameters:**
- `api` (required): `SYNO.Backup.Target`
- `version` (required): `1`
- `method` (required): `get`
- `task_id` (required): Task ID
- `_sid` (required): Session ID
- `additional` (optional): JSON array — `["is_online","used_size","check_task_key","check_auth","account_meta"]`

**Response:**
```json
{
  "success": true,
  "data": {
    "is_online": true,
    "format_type": "cloud_image",
    "used_size": 123456789,
    "used_size_cache": 12345678,
    "data_comp": true,
    "data_enc": false,
    "support_multi_version": true,
    "capability": {
      "support_download": true,
      "support_filter": true,
      "support_statistics": true
    }
  }
}
```

**Response Fields:**

| Field | Type | Description |
|-------|------|-------------|
| `is_online` | bool | Destination reachable now |
| `format_type` | string | Backup format at the target (`cloud_image`, …) |
| `used_size` | integer | Bytes used at the destination |
| `support_multi_version` | bool | Target holds multiple versions (`.hbk`) |
| `capability.support_download` | bool | Individual-file download supported |

---

#### Methods: `error_detect`, `error_detect_cancel` *(community-confirmed)*

**HTTP Method:** POST — start / cancel a connectivity+integrity probe of the target
(`task_id` + `X-SYNO-TOKEN`). **Response:** `{ "success": true }`.
