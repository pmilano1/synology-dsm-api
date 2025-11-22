# SYNO.ActiveBackup.Restore

**Category:** Core

[← Back to API Reference](../README.md)

---


**Endpoint:** `entry.cgi`
**Versions:** 1-2


#### Method: `clear`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Restore`
- `version` (required): `1`
- `method` (required): `clear`
- `sessions` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `sessions`
- Error code 120 when parameter missing


#### Method: `list`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Restore`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID from login

**Response:**
```json
{
  "data": {
    "restore_infos": [],
    "total": 0
  },
  "success": true
}
```

**Notes:**
- May take longer to respond


#### Method: `pause`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Restore`
- `version` (required): `1`
- `method` (required): `pause`
- `job_ids` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `job_ids`
- Error code 120 when parameter missing


#### Method: `resume`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Restore`
- `version` (required): `1`
- `method` (required): `resume`
- `job_ids` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `job_ids`
- Error code 120 when parameter missing


#### Method: `status`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Restore`
- `version` (required): `1`
- `method` (required): `status`
- `job_id` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `job_id`
- Error code 120 when parameter missing
- May take longer to respond


#### Method: `stop`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Restore`
- `version` (required): `1`
- `method` (required): `stop`
- `_sid` (required): Session ID from login

**Response:**
```json
{
  "success": true
}
```


---
