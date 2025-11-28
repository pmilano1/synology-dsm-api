# SYNO.ActiveBackup.Report

**Category:** System

[← Back to API Reference](../README.md)

---

**Endpoint:** `/webapi/entry.cgi`


#### Method: `create`


#### Method: `delete`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Report`
- `version` (required): `1`
- `method` (required): `delete`
- `report_ids` (required): Required parameter
- `_sid` (required): Session ID

**Notes:**
- Requires parameter: `report_ids`
- Error code 120 when parameter missing


#### Method: `list`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Report`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID

**Response:**
```json
{
  "data": {
    "reports": [],
    "total": 0
  },
  "success": true
}
```


---
