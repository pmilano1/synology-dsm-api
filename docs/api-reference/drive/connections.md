# Synology Drive - Connections

**Category:** File Collaboration

[← Back to Synology Drive](README.md)

---

**Endpoint:** `/webapi/entry.cgi`

---

## SYNO.SynologyDrive.Connections

#### Method: `GetSummary`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.SynologyDrive.Connections`
- `version` (required): `1`
- `method` (required): `GetSummary`
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "total_connections": 25,
    "desktop_clients": 15,
    "mobile_clients": 8,
    "web_clients": 2
  }
}
```

---

#### Method: `List`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.SynologyDrive.Connections`
- `version` (required): `1`
- `method` (required): `List`
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "connections": [
      {
        "user": "john.doe",
        "client_type": "desktop",
        "client_version": "3.4.0",
        "ip_address": "192.168.1.100",
        "connected_time": 1732788000
      }
    ],
    "total": 1
  }
}
```

**Response Fields:**

| Field | Type | Description |
|-------|------|-------------|
| `user` | string | Username |
| `client_type` | string | Client type (`desktop`, `mobile`, `web`) |
| `client_version` | string | Client version |
| `ip_address` | string | Client IP address |
| `connected_time` | integer | Connection timestamp (Unix time) |

---

## SYNO.SynologyDrive.ShareSync

#### Method: `ListConnections`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.SynologyDrive.ShareSync`
- `version` (required): `1`
- `method` (required): `ListConnections`
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "connections": [
      {
        "user": "john.doe",
        "share_name": "Team Projects",
        "sync_status": "syncing",
        "files_synced": 150,
        "bytes_synced": 104857600
      }
    ],
    "total": 1
  }
}
```

**Sync Status:**
- `idle` - Not syncing
- `syncing` - Currently syncing
- `paused` - Sync paused
- `error` - Sync error

---

## SYNO.SynologyDrive.UserProfile

#### Method: `Get`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.SynologyDrive.UserProfile`
- `version` (required): `1`
- `method` (required): `Get`
- `user` (required): Username
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "user": "john.doe",
    "quota_used": 5368709120,
    "quota_total": 107374182400,
    "file_count": 500,
    "folder_count": 50,
    "last_sync_time": 1732788000
  }
}
```

**Notes:**
- User profiles track quota and usage
- Quotas can be set per user
- Sync profiles show last sync activity

