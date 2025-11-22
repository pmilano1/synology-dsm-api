# SYNO.ActiveBackup.Wrapper.Domain

**Category:** Integration

[← Back to API Reference](../README.md)

---


**Endpoint:** `entry.cgi`
**Versions:** 1-2


#### Method: `get`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Wrapper.Domain`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from login

**Response:**
```json
{
  "data": {
    "enable_domain": false
  },
  "success": true
}
```


#### Method: `get_domain_list`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Wrapper.Domain`
- `version` (required): `1`
- `method` (required): `get_domain_list`
- `_sid` (required): Session ID from login

**Response:**
```json
{
  "data": {
    "domain_list": []
  },
  "success": true
}
```


#### Method: `test_dc`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Wrapper.Domain`
- `version` (required): `1`
- `method` (required): `test_dc`
- `_sid` (required): Session ID from login

**Response:**
```json
{
  "data": {
    "test_join_success": false
  },
  "success": true
}
```


---
