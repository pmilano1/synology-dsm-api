# Virtual Machine Manager - Tasks

**Category:** Virtualization

[← Back to Virtual Machine Manager](README.md)

---

**Endpoint:** `/webapi/entry.cgi`

---

## SYNO.Virtualization.Task

#### Method: `List`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.Virtualization.Task`
- `version` (required): `1`
- `method` (required): `List`
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "tasks": [
      "task_123",
      "task_124",
      "task_125"
    ]
  }
}
```

---

#### Method: `Get`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.Virtualization.Task`
- `version` (required): `1`
- `method` (required): `Get`
- `taskid` (required): Task ID
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "task_id": "task_123",
    "status": "running",
    "progress": 65,
    "operation": "power_on",
    "guest_id": "vm-1"
  }
}
```

**Response Fields:**

| Field | Type | Description |
|-------|------|-------------|
| `task_id` | string | Task ID |
| `status` | string | Task status (`running`, `completed`, `failed`) |
| `progress` | integer | Progress percentage (0-100) |
| `operation` | string | Operation type |
| `guest_id` | string | Associated VM ID |

---

#### Method: `Clear`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Virtualization.Task`
- `version` (required): `1`
- `method` (required): `Clear`
- `taskid` (required): Task ID
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true
}
```

**Notes:**
- Tasks are created for asynchronous operations
- Completed tasks can be cleared to free resources
- Failed tasks contain error information
- Task status: `running`, `completed`, `failed`, `cancelled`

