# SYNO.ActiveBackup.Agentless

**Category:** Agent

[← Back to API Reference](../README.md)

---


**Endpoint:** `entry.cgi`
**Versions:** 1-2


#### Method: `create_device`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Agentless`
- `version` (required): `1`
- `method` (required): `create_device`
- `remote_connection_info` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `remote_connection_info`
- Error code 120 when parameter missing


#### Method: `get_datapath_on_storage`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Agentless`
- `version` (required): `1`
- `method` (required): `get_datapath_on_storage`
- `share_name` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `share_name`
- Error code 120 when parameter missing


#### Method: `get_task_setting`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Agentless`
- `version` (required): `1`
- `method` (required): `get_task_setting`
- `task_id` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `task_id`
- Error code 120 when parameter missing


#### Method: `list_device_folder`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Agentless`
- `version` (required): `1`
- `method` (required): `list_device_folder`
- `remote_connection_info` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `remote_connection_info`
- Error code 120 when parameter missing


#### Method: `remove_ssh_key_tmp_file`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Agentless`
- `version` (required): `1`
- `method` (required): `remove_ssh_key_tmp_file`
- `ssh_key_file` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `ssh_key_file`
- Error code 120 when parameter missing


#### Method: `set_device`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Agentless`
- `version` (required): `1`
- `method` (required): `set_device`
- `remote_connection_info` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `remote_connection_info`
- Error code 120 when parameter missing


#### Method: `smb_list_remote_folder`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Agentless`
- `version` (required): `1`
- `method` (required): `smb_list_remote_folder`
- `host_ip` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `host_ip`
- Error code 120 when parameter missing


#### Method: `test_connection`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Agentless`
- `version` (required): `1`
- `method` (required): `test_connection`
- `remote_connection_info` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `remote_connection_info`
- Error code 120 when parameter missing


#### Method: `test_rsync_module_connection`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Agentless`
- `version` (required): `1`
- `method` (required): `test_rsync_module_connection`
- `remote_connection_info` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `remote_connection_info`
- Error code 120 when parameter missing


#### Method: `test_ssh_key`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Agentless`
- `version` (required): `1`
- `method` (required): `test_ssh_key`
- `ssh_key_file_path` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `ssh_key_file_path`
- Error code 120 when parameter missing


#### Method: `test_task_settings`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Agentless`
- `version` (required): `1`
- `method` (required): `test_task_settings`
- `_sid` (required): Session ID from login

**Response:**
```json
{
  "success": true
}
```


#### Method: `upload_ssh_key`


---
