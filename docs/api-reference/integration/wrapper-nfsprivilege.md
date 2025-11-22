# SYNO.ActiveBackup.Wrapper.NFSPrivilege

**Category:** Integration

[← Back to API Reference](../README.md)

---


**Endpoint:** `entry.cgi`
**Versions:** 1-2


#### Method: `load`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Wrapper.NFSPrivilege`
- `version` (required): `1`
- `method` (required): `load`
- `share_name` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `share_name`
- Error code 120 when parameter missing


#### Method: `save`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Wrapper.NFSPrivilege`
- `version` (required): `1`
- `method` (required): `save`
- `share_name` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `share_name`
- Error code 120 when parameter missing

