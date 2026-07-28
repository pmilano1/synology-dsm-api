# FileStation - Upload & Download

**Category:** File Management

[← Back to FileStation](README.md)

---

**Endpoint:** `/webapi/entry.cgi`

---

## SYNO.FileStation.Upload

#### Method: `upload`

**HTTP Method:** POST (multipart/form-data)

**Parameters:**
- `api` (required): `SYNO.FileStation.Upload`
- `version` (required): `2`
- `method` (required): `upload`
- `path` (required): Destination folder path
- `file` (required): File data
- `_sid` (required): Session ID
- `create_parents` (optional): Create parent folders (default: true)
- `overwrite` (optional): Overwrite existing (default: false)
- `mtime` (optional): Modified time (Unix timestamp)
- `crtime` (optional): Create time (Unix timestamp)
- `atime` (optional): Access time (Unix timestamp)

**Response:**
```json
{
  "success": true
}
```

---

## SYNO.FileStation.Download

#### Method: `download`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.FileStation.Download`
- `version` (required): `2`
- `method` (required): `download`
- `path` (required): File path (JSON array for multiple - creates ZIP)
- `_sid` (required): Session ID
- `mode` (optional): `open` or `download`

**Response:**
```
Binary file data, or a ZIP archive for multiple files (no JSON envelope on success).
```

---

## SYNO.FileStation.CheckPermission

#### Method: `write`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.FileStation.CheckPermission`
- `version` (required): `3`
- `method` (required): `write`
- `path` (required): Destination folder path
- `filename` (required): Filename to check
- `_sid` (required): Session ID
- `overwrite` (optional): Check overwrite permission (default: false)
- `create_only` (optional): File must not exist (default: false)

**Response:**
```json
{
  "success": true,
  "data": {
    "result": true
  }
}
```

