# SYNO.ActiveBackup.Restore

**Category:** Core

[← Back to API Reference](../README.md)

---

**Endpoint:** `/webapi/entry.cgi`


#### Method: `clear`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Restore`
- `version` (required): `1`
- `method` (required): `clear`
- `sessions` (required): Required parameter
- `_sid` (required): Session ID

**Notes:**
- Requires parameter: `sessions`
- Error code 120 when parameter missing

**Response:**
```json
{
  "success": true
}
```


#### Method: `list`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Restore`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID

**Response:**
```json
{
  "data": {
    "restore_infos": [],
    "total": 0
  },
  "success": true
}
```

**Notes:**
- May take longer to respond


#### Method: `pause`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Restore`
- `version` (required): `1`
- `method` (required): `pause`
- `job_ids` (required): Required parameter
- `_sid` (required): Session ID

**Notes:**
- Requires parameter: `job_ids`
- Error code 120 when parameter missing

**Response:**
```json
{
  "success": true
}
```


#### Method: `resume`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Restore`
- `version` (required): `1`
- `method` (required): `resume`
- `job_ids` (required): Required parameter
- `_sid` (required): Session ID

**Notes:**
- Requires parameter: `job_ids`
- Error code 120 when parameter missing

**Response:**
```json
{
  "success": true
}
```


#### Method: `status`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Restore`
- `version` (required): `1`
- `method` (required): `status`
- `job_id` (required): Required parameter
- `_sid` (required): Session ID

**Notes:**
- Requires parameter: `job_id`
- Error code 120 when parameter missing
- May take longer to respond

**Response:**
```json
{
  "success": true,
  "data": {}
}
```


#### Method: `stop`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Restore`
- `version` (required): `1`
- `method` (required): `stop`
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true
}
```


---
