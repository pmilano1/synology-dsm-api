# SYNO.ActiveBackup.Inventory

**Category:** Vm

[← Back to API Reference](../README.md)

---


**Endpoint:** `entry.cgi`
**Versions:** 1-2


#### Method: `cancel_check_job`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Inventory`
- `version` (required): `1`
- `method` (required): `cancel_check_job`
- `session` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `session`
- Error code 120 when parameter missing


#### Method: `check_identity`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Inventory`
- `version` (required): `1`
- `method` (required): `check_identity`
- `inventory_id` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `inventory_id`
- Error code 120 when parameter missing


#### Method: `check_iscsi`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Inventory`
- `version` (required): `1`
- `method` (required): `check_iscsi`
- `inventory_id` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `inventory_id`
- Error code 120 when parameter missing


#### Method: `create`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Inventory`
- `version` (required): `1`
- `method` (required): `create`
- `host_name` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `host_name`
- Error code 120 when parameter missing


#### Method: `create_check_job`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Inventory`
- `version` (required): `1`
- `method` (required): `create_check_job`
- `session` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `session`
- Error code 120 when parameter missing


#### Method: `get_check_status`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Inventory`
- `version` (required): `1`
- `method` (required): `get_check_status`
- `session` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `session`
- Error code 120 when parameter missing
- May take longer to respond


#### Method: `get_host_interface`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Inventory`
- `version` (required): `1`
- `method` (required): `get_host_interface`
- `inventory_id` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `inventory_id`
- Error code 120 when parameter missing


#### Method: `get_node_infos`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Inventory`
- `version` (required): `1`
- `method` (required): `get_node_infos`
- `ids` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `ids`
- Error code 120 when parameter missing


#### Method: `get_node_path`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Inventory`
- `version` (required): `1`
- `method` (required): `get_node_path`
- `node_path_list` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `node_path_list`
- Error code 120 when parameter missing


#### Method: `get_server_cache`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Inventory`
- `version` (required): `1`
- `method` (required): `get_server_cache`
- `inventory_id` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `inventory_id`
- Error code 120 when parameter missing
- May take longer to respond


#### Method: `get_server_info`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Inventory`
- `version` (required): `1`
- `method` (required): `get_server_info`
- `inventory_id` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `inventory_id`
- Error code 120 when parameter missing
- May take longer to respond


#### Method: `list`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Inventory`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID from login

**Response:**
```json
{
  "data": [],
  "success": true
}
```

**Notes:**
- May take longer to respond


#### Method: `list_category_with_tag`


#### Method: `list_child`


#### Method: `list_cluster_shared_volume`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Inventory`
- `version` (required): `1`
- `method` (required): `list_cluster_shared_volume`
- `inventory_id` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `inventory_id`
- Error code 120 when parameter missing


#### Method: `list_guest_node`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Inventory`
- `version` (required): `1`
- `method` (required): `list_guest_node`
- `inventory_id` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `inventory_id`
- Error code 120 when parameter missing


#### Method: `list_node`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Inventory`
- `version` (required): `1`
- `method` (required): `list_node`
- `parent_id` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `parent_id`
- Error code 120 when parameter missing


#### Method: `merge_auto_backup_rule`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Inventory`
- `version` (required): `1`
- `method` (required): `merge_auto_backup_rule`
- `aem_uuid` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `aem_uuid`
- Error code 120 when parameter missing


#### Method: `remove`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Inventory`
- `version` (required): `1`
- `method` (required): `remove`
- `_sid` (required): Session ID from login

**Response:**
```json
{
  "success": true
}
```


#### Method: `test_connection`


#### Method: `update`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Inventory`
- `version` (required): `1`
- `method` (required): `update`
- `auth_user` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `auth_user`
- Error code 120 when parameter missing


#### Method: `update_cache`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Inventory`
- `version` (required): `1`
- `method` (required): `update_cache`
- `inventory_id` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `inventory_id`
- Error code 120 when parameter missing
- May take longer to respond


---
