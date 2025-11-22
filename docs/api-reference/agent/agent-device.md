# SYNO.ActiveBackup.Agent.Device

**Category:** Agent

[← Back to API Reference](../README.md)

---


**Endpoint:** `entry.cgi`
**Versions:** 1-2


#### Method: `duplicate_workload`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Agent.Device`
- `version` (required): `1`
- `method` (required): `duplicate_workload`
- `workload_uuid` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `workload_uuid`
- Error code 120 when parameter missing


#### Method: `list_nodes`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Agent.Device`
- `version` (required): `1`
- `method` (required): `list_nodes`
- `device_id` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `device_id`
- Error code 120 when parameter missing


#### Method: `set_update_policy`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Agent.Device`
- `version` (required): `1`
- `method` (required): `set_update_policy`
- `auto_update` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `auto_update`
- Error code 120 when parameter missing


#### Method: `update_agent`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Agent.Device`
- `version` (required): `1`
- `method` (required): `update_agent`
- `_sid` (required): Session ID from login

**Response:**
```json
{
  "success": true
}
```


#### Method: `upgrade`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Agent.Device`
- `version` (required): `1`
- `method` (required): `upgrade`
- `device_ids` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `device_ids`
- Error code 120 when parameter missing


---
