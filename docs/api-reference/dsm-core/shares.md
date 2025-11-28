# DSM Core - Shares

**Category:** System Management

[← Back to DSM Core](README.md)

---

**Endpoint:** `/webapi/entry.cgi`

---

## SYNO.Core.Share

#### Method: `list`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.Core.Share`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID
- `share_type` (optional): Share type (`all`, `user`, `system`)
- `additional` (optional): Additional fields (comma-separated): `hidden`, `encryption`, `is_aclmode`, `recyclebin`, `share_quota`, `enable_share_compress`, `enable_share_cow`

**Response:**
```json
{
  "success": true,
  "data": {
    "total": 5,
    "shares": [
      {
        "name": "docker",
        "path": "/volume1/docker",
        "vol_path": "/volume1",
        "description": "Docker shared folder",
        "encryption": false,
        "hidden": false,
        "recyclebin": true,
        "share_quota": 0
      }
    ]
  }
}
```

---

#### Method: `get`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.Core.Share`
- `version` (required): `1`
- `method` (required): `get`
- `name` (required): Share name
- `_sid` (required): Session ID
- `additional` (optional): Additional fields

**Response:**
```json
{
  "success": true,
  "data": {
    "share": {
      "name": "docker",
      "path": "/volume1/docker",
      "vol_path": "/volume1",
      "description": "Docker shared folder"
    }
  }
}
```

---

#### Method: `create`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Share`
- `version` (required): `1`
- `method` (required): `create`
- `name` (required): Share name
- `vol_path` (required): Volume path (e.g., `/volume1`)
- `_sid` (required): Session ID
- `desc` (optional): Description
- `encryption` (optional): Enable encryption (default: false)
- `enable_share_compress` (optional): Enable compression (default: false)
- `enable_share_cow` (optional): Enable Btrfs COW (default: false)
- `recyclebin` (optional): Enable recycle bin (default: false)

**Response:**
```json
{
  "success": true
}
```

---

#### Method: `set`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Share`
- `version` (required): `1`
- `method` (required): `set`
- `name` (required): Share name
- `_sid` (required): Session ID
- `desc` (optional): Description
- `recyclebin` (optional): Enable recycle bin
- `enable_share_compress` (optional): Enable compression
- `enable_share_cow` (optional): Enable Btrfs COW

**Response:**
```json
{
  "success": true
}
```

---

#### Method: `delete`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Share`
- `version` (required): `1`
- `method` (required): `delete`
- `name` (required): Share name (comma-separated for multiple)
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true
}
```

---

## SYNO.Core.Share.Permission

#### Method: `get`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.Core.Share.Permission`
- `version` (required): `1`
- `method` (required): `get`
- `name` (required): Share name
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "permissions": [
      {
        "name": "admin",
        "is_group": false,
        "permission": "RW"
      },
      {
        "name": "users",
        "is_group": true,
        "permission": "RO"
      }
    ]
  }
}
```

---

#### Method: `set`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Share.Permission`
- `version` (required): `1`
- `method` (required): `set`
- `name` (required): Share name
- `_sid` (required): Session ID
- `permissions` (required): JSON array of permissions

**Notes:**
- Permission values: `RW` (read/write), `RO` (read-only), `NA` (no access)

**Response:**
```json
{
  "success": true
}
```

