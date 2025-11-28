# Snapshot Replication - Replication Plans

**Category:** Storage Management

[← Back to Snapshot Replication](README.md)

---

**Endpoint:** `/webapi/entry.cgi`

---

## SYNO.Core.Share.Replication

#### Method: `List`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.Core.Share.Replication`
- `version` (required): `1`
- `method` (required): `List`
- `additional_info` (optional): Additional info fields (comma-separated: `status`, `last_sync`, `schedule`)
- `offset` (optional): Starting index (default: 0)
- `limit` (optional): Max results (default: 100)
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "plans": [
      {
        "id": "plan_1",
        "name": "Offsite Backup",
        "source_share": "Documents",
        "destination_host": "192.168.1.100",
        "destination_share": "Documents_Backup",
        "enabled": true,
        "status": "normal",
        "last_sync": 1732788000
      }
    ],
    "total": 1
  }
}
```

**Response Fields:**

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Replication plan ID |
| `name` | string | Plan name |
| `source_share` | string | Source shared folder |
| `destination_host` | string | Destination NAS IP/hostname |
| `destination_share` | string | Destination shared folder |
| `enabled` | boolean | Plan enabled |
| `status` | string | Replication status |
| `last_sync` | integer | Last sync timestamp (Unix time) |

---

#### Method: `Sync`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Share.Replication`
- `version` (required): `1`
- `method` (required): `Sync`
- `plan_id` (required): Replication plan ID
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "task_id": "sync_task_123"
  }
}
```

**Notes:**
- Replication requires Snapshot Replication package
- Source and destination must both support snapshots
- Replication is incremental (only changes are transferred)
- Use task_id to monitor sync progress

---

## SYNO.Core.Share.Replication.Task

#### Method: `Status`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.Core.Share.Replication.Task`
- `version` (required): `1`
- `method` (required): `Status`
- `task_id` (required): Task ID
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "status": "running",
    "progress": 45,
    "transferred": 536870912,
    "total": 1073741824
  }
}
```

**Response Fields:**

| Field | Type | Description |
|-------|------|-------------|
| `status` | string | Task status (`running`, `completed`, `failed`) |
| `progress` | integer | Progress percentage (0-100) |
| `transferred` | integer | Bytes transferred |
| `total` | integer | Total bytes to transfer |

**Notes:**
- Replication status: `normal`, `syncing`, `error`, `paused`
- Failed replications can be retried
- Replication preserves snapshots on destination

