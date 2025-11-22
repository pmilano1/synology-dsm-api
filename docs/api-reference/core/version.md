# SYNO.ActiveBackup.Version

**Category:** Core

[← Back to API Reference](../README.md)

---


**Endpoint:** `entry.cgi`
**Versions:** 1-2


#### Method: `delete`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Version`
- `version` (required): `1`
- `method` (required): `delete`
- `task_id` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `task_id`
- Error code 120 when parameter missing


#### Method: `download`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Version`
- `version` (required): `1`
- `method` (required): `download`
- `device_id` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `device_id`
- Error code 120 when parameter missing
- Supports file download


#### Method: `list`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Version`
- `version` (required): `1`
- `method` (required): `list`
- `task_id` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `task_id`
- Error code 120 when parameter missing


#### Method: `list_node`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Version`
- `version` (required): `1`
- `method` (required): `list_node`
- `device_id` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `device_id`
- Error code 120 when parameter missing


#### Method: `lock`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Version`
- `version` (required): `1`
- `method` (required): `lock`
- `task_id` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `task_id`
- Error code 120 when parameter missing


#### Method: `restore`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Version`
- `version` (required): `1`
- `method` (required): `restore`
- `device_id` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `device_id`
- Error code 120 when parameter missing


---
