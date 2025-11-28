# Snapshot Replication - Volume Snapshots

**Category:** Storage Management

[← Back to Snapshot Replication](README.md)

---

**Endpoint:** `/webapi/entry.cgi`

---

## SYNO.Core.Share.Snapshot

#### Method: `List`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.Core.Share.Snapshot`
- `version` (required): `1`
- `method` (required): `List`
- `share_name` (required): Shared folder name
- `offset` (optional): Starting index (default: 0)
- `limit` (optional): Max results (default: 100)
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "snapshots": [
      {
        "id": "snapshot_1",
        "name": "@GMT-2025.11.28-10.00.00",
        "time_create": 1732788000,
        "description": "Daily backup",
        "is_locked": false,
        "size": 1073741824
      }
    ],
    "total": 1
  }
}
```

**Response Fields:**

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Snapshot ID |
| `name` | string | Snapshot name (GMT format) |
| `time_create` | integer | Creation timestamp (Unix time) |
| `description` | string | Snapshot description |
| `is_locked` | boolean | Locked status (protected from deletion) |
| `size` | integer | Snapshot size (bytes) |

---

#### Method: `Create`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Share.Snapshot`
- `version` (required): `1`
- `method` (required): `Create`
- `share_name` (required): Shared folder name
- `description` (optional): Snapshot description
- `is_locked` (optional): Lock snapshot (default: false)
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "snapshot_id": "snapshot_2"
  }
}
```

---

#### Method: `Delete`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Share.Snapshot`
- `version` (required): `1`
- `method` (required): `Delete`
- `share_name` (required): Shared folder name
- `snapshot_ids` (required): Snapshot IDs (comma-separated)
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true
}
```

---

#### Method: `SetAttr`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Share.Snapshot`
- `version` (required): `1`
- `method` (required): `SetAttr`
- `share_name` (required): Shared folder name
- `snapshot_id` (required): Snapshot ID
- `description` (optional): New description
- `is_locked` (optional): Lock status
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true
}
```

**Notes:**
- Btrfs file system required for volume snapshots
- Locked snapshots cannot be deleted
- Snapshots are read-only
- Snapshot names use GMT format: @GMT-YYYY.MM.DD-HH.MM.SS

