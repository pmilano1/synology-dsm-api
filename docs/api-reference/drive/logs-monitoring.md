# Synology Drive - Logs & Monitoring

**Category:** File Collaboration

[← Back to Synology Drive](README.md)

---

**Endpoint:** `/webapi/entry.cgi`

---

## SYNO.SynologyDrive.Log

#### Method: `List`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.SynologyDrive.Log`
- `version` (required): `1`
- `method` (required): `List`
- `share_type` (optional): Share type (`all`, `team_folder`, `personal`)
- `offset` (optional): Starting index (default: 0)
- `limit` (optional): Max results (default: 100)
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "logs": [
      {
        "time": 1732788000,
        "user": "john.doe",
        "action": "upload",
        "file_path": "/Team Projects/report.pdf",
        "ip_address": "192.168.1.100"
      }
    ],
    "total": 1
  }
}
```

**Response Fields:**

| Field | Type | Description |
|-------|------|-------------|
| `time` | integer | Log timestamp (Unix time) |
| `user` | string | Username |
| `action` | string | Action type |
| `file_path` | string | File path |
| `ip_address` | string | Client IP address |

**Action Types:**
- `upload` - File uploaded
- `download` - File downloaded
- `delete` - File deleted
- `rename` - File renamed
- `move` - File moved
- `share` - File shared

---

## SYNO.SynologyDrive.Share

#### Method: `ListActive`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.SynologyDrive.Share`
- `version` (required): `1`
- `method` (required): `ListActive`
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "shares": [
      {
        "name": "Team Projects",
        "type": "team_folder",
        "users": 10,
        "size": 5368709120,
        "file_count": 500
      }
    ],
    "total": 1
  }
}
```

---

## SYNO.SynologyDrive.Deletion

#### Method: `GetStatus`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.SynologyDrive.Deletion`
- `version` (required): `1`
- `method` (required): `GetStatus`
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "pending_deletions": 25,
    "deleted_size": 1073741824,
    "retention_days": 30
  }
}
```

**Response Fields:**

| Field | Type | Description |
|-------|------|-------------|
| `pending_deletions` | integer | Files pending permanent deletion |
| `deleted_size` | integer | Size of deleted files (bytes) |
| `retention_days` | integer | Days before permanent deletion |

**Notes:**
- Deleted files are retained for configured period
- Users can restore deleted files during retention
- Permanent deletion occurs after retention expires
- Admins can force immediate permanent deletion

