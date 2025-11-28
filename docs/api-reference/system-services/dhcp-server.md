# System Services - DHCP Server

**Category:** System Management

[← Back to System Services](README.md)

---

**Endpoint:** `/webapi/entry.cgi`

---

## SYNO.Core.Network.DHCPServer

#### Method: `Get`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.Core.Network.DHCPServer`
- `version` (required): `1`
- `method` (required): `Get`
- `ifname` (optional): Interface name (default: `ovs_eth0`)
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "enabled": true,
    "interface": "ovs_eth0",
    "start_ip": "192.168.1.100",
    "end_ip": "192.168.1.200",
    "netmask": "255.255.255.0",
    "gateway": "192.168.1.1",
    "dns_server": "192.168.1.1",
    "lease_time": 86400
  }
}
```

**Response Fields:**

| Field | Type | Description |
|-------|------|-------------|
| `enabled` | boolean | DHCP server enabled |
| `interface` | string | Network interface |
| `start_ip` | string | DHCP range start IP |
| `end_ip` | string | DHCP range end IP |
| `netmask` | string | Subnet mask |
| `gateway` | string | Default gateway |
| `dns_server` | string | DNS server |
| `lease_time` | integer | Lease time (seconds) |

---

## SYNO.Core.Network.DHCPServer.ClientList

#### Method: `List`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.Core.Network.DHCPServer.ClientList`
- `version` (required): `1`
- `method` (required): `List`
- `ifname` (optional): Interface name (default: `bond0`)
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "clients": [
      {
        "hostname": "laptop",
        "ip": "192.168.1.150",
        "mac": "00:11:22:33:44:55",
        "lease_time": 1732788000
      }
    ],
    "total": 1
  }
}
```

**Response Fields:**

| Field | Type | Description |
|-------|------|-------------|
| `hostname` | string | Client hostname |
| `ip` | string | Assigned IP address |
| `mac` | string | MAC address |
| `lease_time` | integer | Lease expiration (Unix time) |

---

## SYNO.Core.Network.DHCPServer.Reservation

#### Method: `List`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.Core.Network.DHCPServer.Reservation`
- `version` (required): `1`
- `method` (required): `List`
- `ifname` (optional): Interface name (default: `bond0`)
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "reservations": [
      {
        "hostname": "server",
        "ip": "192.168.1.50",
        "mac": "AA:BB:CC:DD:EE:FF"
      }
    ],
    "total": 1
  }
}
```

**Notes:**
- DHCP Server package must be installed
- Only one DHCP server per network interface
- Reservations ensure specific devices always get the same IP
- Common interface names: `ovs_eth0`, `bond0`, `eth0`

