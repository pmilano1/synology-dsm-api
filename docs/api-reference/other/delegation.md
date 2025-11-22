# SYNO.ActiveBackup.Delegation

**Category:** Other

[← Back to API Reference](../README.md)

---


**Endpoint:** `entry.cgi`
**Versions:** 1-2


#### Method: `create_or_update`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Delegation`
- `version` (required): `1`
- `method` (required): `create_or_update`
- `uids` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `uids`
- Error code 120 when parameter missing


#### Method: `delete`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Delegation`
- `version` (required): `1`
- `method` (required): `delete`
- `uids` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `uids`
- Error code 120 when parameter missing


#### Method: `list`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Delegation`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID from login

**Response:**
```json
{
  "data": {
    "total": 0,
    "users": []
  },
  "success": true
}
```


---
