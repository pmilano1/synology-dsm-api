# System Services - Log Center

**Category:** System Management

[← Back to System Services](README.md)

---

**Endpoint:** `/webapi/entry.cgi`

---

## SYNO.Core.SyslogClient.Log

#### Method: `List`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.Core.SyslogClient.Log`
- `version` (required): `1`
- `method` (required): `List`
- `offset` (optional): Starting index (default: 0)
- `limit` (optional): Max results (default: 100)
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "logs": [
      {
        "time": 1732788000,
        "level": "info",
        "user": "admin",
        "event": "User logged in",
        "ip": "192.168.1.100"
      }
    ],
    "total": 1
  }
}
```

**Response Fields:**

| Field | Type | Description |
|-------|------|-------------|
| `time` | integer | Log timestamp (Unix time) |
| `level` | string | Log level (`info`, `warning`, `error`) |
| `user` | string | Username |
| `event` | string | Event description |
| `ip` | string | Source IP address |

---

## SYNO.Core.SyslogClient.Status

#### Method: `GetCount`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.Core.SyslogClient.Status`
- `version` (required): `1`
- `method` (required): `GetCount`
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "total_logs": 12345,
    "info_count": 10000,
    "warning_count": 2000,
    "error_count": 345
  }
}
```

---

#### Method: `GetEPS`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.Core.SyslogClient.Status`
- `version` (required): `1`
- `method` (required): `GetEPS`
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "events_per_second": 15.3,
    "peak_eps": 120.5
  }
}
```

**Notes:**
- EPS = Events Per Second
- Useful for monitoring log volume

---

## SYNO.Core.SyslogClient.Setting.Storage

#### Method: `List`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.Core.SyslogClient.Setting.Storage`
- `version` (required): `1`
- `method` (required): `List`
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "storage_path": "/volume1/logs",
    "max_size": 10737418240,
    "current_size": 5368709120,
    "rotation_enabled": true
  }
}
```

**Notes:**
- Log Center package must be installed
- Logs can be stored locally or sent to remote syslog server
- Log rotation prevents disk space exhaustion
- Supports filtering by time, level, user, event

