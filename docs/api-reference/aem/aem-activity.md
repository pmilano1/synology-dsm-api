# SYNO.ActiveBackup.AEM.Activity

**Category:** Aem

[← Back to API Reference](../README.md)

---


**Endpoint:** `entry.cgi`
**Versions:** 1-2


#### Method: `backup_result`


#### Method: `backup_status`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.AEM.Activity`
- `version` (required): `1`
- `method` (required): `backup_status`
- `_sid` (required): Session ID from login

**Response:**
```json
{
  "data": {},
  "success": true
}
```


#### Method: `restore_result`


#### Method: `write_vmm_log`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.AEM.Activity`
- `version` (required): `1`
- `method` (required): `write_vmm_log`
- `guest_id` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `guest_id`
- Error code 120 when parameter missing


---
