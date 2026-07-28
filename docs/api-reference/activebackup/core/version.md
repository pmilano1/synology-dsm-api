# SYNO.ActiveBackup.Version

**Category:** Core

[← Back to API Reference](../README.md)

---

**Endpoint:** `/webapi/entry.cgi`


#### Method: `delete`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Version`
- `version` (required): `1`
- `method` (required): `delete`
- `task_id` (required): Required parameter
- `_sid` (required): Session ID

**Notes:**
- Requires parameter: `task_id`
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
- `api` (required): `SYNO.ActiveBackup.Version`
- `version` (required): `1`
- `method` (required): `download`
- `device_id` (required): Required parameter
- `_sid` (required): Session ID

**Notes:**
- Requires parameter: `device_id`
- Error code 120 when parameter missing
- Supports file download

**Response:**
```json
{
  "success": true
}
```


#### Method: `list`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Version`
- `version` (required): `1`
- `method` (required): `list`
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


#### Method: `list_node`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Version`
- `version` (required): `1`
- `method` (required): `list_node`
- `device_id` (required): Required parameter
- `_sid` (required): Session ID

**Notes:**
- Requires parameter: `device_id`
- Error code 120 when parameter missing

**Response:**
```json
{
  "success": true,
  "data": {}
}
```


#### Method: `lock`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Version`
- `version` (required): `1`
- `method` (required): `lock`
- `task_id` (required): Required parameter
- `_sid` (required): Session ID

**Notes:**
- Requires parameter: `task_id`
- Error code 120 when parameter missing

**Response:**
```json
{
  "success": true
}
```


#### Method: `restore`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Version`
- `version` (required): `1`
- `method` (required): `restore`
- `device_id` (required): Required parameter
- `_sid` (required): Session ID

**Notes:**
- Requires parameter: `device_id`
- Error code 120 when parameter missing

**Response:**
```json
{
  "success": true
}
```


---
