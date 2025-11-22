# SYNO.ActiveBackup.UserGroup

**Category:** System

[← Back to API Reference](../README.md)

---


**Endpoint:** `entry.cgi`
**Versions:** 1-2


#### Method: `list`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.UserGroup`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID from login

**Response:**
```json
{
  "data": {
    "total": 3,
    "users_groups": [
      {
        "is_admin": true,
        "is_group": false,
        "name": "admin",
        "type": "local",
        "uid": 1024
      }
    ]
  },
  "success": true
}
```


#### Method: `list_admin`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.UserGroup`
- `version` (required): `1`
- `method` (required): `list_admin`
- `_sid` (required): Session ID from login

**Response:**
```json
{
  "data": {
    "groups": [
      {
        "is_admin": true,
        "is_group": true,
        "name": "administrators",
        "uid": 101
      }
    ],
    "users": [
      {
        "is_admin": true,
        "is_group": false,
        "name": "admin",
        "uid": 1024
      }
    ]
  },
  "success": true
}
```


---
