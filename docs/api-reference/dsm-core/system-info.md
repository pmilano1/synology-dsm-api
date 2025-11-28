# DSM Core - System Info

**Category:** System Management

[← Back to DSM Core](README.md)

---

**Endpoint:** `/webapi/entry.cgi`

---

## SYNO.Core.System

#### Method: `info`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.Core.System`
- `version` (required): `3`
- `method` (required): `info`
- `type` (optional): Info type (`storage`, `network`, `service`)
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "codepage": "enu",
    "model": "DS920+",
    "ram_size": 4096,
    "serial": "20C0SQN123456",
    "temperature": 42,
    "temperature_warn": false,
    "time": "Thu Nov 28 01:30:00 2024",
    "time_zone": "America/New_York",
    "time_zone_desc": "EST",
    "up_time": 86400,
    "usb_dev": [],
    "version": "7.2-64570",
    "version_string": "DSM 7.2-64570"
  }
}
```

---

## SYNO.Core.System.Utilization

#### Method: `get`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.Core.System.Utilization`
- `version` (required): `1`
- `method` (required): `get`
- `resource` (required): Resource type (`cpu`, `memory`, `disk`, `network`)
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "cpu": {
      "other_load": 5,
      "system_load": 10,
      "user_load": 15
    },
    "memory": {
      "real_usage": 2048,
      "si_disk": 0,
      "so_disk": 0,
      "swap_usage": 0
    },
    "disk": {
      "disk": [
        {
          "device": "sda",
          "display_name": "Drive 1",
          "read_access": 100,
          "type": "internal",
          "utilization": 50,
          "write_access": 50
        }
      ]
    },
    "network": [
      {
        "device": "eth0",
        "rx": 1048576,
        "tx": 524288
      }
    ]
  }
}
```

---

## SYNO.Core.System.SystemHealth

#### Method: `get`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.Core.System.SystemHealth`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "cpu_temperature": 42,
    "disk_temperature": [38, 40, 39, 41],
    "fan_status": "normal",
    "power_status": "normal",
    "system_status": "normal",
    "temperature_warning": false
  }
}
```

---

## SYNO.Core.FileServ.SMB

#### Method: `get`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.Core.FileServ.SMB`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "enable": true,
    "workgroup": "WORKGROUP",
    "wins_server": "",
    "local_master": true
  }
}
```

---

## SYNO.Core.FileServ.AFP

#### Method: `get`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.Core.FileServ.AFP`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "enable": true,
    "enable_bonjour": true
  }
}
```

---

## SYNO.Core.FileServ.NFS

#### Method: `get`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.Core.FileServ.NFS`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "enable": true,
    "enable_nfsv4": true
  }
}
```

