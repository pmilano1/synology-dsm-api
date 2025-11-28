# Hyper Backup - Tasks

**Category:** Data Protection

[← Back to Hyper Backup](README.md)

---

**Endpoint:** `/webapi/entry.cgi`

---

## SYNO.Backup.Task

#### Method: `List`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.Backup.Task`
- `version` (required): `1`
- `method` (required): `List`
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "tasks": [
      {
        "task_id": "1",
        "name": "Daily System Backup",
        "status": "idle",
        "last_backup_time": 1732788000,
        "next_backup_time": 1732874400,
        "destination": "rsync://backup.example.com/backups"
      }
    ],
    "total": 1
  }
}
```

**Response Fields:**

| Field | Type | Description |
|-------|------|-------------|
| `task_id` | string | Task ID |
| `name` | string | Task name |
| `status` | string | Task status |
| `last_backup_time` | integer | Last backup timestamp (Unix time) |
| `next_backup_time` | integer | Next backup timestamp (Unix time) |
| `destination` | string | Backup destination |

**Task Status:**
- `idle` - Not running
- `running` - Backup in progress
- `suspended` - Backup suspended
- `error` - Error occurred

---

#### Method: `Get`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.Backup.Task`
- `version` (required): `1`
- `method` (required): `Get`
- `task_id` (required): Task ID
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "task_id": "1",
    "name": "Daily System Backup",
    "status": "idle",
    "source_folders": ["/volume1/important"],
    "destination": "rsync://backup.example.com/backups",
    "schedule": {
      "enabled": true,
      "hour": 2,
      "minute": 0
    }
  }
}
```

---

#### Method: `GetStatus`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.Backup.Task`
- `version` (required): `1`
- `method` (required): `GetStatus`
- `task_id` (required): Task ID
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "status": "running",
    "progress": 45,
    "files_backed_up": 150,
    "bytes_backed_up": 104857600,
    "estimated_time_remaining": 1800
  }
}
```

---

#### Method: `Run`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Backup.Task`
- `version` (required): `1`
- `method` (required): `Run`
- `task_id` (required): Task ID
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true
}
```

**Notes:**
- Runs backup immediately regardless of schedule
- Task must not already be running

---

#### Method: `Cancel`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Backup.Task`
- `version` (required): `1`
- `method` (required): `Cancel`
- `task_id` (required): Task ID
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true
}
```

---

#### Method: `Suspend`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Backup.Task`
- `version` (required): `1`
- `method` (required): `Suspend`
- `task_id` (required): Task ID
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true
}
```

**Notes:**
- Suspends running backup
- Can be resumed later
- Partial backup data is preserved

---

#### Method: `Resume`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Backup.Task`
- `version` (required): `1`
- `method` (required): `Resume`
- `task_id` (required): Task ID
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true
}
```

**Notes:**
- Resumes suspended backup
- Continues from suspension point

