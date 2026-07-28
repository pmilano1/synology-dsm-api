# VPN Server - Protocols

**Category:** Network Services

[← Back to VPN Server](README.md)

---

**Endpoint:** `/webapi/entry.cgi`

---

## SYNO.VPNCenter.Server.PPTP

#### Method: `load`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.VPNCenter.Server.PPTP`
- `version` (required): `1`
- `method` (required): `load`
- `serv_type` (required): `pptp`
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "enabled": true,
    "port": 1723,
    "max_connections": 10,
    "authentication": "mschap_v2",
    "encryption": "mppe_128"
  }
}
```

---

## SYNO.VPNCenter.Server.OpenVPN

#### Method: `load`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.VPNCenter.Server.OpenVPN`
- `version` (required): `1`
- `method` (required): `load`
- `serv_type` (required): `openvpn`
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "enabled": true,
    "port": 1194,
    "protocol": "udp",
    "max_connections": 20,
    "compression": true,
    "cipher": "AES-256-CBC"
  }
}
```

---

#### Method: `export_config`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.VPNCenter.Server.OpenVPN`
- `version` (required): `1`
- `method` (required): `export_config`
- `_sid` (required): Session ID

**Response:**
```
Binary ZIP archive containing the OpenVPN configuration files (no JSON envelope on success).
```

**Notes:**
- Response is a ZIP file, not JSON
- Contains `.ovpn` configuration file and certificates
- Can be imported directly into OpenVPN clients

---

## SYNO.VPNCenter.Server.L2TP

#### Method: `load`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.VPNCenter.Server.L2TP`
- `version` (required): `1`
- `method` (required): `load`
- `serv_type` (required): `l2tp`
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "enabled": false,
    "port": 1701,
    "max_connections": 10,
    "authentication": "mschap_v2",
    "ipsec_psk": "shared_secret_key"
  }
}
```

**Response Fields:**

| Field | Type | Description |
|-------|------|-------------|
| `enabled` | boolean | Protocol enabled |
| `port` | integer | Listening port |
| `max_connections` | integer | Maximum concurrent connections |
| `authentication` | string | Authentication method |
| `ipsec_psk` | string | IPsec pre-shared key (L2TP only) |
| `protocol` | string | Transport protocol (OpenVPN only) |
| `cipher` | string | Encryption cipher (OpenVPN only) |

**Notes:**
- PPTP is considered insecure, use OpenVPN or L2TP instead
- L2TP requires IPsec for encryption
- OpenVPN supports both TCP and UDP protocols

