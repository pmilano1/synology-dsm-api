# Docker - Containers

**Category:** Container Management

[← Back to Docker](README.md)

---

**Endpoint:** `/webapi/entry.cgi`

---

## SYNO.Docker.Container

#### Method: `list`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.Docker.Container`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID
- `offset` (optional): Starting index (default: 0)
- `limit` (optional): Max results (default: -1 = all)
- `type` (optional): Container type (`all`, `running`, `stopped`)

**Response:**
```json
{
  "success": true,
  "data": {
    "total": 10,
    "containers": [
      {
        "id": "abc123def456",
        "name": "nginx-proxy",
        "image": "nginxproxy/nginx-proxy:latest",
        "status": "running",
        "state": "running",
        "uptime": 86400,
        "cpu_usage": 5,
        "memory_usage": 104857600,
        "network_rx": 1048576,
        "network_tx": 524288
      }
    ]
  }
}
```

---

#### Method: `get`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.Docker.Container`
- `version` (required): `1`
- `method` (required): `get`
- `name` (required): Container name
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "container": {
      "id": "abc123def456",
      "name": "nginx-proxy",
      "image": "nginxproxy/nginx-proxy:latest",
      "status": "running",
      "ports": [
        {
          "container_port": 80,
          "host_port": 80,
          "type": "tcp"
        }
      ],
      "volumes": [
        {
          "host_path": "/volume1/docker/nginx-proxy",
          "container_path": "/etc/nginx"
        }
      ],
      "env": [
        "DEFAULT_HOST=example.com"
      ]
    }
  }
}
```

---

#### Method: `start`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Docker.Container`
- `version` (required): `1`
- `method` (required): `start`
- `name` (required): Container name
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
- `api` (required): `SYNO.Docker.Container`
- `version` (required): `1`
- `method` (required): `stop`
- `name` (required): Container name
- `_sid` (required): Session ID
- `timeout` (optional): Stop timeout in seconds (default: 10)

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
- `api` (required): `SYNO.Docker.Container`
- `version` (required): `1`
- `method` (required): `restart`
- `name` (required): Container name
- `_sid` (required): Session ID

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
- `api` (required): `SYNO.Docker.Container`
- `version` (required): `1`
- `method` (required): `delete`
- `name` (required): Container name (comma-separated for multiple)
- `_sid` (required): Session ID
- `force` (optional): Force delete (default: false)

**Response:**
```json
{
  "success": true
}
```

---

## SYNO.Docker.Container.Resource

#### Method: `get`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.Docker.Container.Resource`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "containers": [
      {
        "name": "nginx-proxy",
        "cpu_usage": 5,
        "memory_usage": 104857600,
        "memory_limit": 1073741824,
        "network_rx": 1048576,
        "network_tx": 524288
      }
    ]
  }
}
```

