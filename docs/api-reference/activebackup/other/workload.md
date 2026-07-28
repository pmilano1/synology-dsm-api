# SYNO.ActiveBackup.Workload

**Category:** Other

[← Back to API Reference](../README.md)

---

**Endpoint:** `/webapi/entry.cgi`


#### Method: `backup`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Workload`
- `version` (required): `1`
- `method` (required): `backup`
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true
}
```


#### Method: `cancel`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Workload`
- `version` (required): `1`
- `method` (required): `cancel`
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true
}
```


#### Method: `cancel_by_activity_uid`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Workload`
- `version` (required): `1`
- `method` (required): `cancel_by_activity_uid`
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true
}
```


#### Method: `cancel_then_delete`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Workload`
- `version` (required): `1`
- `method` (required): `cancel_then_delete`
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true
}
```


#### Method: `create`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Workload`
- `version` (required): `1`
- `method` (required): `create`
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true
}
```


#### Method: `delete`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Workload`
- `version` (required): `1`
- `method` (required): `delete`
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true
}
```


#### Method: `delete_without_dedup`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Workload`
- `version` (required): `1`
- `method` (required): `delete_without_dedup`
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true
}
```


#### Method: `get_plan`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Workload`
- `version` (required): `1`
- `method` (required): `get_plan`
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {}
}
```


#### Method: `get_status`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Workload`
- `version` (required): `1`
- `method` (required): `get_status`
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {}
}
```


#### Method: `update`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Workload`
- `version` (required): `1`
- `method` (required): `update`
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true
}
```


---
