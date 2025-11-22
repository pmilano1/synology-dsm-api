# SYNO.ActiveBackup.General

**Category:** System

[← Back to API Reference](../README.md)

---


**Endpoint:** `entry.cgi`
**Versions:** 1-2


#### Method: `fsync`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.General`
- `version` (required): `1`
- `method` (required): `fsync`
- `path` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `path`
- Error code 120 when parameter missing


#### Method: `get_sys_mem_info`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.General`
- `version` (required): `1`
- `method` (required): `get_sys_mem_info`
- `_sid` (required): Session ID from login

**Response:**
```json
{
  "data": {
    "sysMemInfo": {
      "free": 10764906496,
      "total": 16624132096,
      "used": 5859225600
    }
  },
  "success": true
}
```


#### Method: `is_syno_internal`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.General`
- `version` (required): `1`
- `method` (required): `is_syno_internal`
- `_sid` (required): Session ID from login

**Response:**
```json
{
  "data": {
    "is_internal": 0
  },
  "success": true
}
```


---
