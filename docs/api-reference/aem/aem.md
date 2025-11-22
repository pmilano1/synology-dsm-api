# SYNO.ActiveBackup.AEM

**Category:** Aem

[← Back to API Reference](../README.md)

---


**Endpoint:** `entry.cgi`
**Versions:** 1-2


#### Method: `check_key`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.AEM`
- `version` (required): `1`
- `method` (required): `check_key`
- `key` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `key`
- Error code 120 when parameter missing


#### Method: `check_leader_address`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.AEM`
- `version` (required): `1`
- `method` (required): `check_leader_address`
- `leader_addr` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `leader_addr`
- Error code 120 when parameter missing


#### Method: `edit_connection`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.AEM`
- `version` (required): `1`
- `method` (required): `edit_connection`
- `hostname` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `hostname`
- Error code 120 when parameter missing


#### Method: `get_info`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.AEM`
- `version` (required): `1`
- `method` (required): `get_info`
- `_sid` (required): Session ID from login

**Response:**
```json
{
  "data": {
    "addr": "192.168.X.X",
    "role": 2,
    "status": 0
  },
  "success": true
}
```


#### Method: `get_join_state`


#### Method: `join`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.AEM`
- `version` (required): `1`
- `method` (required): `join`
- `key` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `key`
- Error code 120 when parameter missing


#### Method: `leave`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.AEM`
- `version` (required): `1`
- `method` (required): `leave`
- `_sid` (required): Session ID from login

**Response:**
```json
{
  "success": true
}
```


#### Method: `leave_by_leader`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.AEM`
- `version` (required): `1`
- `method` (required): `leave_by_leader`
- `_sid` (required): Session ID from login

**Response:**
```json
{
  "success": true
}
```


#### Method: `rebuild_version`


#### Method: `rebuild_workload`


---
