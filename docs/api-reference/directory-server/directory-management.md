# Directory Server - Directory Management

**Category:** Identity Management

[← Back to Directory Server](README.md)

---

**Endpoint:** `/webapi/entry.cgi`

---

## SYNO.DirectoryServer.Domain

#### Method: `GetInfo`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.DirectoryServer.Domain`
- `version` (required): `1`
- `method` (required): `GetInfo`
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "domain": "example.com",
    "netbios_name": "EXAMPLE",
    "base_dn": "DC=example,DC=com",
    "status": "running"
  }
}
```

**Response Fields:**

| Field | Type | Description |
|-------|------|-------------|
| `domain` | string | Domain name |
| `netbios_name` | string | NetBIOS name |
| `base_dn` | string | Base Distinguished Name |
| `status` | string | Directory server status |

---

#### Method: `List`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.DirectoryServer.Domain`
- `version` (required): `1`
- `method` (required): `List`
- `basedn` (required): Base DN to search
- `offset` (optional): Starting index (default: 0)
- `limit` (optional): Max results (default: 100)
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "objects": [
      {
        "dn": "CN=John Doe,OU=Users,DC=example,DC=com",
        "cn": "John Doe",
        "objectClass": ["user", "person"],
        "mail": "john.doe@example.com"
      }
    ],
    "total": 1
  }
}
```

---

## SYNO.DirectoryServer.Sync

#### Method: `UpdateDomain`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.DirectoryServer.Sync`
- `version` (required): `1`
- `method` (required): `UpdateDomain`
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "task_id": "sync_12345"
  }
}
```

**Notes:**
- Synchronizes Synology users/groups with Directory Server
- Returns task ID for status monitoring
- Can take several minutes for large directories

---

#### Method: `GetTaskStatus`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.DirectoryServer.Sync`
- `version` (required): `1`
- `method` (required): `GetTaskStatus`
- `task_id` (required): Task ID from UpdateDomain
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "status": "running",
    "progress": 45,
    "users_synced": 150,
    "groups_synced": 25
  }
}
```

**Task Status:**
- `running` - Sync in progress
- `completed` - Sync completed successfully
- `failed` - Sync failed

**Notes:**
- Poll this endpoint to monitor sync progress
- Sync updates local DSM user/group database
- Changes from Directory Server are applied to DSM

