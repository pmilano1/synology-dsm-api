# Synology Drive - Status & Configuration

**Category:** File Collaboration

[← Back to Synology Drive](README.md)

---

**Endpoint:** `/webapi/entry.cgi`

---

## SYNO.SynologyDrive.Info

#### Method: `GetStatus`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.SynologyDrive.Info`
- `version` (required): `1`
- `method` (required): `GetStatus`
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "enabled": true,
    "version": "3.4.0-15724",
    "status": "running",
    "total_users": 50,
    "active_connections": 25
  }
}
```

**Response Fields:**

| Field | Type | Description |
|-------|------|-------------|
| `enabled` | boolean | Drive enabled |
| `version` | string | Drive version |
| `status` | string | Service status |
| `total_users` | integer | Total Drive users |
| `active_connections` | integer | Active connections |

---

#### Method: `GetConfig`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.SynologyDrive.Info`
- `version` (required): `1`
- `method` (required): `GetConfig`
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "max_file_size": 10737418240,
    "enable_versioning": true,
    "version_retention": 32,
    "enable_team_folder": true
  }
}
```

---

## SYNO.SynologyDrive.Settings

#### Method: `Get`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.SynologyDrive.Settings`
- `version` (required): `1`
- `method` (required): `Get`
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "enable_link_sharing": true,
    "enable_office_online": true,
    "enable_mobile_access": true,
    "max_upload_size": 10737418240
  }
}
```

---

## SYNO.SynologyDrive.DB

#### Method: `GetUsage`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.SynologyDrive.DB`
- `version` (required): `1`
- `method` (required): `GetUsage`
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "db_size": 524288000,
    "total_files": 15000,
    "total_folders": 2500,
    "total_versions": 45000
  }
}
```

**Response Fields:**

| Field | Type | Description |
|-------|------|-------------|
| `db_size` | integer | Database size (bytes) |
| `total_files` | integer | Total files tracked |
| `total_folders` | integer | Total folders tracked |
| `total_versions` | integer | Total file versions |

**Notes:**
- Database tracks all Drive files and versions
- Large databases may impact performance
- Regular cleanup recommended for old versions

