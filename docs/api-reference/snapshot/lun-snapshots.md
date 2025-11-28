# Snapshot Replication - LUN Snapshots

**Category:** Storage Management

[← Back to Snapshot Replication](README.md)

---

**Endpoint:** `/webapi/entry.cgi`

---

## SYNO.Core.ISCSI.LUN

#### Method: `List`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.Core.ISCSI.LUN`
- `version` (required): `1`
- `method` (required): `List`
- `types` (optional): LUN types (comma-separated: `file`, `block`, `advanced`)
- `offset` (optional): Starting index (default: 0)
- `limit` (optional): Max results (default: 100)
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "luns": [
      {
        "uuid": "lun-uuid-1",
        "name": "LUN1",
        "type": "file",
        "size": 10737418240,
        "allocated": 5368709120,
        "status": "normal"
      }
    ],
    "total": 1
  }
}
```

**Response Fields:**

| Field | Type | Description |
|-------|------|-------------|
| `uuid` | string | LUN UUID |
| `name` | string | LUN name |
| `type` | string | LUN type (`file`, `block`, `advanced`) |
| `size` | integer | LUN size (bytes) |
| `allocated` | integer | Allocated space (bytes) |
| `status` | string | LUN status |

---

## SYNO.Core.ISCSI.LUN.Snapshot

#### Method: `List`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.Core.ISCSI.LUN.Snapshot`
- `version` (required): `1`
- `method` (required): `List`
- `src_lun_uuid` (required): Source LUN UUID
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
        "uuid": "snapshot-uuid-1",
        "name": "LUN1_snapshot_1",
        "time_create": 1732788000,
        "description": "Before update",
        "is_locked": false
      }
    ],
    "total": 1
  }
}
```

---

#### Method: `Create`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.ISCSI.LUN.Snapshot`
- `version` (required): `1`
- `method` (required): `Create`
- `lun_id` (required): LUN ID
- `description` (optional): Snapshot description
- `is_locked` (optional): Lock snapshot (default: false)
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "snapshot_uuid": "snapshot-uuid-2"
  }
}
```

---

#### Method: `Delete`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.ISCSI.LUN.Snapshot`
- `version` (required): `1`
- `method` (required): `Delete`
- `snapshot_uuids` (required): Snapshot UUIDs (comma-separated)
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true
}
```

**Notes:**
- iSCSI Manager package required
- LUN snapshots are space-efficient
- Locked snapshots cannot be deleted
- Snapshots can be cloned to create new LUNs

