# SYNO.ActiveBackup.Storage

**Category:** System

[← Back to API Reference](../README.md)

---

**Endpoint:** `/webapi/entry.cgi`


#### Method: `automount_get`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Storage`
- `version` (required): `1`
- `method` (required): `automount_get`
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {}
}
```


#### Method: `automount_list_location`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Storage`
- `version` (required): `1`
- `method` (required): `automount_list_location`
- `_sid` (required): Session ID

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
- `_sid` (required): Session ID

**Notes:**
- Requires parameter: `task_id`
- Error code 120 when parameter missing

**Response:**
```json
{
  "success": true,
  "data": {}
}
```


#### Method: `check_mount`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Storage`
- `version` (required): `1`
- `method` (required): `check_mount`
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {}
}
```


#### Method: `download_private_key`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Storage`
- `version` (required): `1`
- `method` (required): `download_private_key`
- `pwd` (required): Required parameter
- `_sid` (required): Session ID

**Notes:**
- Requires parameter: `pwd`
- Error code 120 when parameter missing
- Supports file download

**Response:**
```json
{
  "success": true
}
```


#### Method: `list_dsm_share`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Storage`
- `version` (required): `1`
- `method` (required): `list_dsm_share`
- `task_id` (required): Required parameter
- `_sid` (required): Session ID

**Notes:**
- Requires parameter: `task_id`
- Error code 120 when parameter missing

**Response:**
```json
{
  "success": true,
  "data": {}
}
```


#### Method: `mount_dsm_enc_share`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Storage`
- `version` (required): `1`
- `method` (required): `mount_dsm_enc_share`
- `name` (required): Required parameter
- `_sid` (required): Session ID

**Notes:**
- Requires parameter: `name`
- Error code 120 when parameter missing

**Response:**
```json
{
  "success": true
}
```


#### Method: `umount_dsm_enc_share`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Storage`
- `version` (required): `1`
- `method` (required): `umount_dsm_enc_share`
- `mount_path` (required): Required parameter
- `_sid` (required): Session ID

**Notes:**
- Requires parameter: `mount_path`
- Error code 120 when parameter missing

**Response:**
```json
{
  "success": true
}
```


#### Method: `unmount`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Storage`
- `version` (required): `1`
- `method` (required): `unmount`
- `storage_id` (required): Required parameter
- `_sid` (required): Session ID

**Notes:**
- Requires parameter: `storage_id`
- Error code 120 when parameter missing

**Response:**
```json
{
  "success": true
}
```


#### Method: `upload_private_key`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Storage`
- `version` (required): `1`
- `method` (required): `upload_private_key`
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true
}
```


#### Method: `verify`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Storage`
- `version` (required): `1`
- `method` (required): `verify`
- `automount_enabled` (required): Required parameter
- `_sid` (required): Session ID

**Notes:**
- Requires parameter: `automount_enabled`
- Error code 120 when parameter missing

**Response:**
```json
{
  "success": true
}
```


---
