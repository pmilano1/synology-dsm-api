# Docker - Volumes

**Category:** Container Management

[← Back to Docker](README.md)

---

**Endpoint:** `/webapi/entry.cgi`

---

## SYNO.Docker.Volume

#### Method: `list`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.Docker.Volume`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "volumes": [
      {
        "name": "nginx-data",
        "driver": "local",
        "mountpoint": "/volume1/@docker/volumes/nginx-data/_data",
        "scope": "local",
        "created": 1732752000
      }
    ]
  }
}
```

---

#### Method: `create`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Docker.Volume`
- `version` (required): `1`
- `method` (required): `create`
- `name` (required): Volume name
- `_sid` (required): Session ID
- `driver` (optional): Volume driver (default: `local`)

**Response:**
```json
{
  "success": true,
  "data": {
    "name": "nginx-data"
  }
}
```

---

#### Method: `delete`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Docker.Volume`
- `version` (required): `1`
- `method` (required): `delete`
- `name` (required): Volume name
- `_sid` (required): Session ID
- `force` (optional): Force delete (default: false)

**Response:**
```json
{
  "success": true
}
```

