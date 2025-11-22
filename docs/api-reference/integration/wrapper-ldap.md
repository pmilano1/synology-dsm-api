# SYNO.ActiveBackup.Wrapper.LDAP

**Category:** Integration

[← Back to API Reference](../README.md)

---


**Endpoint:** `entry.cgi`
**Versions:** 1-2


#### Method: `get`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Wrapper.LDAP`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from login

**Response:**
```json
{
  "data": {
    "base_dn": "",
    "enable_cifs": false,
    "enable_cifs_pam": false,
    "enable_client": false,
    "enable_client_certificate": false,
    "enable_idmap": false,
    "encryption": "no",
    "error": 2703,
    "host": "",
    "is_syno_server": false,
    "ldap_schema": "rfc2307",
    "nested_group_level": 0,
    "no_nested_group": false,
    "profile": "standard",
    "tls_reqcert": false,
    "update_min": 1440
  },
  "success": true
}
```


---
