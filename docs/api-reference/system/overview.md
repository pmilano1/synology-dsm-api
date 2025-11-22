# SYNO.ActiveBackup.Overview

**Category:** System

[← Back to API Reference](../README.md)

---


**Endpoint:** `entry.cgi`
**Versions:** 1-2


#### Method: `list_activity`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Overview`
- `version` (required): `1`
- `method` (required): `list_activity`
- `_sid` (required): Session ID from login

**Response:**
```json
{
  "data": {
    "activity_list": [],
    "total": 0
  },
  "success": true
}
```

**Notes:**
- May take longer to respond


#### Method: `list_device_last_backup`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Overview`
- `version` (required): `1`
- `method` (required): `list_device_last_backup`
- `_sid` (required): Session ID from login

**Response:**
```json
{
  "data": {
    "device_list": [
      {
        "device_id": 3,
        "device_name": "PETER-PC",
        "task_name": "peterm-Default",
        "time_end": 1755850535,
        "time_start": 1755849604
      }
    ],
    "total": 4
  },
  "success": true
}
```

**Notes:**
- May take longer to respond


#### Method: `list_device_transfer_size`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Overview`
- `version` (required): `1`
- `method` (required): `list_device_transfer_size`
- `time_start` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `time_start`
- Error code 120 when parameter missing


#### Method: `list_result_status_summary`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Overview`
- `version` (required): `1`
- `method` (required): `list_result_status_summary`
- `_sid` (required): Session ID from login
- `filter` (required): Used value: `{}`

**Response:**
```json
{
  "data": {
    "info_list": [
      {
        "count": 1,
        "status": 2,
        "time_end": 1594742400,
        "time_start": 1594738800
      }
    ],
    "total": 4928
  },
  "success": true
}
```

**Notes:**
- May take longer to respond


#### Method: `list_type_transfer_size`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Overview`
- `version` (required): `1`
- `method` (required): `list_type_transfer_size`
- `_sid` (required): Session ID from login
- `filter` (required): Used value: `{}`

**Response:**
```json
{
  "data": {
    "info_list": [
      {
        "backup_type": 2,
        "elapsed_time": 4124,
        "processed_bytes": 713051653632,
        "time_end": 1594742400,
        "time_start": 1594738800,
        "transfered_bytes": 713051653632
      }
    ],
    "total": 4928
  },
  "success": true
}
```


---
