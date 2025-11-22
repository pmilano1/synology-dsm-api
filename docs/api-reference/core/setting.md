# SYNO.ActiveBackup.Setting

**Category:** Core

[← Back to API Reference](../README.md)

---


**Endpoint:** `entry.cgi`
**Versions:** 1-2


#### Method: `get_phys_memsize`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Setting`
- `version` (required): `1`
- `method` (required): `get_phys_memsize`
- `_sid` (required): Session ID from login

**Response:**
```json
{
  "data": {
    "memory_size": 16777216
  },
  "success": true
}
```


#### Method: `list`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Setting`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID from login

**Response:**
```json
{
  "data": {
    "cert_info": {
      "cert_from_dsm": {
        "cert_common_name": "synology",
        "cert_issuer": "Synology Inc. CA",
        "cert_san": [
          "synology"
        ],
        "cert_tillTime": "Nov 20 03:17:39 2026 GMT"
      },
      "cert_from_package": {
        "cert_common_name": "Active Backup for Business",
        "cert_issuer": "Synology Active Backup for Business",
        "cert_san": [
          "Active Backup for Business"
        ],
        "cert_tillTime": 2079189993468
      },
      "cert_use_package": false
    },
    "settings": [
      {
        "id": 1,
        "name": "max_concurrent_devices",
        "value": "5"
      }
    ]
  },
  "success": true
}
```


#### Method: `renew_certificate`


#### Method: `set`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Setting`
- `version` (required): `1`
- `method` (required): `set`
- `settings` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `settings`
- Error code 120 when parameter missing


---
