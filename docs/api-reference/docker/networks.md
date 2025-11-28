# Docker - Networks

**Category:** Container Management

[← Back to Docker](README.md)

---

**Endpoint:** `/webapi/entry.cgi`

---

## SYNO.Docker.Network

#### Method: `list`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.Docker.Network`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "networks": [
      {
        "id": "abc123def456",
        "name": "bridge",
        "driver": "bridge",
        "scope": "local",
        "ipam": {
          "driver": "default",
          "config": [
            {
              "subnet": "172.17.0.0/16",
              "gateway": "172.17.0.1"
            }
          ]
        }
      }
    ]
  }
}
```

---

#### Method: `create`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Docker.Network`
- `version` (required): `1`
- `method` (required): `create`
- `name` (required): Network name
- `_sid` (required): Session ID
- `driver` (optional): Network driver (`bridge`, `host`, `overlay`, `macvlan`)
- `subnet` (optional): Subnet (e.g., `172.18.0.0/16`)
- `gateway` (optional): Gateway IP
- `ip_range` (optional): IP range

**Response:**
```json
{
  "success": true,
  "data": {
    "id": "network_id_123"
  }
}
```

---

#### Method: `delete`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Docker.Network`
- `version` (required): `1`
- `method` (required): `delete`
- `name` (required): Network name
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true
}
```

