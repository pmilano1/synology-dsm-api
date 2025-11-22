# SYNO.ActiveBackup.RestoreVM

**Category:** Vm

[← Back to API Reference](../README.md)

---


**Endpoint:** `entry.cgi`
**Versions:** 1-2


#### Method: `abe_cancel`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.RestoreVM`
- `version` (required): `1`
- `method` (required): `abe_cancel`
- `_sid` (required): Session ID from login

**Response:**
```json
{
  "success": true
}
```


#### Method: `abe_verify`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.RestoreVM`
- `version` (required): `1`
- `method` (required): `abe_verify`
- `_sid` (required): Session ID from login

**Response:**
```json
{
  "success": true
}
```


#### Method: `check_spec`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.RestoreVM`
- `version` (required): `1`
- `method` (required): `check_spec`
- `device_list` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `device_list`
- Error code 120 when parameter missing


#### Method: `check_support_tcmu`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.RestoreVM`
- `version` (required): `1`
- `method` (required): `check_support_tcmu`
- `_sid` (required): Session ID from login

**Response:**
```json
{
  "data": true,
  "success": true
}
```


#### Method: `check_vmm`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.RestoreVM`
- `version` (required): `1`
- `method` (required): `check_vmm`
- `_sid` (required): Session ID from login

**Response:**
```json
{
  "data": {
    "dsmSupported": true,
    "inCluster": false,
    "installed": false,
    "vmmBirthInfo": false,
    "vmmMigratable": false,
    "vmmSupported": false,
    "vmmTcmu": false,
    "volumeStatus": 2
  },
  "success": true
}
```


#### Method: `clone_enc_cmp_image`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.RestoreVM`
- `version` (required): `1`
- `method` (required): `clone_enc_cmp_image`
- `file_path` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `file_path`
- Error code 120 when parameter missing


#### Method: `create_image`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.RestoreVM`
- `version` (required): `1`
- `method` (required): `create_image`
- `task_id` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `task_id`
- Error code 120 when parameter missing


#### Method: `default_restore_name`


#### Method: `get_available_mem`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.RestoreVM`
- `version` (required): `1`
- `method` (required): `get_available_mem`
- `_sid` (required): Session ID from login

**Response:**
```json
{
  "data": {
    "avaiable_mb": 7675
  },
  "success": true
}
```


#### Method: `get_vmm_meta`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.RestoreVM`
- `version` (required): `1`
- `method` (required): `get_vmm_meta`
- `_sid` (required): Session ID from login

**Response:**
```json
{
  "success": true
}
```

**Notes:**
- May take longer to respond


#### Method: `job_check`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.RestoreVM`
- `version` (required): `1`
- `method` (required): `job_check`
- `_sid` (required): Session ID from login

**Response:**
```json
{
  "success": true
}
```


#### Method: `list_latest_version`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.RestoreVM`
- `version` (required): `1`
- `method` (required): `list_latest_version`
- `single_mode` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `single_mode`
- Error code 120 when parameter missing


#### Method: `list_spec`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.RestoreVM`
- `version` (required): `1`
- `method` (required): `list_spec`
- `device_list` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `device_list`
- Error code 120 when parameter missing


#### Method: `migrate`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.RestoreVM`
- `version` (required): `1`
- `method` (required): `migrate`
- `device_list` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `device_list`
- Error code 120 when parameter missing


#### Method: `remove_image`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.RestoreVM`
- `version` (required): `1`
- `method` (required): `remove_image`
- `task_id` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `task_id`
- Error code 120 when parameter missing


#### Method: `remove_vmm_meta`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.RestoreVM`
- `version` (required): `1`
- `method` (required): `remove_vmm_meta`
- `_sid` (required): Session ID from login

**Response:**
```json
{
  "success": true
}
```


#### Method: `restore`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.RestoreVM`
- `version` (required): `1`
- `method` (required): `restore`
- `device_list` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `device_list`
- Error code 120 when parameter missing


#### Method: `set_vmm_meta`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.RestoreVM`
- `version` (required): `1`
- `method` (required): `set_vmm_meta`
- `_sid` (required): Session ID from login

**Response:**
```json
{
  "success": true
}
```


#### Method: `status_image`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.RestoreVM`
- `version` (required): `1`
- `method` (required): `status_image`
- `serial_id` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `serial_id`
- Error code 120 when parameter missing


---
