# SYNO.ActiveBackup.Activation

**Category:** System

[← Back to API Reference](../README.md)

---


**Endpoint:** `entry.cgi`
**Versions:** 1-2


#### Method: `get`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Activation`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from login

**Response:**
```json
{
  "data": {
    "activated": true,
    "serial_number": "SERIAL_NUMBER"
  },
  "success": true
}
```


#### Method: `set`


---
