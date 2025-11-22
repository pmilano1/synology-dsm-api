# SYNO.ActiveBackup.Storage

**Category:** System

[← Back to API Reference](../README.md)

---


**Endpoint:** `entry.cgi`
**Versions:** 1-2


#### Method: `automount_get`


#### Method: `automount_list_location`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Storage`
- `version` (required): `1`
- `method` (required): `automount_list_location`
- `_sid` (required): Session ID from login

**Response:**
```json
{
  "data": [
    {
      "location": "sys_part",
      "status": 0
    }
  ],
  "success": true
}
```


#### Method: `check_dsm_share_mount`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Storage`
- `version` (required): `1`
- `method` (required): `check_dsm_share_mount`
- `task_id` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `task_id`
- Error code 120 when parameter missing


#### Method: `check_mount`


#### Method: `download_private_key`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Storage`
- `version` (required): `1`
- `method` (required): `download_private_key`
- `pwd` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `pwd`
- Error code 120 when parameter missing
- Supports file download


#### Method: `list_dsm_share`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Storage`
- `version` (required): `1`
- `method` (required): `list_dsm_share`
- `task_id` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `task_id`
- Error code 120 when parameter missing


#### Method: `mount_dsm_enc_share`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Storage`
- `version` (required): `1`
- `method` (required): `mount_dsm_enc_share`
- `name` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `name`
- Error code 120 when parameter missing


#### Method: `umount_dsm_enc_share`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Storage`
- `version` (required): `1`
- `method` (required): `umount_dsm_enc_share`
- `mount_path` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `mount_path`
- Error code 120 when parameter missing


#### Method: `unmount`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Storage`
- `version` (required): `1`
- `method` (required): `unmount`
- `storage_id` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `storage_id`
- Error code 120 when parameter missing


#### Method: `upload_private_key`


#### Method: `verify`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Storage`
- `version` (required): `1`
- `method` (required): `verify`
- `automount_enabled` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `automount_enabled`
- Error code 120 when parameter missing


---
