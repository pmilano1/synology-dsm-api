# DSM Core - Groups

**Category:** System Management

[← Back to DSM Core](README.md)

---

**Endpoint:** `/webapi/entry.cgi`

---

## SYNO.Core.Group

#### Method: `list`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.Core.Group`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID
- `offset` (optional): Starting index (default: 0)
- `limit` (optional): Max results (default: -1 = all)
- `name_only` (optional): Return only names (default: false)

**Response:**
```json
{
  "success": true,
  "data": {
    "offset": 0,
    "total": 3,
    "groups": [
      {
        "name": "administrators",
        "gid": 101,
        "description": "System default admin group"
      },
      {
        "name": "users",
        "gid": 100,
        "description": "System default group"
      }
    ]
  }
}
```

---

#### Method: `get`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.Core.Group`
- `version` (required): `1`
- `method` (required): `get`
- `name` (required): Group name
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "group": {
      "name": "administrators",
      "gid": 101,
      "description": "System default admin group"
    }
  }
}
```

---

#### Method: `create`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Group`
- `version` (required): `1`
- `method` (required): `create`
- `name` (required): Group name
- `_sid` (required): Session ID
- `description` (optional): Group description

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
- `api` (required): `SYNO.Core.Group`
- `version` (required): `1`
- `method` (required): `set`
- `name` (required): Group name
- `_sid` (required): Session ID
- `new_name` (optional): New group name
- `description` (optional): Group description

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
- `api` (required): `SYNO.Core.Group`
- `version` (required): `1`
- `method` (required): `delete`
- `name` (required): Group name (comma-separated for multiple)
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true
}
```

---

## SYNO.Core.Group.Member

#### Method: `list`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.Core.Group.Member`
- `version` (required): `1`
- `method` (required): `list`
- `group` (required): Group name
- `_sid` (required): Session ID
- `in_group` (optional): List members (true) or non-members (false)

**Response:**
```json
{
  "success": true,
  "data": {
    "members": ["admin", "user1", "user2"]
  }
}
```

---

#### Method: `add`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Group.Member`
- `version` (required): `1`
- `method` (required): `add`
- `group` (required): Group name
- `users` (required): Usernames (comma-separated)
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true
}
```

---

#### Method: `remove`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Group.Member`
- `version` (required): `1`
- `method` (required): `remove`
- `group` (required): Group name
- `users` (required): Usernames (comma-separated)
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true
}
```

