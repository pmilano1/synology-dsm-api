# Docker - Images

**Category:** Container Management

[← Back to Docker](README.md)

---

**Endpoint:** `/webapi/entry.cgi`

---

## SYNO.Docker.Image

#### Method: `list`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.Docker.Image`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID
- `offset` (optional): Starting index (default: 0)
- `limit` (optional): Max results (default: -1 = all)
- `show_dsm` (optional): Show DSM images (default: false)

**Response:**
```json
{
  "success": true,
  "data": {
    "total": 25,
    "images": [
      {
        "id": "sha256:abc123def456",
        "repository": "nginxproxy/nginx-proxy",
        "tag": "latest",
        "size": 157286400,
        "created": 1732752000,
        "is_ddsm": false
      }
    ]
  }
}
```

---

#### Method: `get`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.Docker.Image`
- `version` (required): `1`
- `method` (required): `get`
- `repository` (required): Image repository
- `tag` (required): Image tag
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "image": {
      "id": "sha256:abc123def456",
      "repository": "nginxproxy/nginx-proxy",
      "tag": "latest",
      "size": 157286400,
      "created": 1732752000
    }
  }
}
```

---

#### Method: `pull`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Docker.Image`
- `version` (required): `1`
- `method` (required): `pull`
- `repository` (required): Image repository
- `tag` (optional): Image tag (default: `latest`)
- `_sid` (required): Session ID
- `registry` (optional): Registry URL

**Response:**
```json
{
  "success": true,
  "data": {
    "task_id": "pull_task_123"
  }
}
```

---

#### Method: `delete`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Docker.Image`
- `version` (required): `1`
- `method` (required): `delete`
- `repository` (required): Image repository
- `tag` (required): Image tag
- `_sid` (required): Session ID
- `force` (optional): Force delete (default: false)

**Response:**
```json
{
  "success": true
}
```

---

## SYNO.Docker.Image.Search

#### Method: `search`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.Docker.Image.Search`
- `version` (required): `1`
- `method` (required): `search`
- `query` (required): Search query
- `_sid` (required): Session ID
- `registry` (optional): Registry to search

**Response:**
```json
{
  "success": true,
  "data": {
    "images": [
      {
        "name": "nginx",
        "description": "Official build of Nginx",
        "star_count": 15000,
        "is_official": true,
        "is_automated": false
      }
    ]
  }
}
```

---

## SYNO.Docker.Image.Registry

#### Method: `list`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.Docker.Image.Registry`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "registries": [
      {
        "name": "Docker Hub",
        "url": "https://registry-1.docker.io",
        "is_default": true
      },
      {
        "name": "GitHub Container Registry",
        "url": "https://ghcr.io",
        "is_default": false
      }
    ]
  }
}
```

---

#### Method: `add`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Docker.Image.Registry`
- `version` (required): `1`
- `method` (required): `add`
- `name` (required): Registry name
- `url` (required): Registry URL
- `_sid` (required): Session ID
- `username` (optional): Registry username
- `password` (optional): Registry password

**Response:**
```json
{
  "success": true
}
```

