# SYNO.ActiveBackup.Wrapper.NFS

**Category:** Integration

[← Back to API Reference](../README.md)

---


**Endpoint:** `entry.cgi`
**Versions:** 1-2


#### Method: `get`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Wrapper.NFS`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from login

**Response:**
```json
{
  "data": {
    "enable_nfs": false,
    "enable_nfs_v4": false,
    "enabled_minor_ver": 0,
    "nfs_v4_domain": "",
    "read_size": 8192,
    "support_encrypt_share": 1,
    "support_major_ver": 4,
    "support_minor_ver": 1,
    "unix_pri_enable": true,
    "write_size": 8192
  },
  "success": true
}
```


#### Method: `set`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Wrapper.NFS`
- `version` (required): `1`
- `method` (required): `set`
- `enable_nfs` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `enable_nfs`
- Error code 120 when parameter missing


---
