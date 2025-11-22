# SYNO.ActiveBackup.AEM.Task

**Category:** Aem

[← Back to API Reference](../README.md)

---


**Endpoint:** `entry.cgi`
**Versions:** 1-2


#### Method: `list_auto_backup_rule`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.AEM.Task`
- `version` (required): `1`
- `method` (required): `list_auto_backup_rule`
- `_sid` (required): Session ID from login

**Response:**
```json
{
  "success": true
}
```


#### Method: `list_with_device`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.AEM.Task`
- `version` (required): `1`
- `method` (required): `list_with_device`
- `backup_type` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `backup_type`
- Error code 120 when parameter missing


---
