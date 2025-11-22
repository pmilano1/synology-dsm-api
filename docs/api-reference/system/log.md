# SYNO.ActiveBackup.Log

**Category:** System

[← Back to API Reference](../README.md)

---


**Endpoint:** `entry.cgi`
**Versions:** 1-2


#### Method: `cancel_download`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Log`
- `version` (required): `1`
- `method` (required): `cancel_download`
- `export_id` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `export_id`
- Error code 120 when parameter missing


#### Method: `check_progress`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Log`
- `version` (required): `1`
- `method` (required): `check_progress`
- `export_id` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `export_id`
- Error code 120 when parameter missing


#### Method: `clear`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Log`
- `version` (required): `1`
- `method` (required): `clear`
- `_sid` (required): Session ID from login

**Response:**
```json
{
  "success": true
}
```


#### Method: `download`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Log`
- `version` (required): `1`
- `method` (required): `download`
- `output_format` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `output_format`
- Error code 120 when parameter missing
- Supports file download


#### Method: `get_info`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Log`
- `version` (required): `1`
- `method` (required): `get_info`
- `_sid` (required): Session ID from login

**Response:**
```json
{
  "data": {
    "retention_policy": {
      "retention_counts": "0",
      "retention_days": "0"
    },
    "send_log_setting": {
      "destination_ip": "",
      "enable_send": false,
      "enable_ssl": false,
      "format": 0,
      "id": 1,
      "port": 514,
      "protocol": 0
    }
  },
  "success": true
}
```


#### Method: `list_log`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Log`
- `version` (required): `1`
- `method` (required): `list_log`
- `_sid` (required): Session ID from login

**Response:**
```json
{
  "data": {
    "count": 1,
    "logs": [
      {
        "backup_type": 0,
        "device_id": 0,
        "device_name": "",
        "error_code": 0,
        "log_id": 29286,
        "log_level": 2,
        "log_time": 1763829984,
        "log_type": 1009,
        "other_params": {
          "backup_type": 0,
          "device_id": 0,
          "device_name": "",
          "platform_type": 0,
          "task_id": 0,
          "task_name": "",
          "user_id": 1024,
          "user_name": "admin"
        },
        "result_id": 0,
        "task_id": 0,
        "task_name": "",
        "user_id": 1024,
        "user_name": "admin"
      }
    ]
  },
  "success": true
}
```

**Notes:**
- May take longer to respond


#### Method: `list_result`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Log`
- `version` (required): `1`
- `method` (required): `list_result`
- `_sid` (required): Session ID from login

**Response:**
```json
{
  "data": {
    "count": 7553,
    "results": [
      {
        "activity_uuid": "",
        "backup_type": 2,
        "detail_path": "",
        "error_count": 0,
        "job_action": 1,
        "none_count": 0,
        "result_id": 1,
        "status": 2,
        "success_count": 0,
        "task_config": {
          "device_list": [
            {
              "device_id": 1,
              "host_name": "HOSTNAME"
            }
          ]
        },
        "task_id": 1,
        "task_name": "peterm-Default",
        "time_end": 1594739532,
        "time_start": 1594735408,
        "warning_count": 0
      }
    ]
  },
  "success": true
}
```


#### Method: `list_result_detail`


#### Method: `send_test_log`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Log`
- `version` (required): `1`
- `method` (required): `send_test_log`
- `_sid` (required): Session ID from login

**Response:**
```json
{
  "success": true
}
```


#### Method: `set_info`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Log`
- `version` (required): `1`
- `method` (required): `set_info`
- `_sid` (required): Session ID from login

**Response:**
```json
{
  "success": true
}
```


#### Method: `set_send_log_setting`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Log`
- `version` (required): `1`
- `method` (required): `set_send_log_setting`
- `_sid` (required): Session ID from login

**Response:**
```json
{
  "success": true
}
```


#### Method: `upload_cert`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Log`
- `version` (required): `1`
- `method` (required): `upload_cert`
- `file_tmp` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `file_tmp`
- Error code 120 when parameter missing
- Supports file upload


---
