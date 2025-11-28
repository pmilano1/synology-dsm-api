# Virtual Machine Manager - Virtual Machines

**Category:** Virtualization

[← Back to Virtual Machine Manager](README.md)

---

**Endpoint:** `/webapi/entry.cgi`

---

## SYNO.Virtualization.Guest

#### Method: `List`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.Virtualization.Guest`
- `version` (required): `1`
- `method` (required): `List`
- `additional` (optional): Include additional info (default: false)
- `offset` (optional): Starting index (default: 0)
- `limit` (optional): Max results (default: 100)
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "guests": [
      {
        "guest_id": "vm-1",
        "guest_name": "Ubuntu Server",
        "status": "running",
        "vcpu_num": 2,
        "vram_size": 4096,
        "storage_size": 53687091200,
        "autorun": 1
      }
    ],
    "total": 1
  }
}
```

**Response Fields:**

| Field | Type | Description |
|-------|------|-------------|
| `guest_id` | string | VM ID |
| `guest_name` | string | VM name |
| `status` | string | VM status (`running`, `stopped`, `paused`) |
| `vcpu_num` | integer | Number of virtual CPUs |
| `vram_size` | integer | RAM size (MB) |
| `storage_size` | integer | Storage size (bytes) |
| `autorun` | integer | Auto-start on boot (0=disabled, 1=enabled) |

---

#### Method: `Get`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.Virtualization.Guest`
- `version` (required): `1`
- `method` (required): `Get`
- `guest_id` (optional): VM ID
- `guest_name` (optional): VM name
- `additional` (optional): Additional info fields (comma-separated)
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "guest_id": "vm-1",
    "guest_name": "Ubuntu Server",
    "status": "running",
    "vcpu_num": 2,
    "vram_size": 4096,
    "storage_size": 53687091200,
    "network": [
      {
        "mac": "00:11:32:AB:CD:EF",
        "network_name": "default"
      }
    ]
  }
}
```

**Notes:**
- Use either `guest_id` or `guest_name` parameter
- Additional info fields: `network`, `storage`, `snapshot`

---

#### Method: `PowerOn`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Virtualization.Guest`
- `version` (required): `1`
- `method` (required): `PowerOn`
- `guest_id` (optional): VM ID
- `guest_name` (optional): VM name
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "task_id": "task_123"
  }
}
```

---

#### Method: `PowerOff`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Virtualization.Guest`
- `version` (required): `1`
- `method` (required): `PowerOff`
- `guest_id` (optional): VM ID
- `guest_name` (optional): VM name
- `force` (optional): Force power off (default: false)
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "task_id": "task_124"
  }
}
```

---

#### Method: `Shutdown`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Virtualization.Guest`
- `version` (required): `1`
- `method` (required): `Shutdown`
- `guest_id` (optional): VM ID
- `guest_name` (optional): VM name
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "task_id": "task_125"
  }
}
```

**Notes:**
- `Shutdown` sends ACPI shutdown signal (graceful)
- `PowerOff` with `force=true` immediately stops VM (ungraceful)
- Use task_id to monitor operation progress

---

#### Method: `Delete`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Virtualization.Guest`
- `version` (required): `1`
- `method` (required): `Delete`
- `guest_id` (optional): VM ID
- `guest_name` (optional): VM name
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true
}
```

---

#### Method: `Set`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Virtualization.Guest`
- `version` (required): `1`
- `method` (required): `Set`
- `guest_id` (optional): VM ID
- `guest_name` (optional): VM name
- `vcpu_num` (optional): Number of virtual CPUs
- `vram_size` (optional): RAM size (MB)
- `autorun` (optional): Auto-start on boot (0=disabled, 1=enabled)
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true
}
```

**Notes:**
- VM must be stopped to change CPU/RAM configuration
- Auto-run setting can be changed while VM is running
- Use either `guest_id` or `guest_name` parameter

