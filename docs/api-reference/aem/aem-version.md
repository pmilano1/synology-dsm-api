# SYNO.ActiveBackup.AEM.Version

**Category:** Aem

[← Back to API Reference](../README.md)

---


**Endpoint:** `entry.cgi`
**Versions:** 1-2


#### Method: `create`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.AEM.Version`
- `version` (required): `1`
- `method` (required): `create`
- `workload_uuid` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `workload_uuid`
- Error code 120 when parameter missing


#### Method: `download`


#### Method: `download_meta`


#### Method: `get_apdb_result`


#### Method: `get_db_backup_info`


#### Method: `get_detail`


#### Method: `get_volume_info`


#### Method: `list_entry`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.AEM.Version`
- `version` (required): `1`
- `method` (required): `list_entry`
- `id` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `id`
- Error code 120 when parameter missing


#### Method: `post_hook`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.AEM.Version`
- `version` (required): `1`
- `method` (required): `post_hook`
- `action_type` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `action_type`
- Error code 120 when parameter missing


#### Method: `pre_hook`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.AEM.Version`
- `version` (required): `1`
- `method` (required): `pre_hook`
- `action_type` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `action_type`
- Error code 120 when parameter missing


#### Method: `restore_entry`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.AEM.Version`
- `version` (required): `1`
- `method` (required): `restore_entry`
- `version_additional_meta` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `version_additional_meta`
- Error code 120 when parameter missing


#### Method: `rollback_copy_versions`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.AEM.Version`
- `version` (required): `1`
- `method` (required): `rollback_copy_versions`
- `versions` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `versions`
- Error code 120 when parameter missing


#### Method: `validate_external_storage`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.AEM.Version`
- `version` (required): `1`
- `method` (required): `validate_external_storage`
- `connection_id` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `connection_id`
- Error code 120 when parameter missing


---
