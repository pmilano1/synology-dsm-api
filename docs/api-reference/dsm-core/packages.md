# DSM Core - Packages

**Category:** System Management

[← Back to DSM Core](README.md)

---

**Endpoint:** `/webapi/entry.cgi`

---

## SYNO.Core.Package

#### Method: `list`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.Core.Package`
- `version` (required): `2`
- `method` (required): `list`
- `_sid` (required): Session ID
- `additional` (optional): Additional fields (comma-separated): `description`, `dependent_packages`, `beta`, `distributor`, `maintainer`, `dsm_apps`, `install_type`, `autoupdate`

**Response:**
```json
{
  "success": true,
  "data": {
    "total": 15,
    "packages": [
      {
        "id": "Docker",
        "name": "Docker",
        "version": "20.10.23-1437",
        "status": "running",
        "description": "Docker container platform",
        "distributor": "Synology Inc.",
        "install_type": "package"
      }
    ]
  }
}
```

---

#### Method: `get`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.Core.Package`
- `version` (required): `2`
- `method` (required): `get`
- `id` (required): Package ID
- `_sid` (required): Session ID
- `additional` (optional): Additional fields

**Response:**
```json
{
  "success": true,
  "data": {
    "package": {
      "id": "Docker",
      "name": "Docker",
      "version": "20.10.23-1437",
      "status": "running",
      "description": "Docker container platform"
    }
  }
}
```

---

## SYNO.Core.Package.Server

#### Method: `list`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.Core.Package.Server`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "packages": [
      {
        "id": "ActiveBackup",
        "name": "Active Backup for Business",
        "version": "2.7.0-13164",
        "available_version": "2.7.1-13200",
        "category": "backup"
      }
    ]
  }
}
```

**Notes:**
- Lists packages available in Package Center
- Shows available updates

---

## SYNO.Core.Package.Installation

#### Method: `install`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Package.Installation`
- `version` (required): `1`
- `method` (required): `install`
- `id` (required): Package ID
- `_sid` (required): Session ID
- `volume` (optional): Installation volume path

**Response:**
```json
{
  "success": true,
  "data": {
    "task_id": "install_task_123"
  }
}
```

---

#### Method: `uninstall`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Package.Installation`
- `version` (required): `1`
- `method` (required): `uninstall`
- `id` (required): Package ID
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true
}
```

---

## SYNO.Core.Package.Control

#### Method: `start`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Package.Control`
- `version` (required): `1`
- `method` (required): `start`
- `id` (required): Package ID
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true
}
```

---

#### Method: `stop`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Package.Control`
- `version` (required): `1`
- `method` (required): `stop`
- `id` (required): Package ID
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true
}
```

---

#### Method: `restart`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Package.Control`
- `version` (required): `1`
- `method` (required): `restart`
- `id` (required): Package ID
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true
}
```

