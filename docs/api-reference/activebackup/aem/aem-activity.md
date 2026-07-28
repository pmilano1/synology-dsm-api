# SYNO.ActiveBackup.AEM.Activity

**Category:** Aem

[← Back to API Reference](../README.md)

---

**Endpoint:** `/webapi/entry.cgi`


#### Method: `backup_result`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.AEM.Activity`
- `version` (required): `1`
- `method` (required): `backup_result`
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {}
}
```


#### Method: `backup_status`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.AEM.Activity`
- `version` (required): `1`
- `method` (required): `backup_status`
- `_sid` (required): Session ID

**Response:**
```json
{
  "data": {},
  "success": true
}
```


#### Method: `restore_result`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.AEM.Activity`
- `version` (required): `1`
- `method` (required): `restore_result`
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {}
}
```


#### Method: `write_vmm_log`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.AEM.Activity`
- `version` (required): `1`
- `method` (required): `write_vmm_log`
- `guest_id` (required): Required parameter
- `_sid` (required): Session ID

**Notes:**
- Requires parameter: `guest_id`
- Error code 120 when parameter missing

**Response:**
```json
{
  "success": true
}
```


---
