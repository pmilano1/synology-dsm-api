# SYNO.ActiveBackup.Device

**Category:** Core

[← Back to API Reference](../README.md)

---


**Endpoint:** `entry.cgi`
**Versions:** 1-2


#### Method: `list`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Device`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID from login

**Response:**
```json
{
  "data": {
    "devices": [
      {
        "agent_token": "REDACTED",
        "agentless_auth_policy": 0,
        "auto_discovery": false,
        "backup_type": 2,
        "create_time": 1594735305,
        "device_id": 1,
        "device_uuid": "37E1E2FE-B040-0F76-E903-40B0760FE904",
        "dsm_model": "",
        "dsm_unique": "",
        "host_ip": "192.168.X.X",
        "host_name": "HOSTNAME",
        "host_port": 0,
        "hypervisor_id": "",
        "inventory_id": 0,
        "kernel_version": "",
        "login_password": "REDACTED",
        "login_time": 1594735318,
        "login_user": "peterm",
        "login_user_id": 1027,
        "mssql_password": "REDACTED",
        "mssql_user": "",
        "oracle_password": "REDACTED",
        "oracle_user": "",
        "os_name": "Windows 11(64-bit)",
        "task_count": 1,
        "time_zone": -18000,
        "vm_moid_path": ""
      }
    ],
    "total": 4,
    "total_devices_of_backup_type": 0
  },
  "success": true
}
```

**Notes:**
- May take longer to respond


#### Method: `list_restorable_version`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Device`
- `version` (required): `1`
- `method` (required): `list_restorable_version`
- `device_id` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `device_id`
- Error code 120 when parameter missing


#### Method: `list_tasks`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Device`
- `version` (required): `1`
- `method` (required): `list_tasks`
- `device_ids` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `device_ids`
- Error code 120 when parameter missing
- May take longer to respond


#### Method: `remove`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Device`
- `version` (required): `1`
- `method` (required): `remove`
- `device_ids` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `device_ids`
- Error code 120 when parameter missing


#### Method: `set_credential`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Device`
- `version` (required): `1`
- `method` (required): `set_credential`
- `device_ids` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `device_ids`
- Error code 120 when parameter missing


---
