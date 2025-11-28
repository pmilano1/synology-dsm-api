# SYNO.ActiveBackup.Delegation

**Category:** Other

[← Back to API Reference](../README.md)

---

**Endpoint:** `/webapi/entry.cgi`


#### Method: `create_or_update`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Delegation`
- `version` (required): `1`
- `method` (required): `create_or_update`
- `uids` (required): Required parameter
- `_sid` (required): Session ID

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
- `_sid` (required): Session ID

**Notes:**
- Requires parameter: `uids`
- Error code 120 when parameter missing


#### Method: `list`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Delegation`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID

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
