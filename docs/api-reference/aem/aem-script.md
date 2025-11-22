# SYNO.ActiveBackup.AEM.Script

**Category:** Aem

[← Back to API Reference](../README.md)

---


**Endpoint:** `entry.cgi`
**Versions:** 1-2


#### Method: `delete`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.AEM.Script`
- `version` (required): `1`
- `method` (required): `delete`
- `script_id` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `script_id`
- Error code 120 when parameter missing


#### Method: `prepare_file_for_join`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.AEM.Script`
- `version` (required): `1`
- `method` (required): `prepare_file_for_join`
- `_sid` (required): Session ID from login

**Response:**
```json
{
  "data": {
    "post_script_name": "",
    "pre_script_name": ""
  },
  "success": true
}
```


#### Method: `update`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.AEM.Script`
- `version` (required): `1`
- `method` (required): `update`
- `script_id` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `script_id`
- Error code 120 when parameter missing


---
