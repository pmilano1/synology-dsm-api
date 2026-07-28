# SYNO.ActiveBackup.AEM.Version

**Category:** Aem

[← Back to API Reference](../README.md)

---

**Endpoint:** `/webapi/entry.cgi`


#### Method: `create`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.AEM.Version`
- `version` (required): `1`
- `method` (required): `create`
- `workload_uuid` (required): Required parameter
- `_sid` (required): Session ID

**Notes:**
- Requires parameter: `workload_uuid`
- Error code 120 when parameter missing

**Response:**
```json
{
  "success": true
}
```


#### Method: `download`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.AEM.Version`
- `version` (required): `1`
- `method` (required): `download`
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true
}
```


#### Method: `download_meta`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.AEM.Version`
- `version` (required): `1`
- `method` (required): `download_meta`
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true
}
```


#### Method: `get_apdb_result`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.AEM.Version`
- `version` (required): `1`
- `method` (required): `get_apdb_result`
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {}
}
```


#### Method: `get_db_backup_info`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.AEM.Version`
- `version` (required): `1`
- `method` (required): `get_db_backup_info`
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {}
}
```


#### Method: `get_detail`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.AEM.Version`
- `version` (required): `1`
- `method` (required): `get_detail`
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {}
}
```


#### Method: `get_volume_info`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.AEM.Version`
- `version` (required): `1`
- `method` (required): `get_volume_info`
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {}
}
```


#### Method: `list_entry`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.AEM.Version`
- `version` (required): `1`
- `method` (required): `list_entry`
- `id` (required): Required parameter
- `_sid` (required): Session ID

**Notes:**
- Requires parameter: `id`
- Error code 120 when parameter missing

**Response:**
```json
{
  "success": true,
  "data": {}
}
```


#### Method: `post_hook`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.AEM.Version`
- `version` (required): `1`
- `method` (required): `post_hook`
- `action_type` (required): Required parameter
- `_sid` (required): Session ID

**Notes:**
- Requires parameter: `action_type`
- Error code 120 when parameter missing

**Response:**
```json
{
  "success": true
}
```


#### Method: `pre_hook`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.AEM.Version`
- `version` (required): `1`
- `method` (required): `pre_hook`
- `action_type` (required): Required parameter
- `_sid` (required): Session ID

**Notes:**
- Requires parameter: `action_type`
- Error code 120 when parameter missing

**Response:**
```json
{
  "success": true
}
```


#### Method: `restore_entry`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.AEM.Version`
- `version` (required): `1`
- `method` (required): `restore_entry`
- `version_additional_meta` (required): Required parameter
- `_sid` (required): Session ID

**Notes:**
- Requires parameter: `version_additional_meta`
- Error code 120 when parameter missing

**Response:**
```json
{
  "success": true
}
```


#### Method: `rollback_copy_versions`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.AEM.Version`
- `version` (required): `1`
- `method` (required): `rollback_copy_versions`
- `versions` (required): Required parameter
- `_sid` (required): Session ID

**Notes:**
- Requires parameter: `versions`
- Error code 120 when parameter missing

**Response:**
```json
{
  "success": true
}
```


#### Method: `validate_external_storage`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.AEM.Version`
- `version` (required): `1`
- `method` (required): `validate_external_storage`
- `connection_id` (required): Required parameter
- `_sid` (required): Session ID

**Notes:**
- Requires parameter: `connection_id`
- Error code 120 when parameter missing

**Response:**
```json
{
  "success": true
}
```


---
