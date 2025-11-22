# SYNO.ActiveBackup.Plan

**Category:** System

[← Back to API Reference](../README.md)

---


**Endpoint:** `entry.cgi`
**Versions:** 1-2


#### Method: `create`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Plan`
- `version` (required): `1`
- `method` (required): `create`
- `plan_uuid` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `plan_uuid`
- Error code 120 when parameter missing


#### Method: `delete`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Plan`
- `version` (required): `1`
- `method` (required): `delete`
- `plan_uuid` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `plan_uuid`
- Error code 120 when parameter missing


#### Method: `get`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Plan`
- `version` (required): `1`
- `method` (required): `get`
- `plan_uuid` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `plan_uuid`
- Error code 120 when parameter missing


#### Method: `list`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Plan`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID from login

**Response:**
```json
{
  "success": true
}
```


#### Method: `update`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Plan`
- `version` (required): `1`
- `method` (required): `update`
- `plan_uuid` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `plan_uuid`
- Error code 120 when parameter missing


---
