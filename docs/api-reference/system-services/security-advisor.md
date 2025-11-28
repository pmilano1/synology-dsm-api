# System Services - Security Advisor

**Category:** System Management

[← Back to System Services](README.md)

---

**Endpoint:** `/webapi/entry.cgi`

---

## SYNO.Core.SecurityScan.Conf

#### Method: `Get`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.Core.SecurityScan.Conf`
- `version` (required): `1`
- `method` (required): `Get`
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "scan_enabled": true,
    "auto_scan": true,
    "scan_schedule": "daily",
    "last_scan": 1732788000
  }
}
```

---

## SYNO.Core.SecurityScan.Status

#### Method: `CheckList`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.Core.SecurityScan.Status`
- `version` (required): `1`
- `method` (required): `CheckList`
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "items": [
      {
        "id": "firewall",
        "name": "Firewall",
        "status": "passed",
        "severity": "high"
      },
      {
        "id": "password_strength",
        "name": "Password Strength",
        "status": "warning",
        "severity": "medium"
      }
    ],
    "total_passed": 15,
    "total_warning": 3,
    "total_failed": 1
  }
}
```

**Response Fields:**

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Check item ID |
| `name` | string | Check item name |
| `status` | string | Status (`passed`, `warning`, `failed`) |
| `severity` | string | Severity level (`high`, `medium`, `low`) |

---

## SYNO.Core.SecurityScan.Operation

#### Method: `Scan`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.SecurityScan.Operation`
- `version` (required): `1`
- `method` (required): `Scan`
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "task_id": "scan_task_123"
  }
}
```

**Notes:**
- Scan is asynchronous (use task_id to monitor)
- Scan checks system security configuration
- Results include recommendations for improvements

---

## SYNO.Core.SecurityScan.LoginActivity

#### Method: `List`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.Core.SecurityScan.LoginActivity`
- `version` (required): `1`
- `method` (required): `List`
- `offset` (optional): Starting index (default: 0)
- `limit` (optional): Max results (default: 20)
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "activities": [
      {
        "time": 1732788000,
        "user": "admin",
        "ip": "192.168.1.100",
        "result": "success",
        "service": "DSM"
      }
    ],
    "total": 1
  }
}
```

**Response Fields:**

| Field | Type | Description |
|-------|------|-------------|
| `time` | integer | Login timestamp (Unix time) |
| `user` | string | Username |
| `ip` | string | Source IP address |
| `result` | string | Login result (`success`, `failed`) |
| `service` | string | Service name (`DSM`, `SSH`, `FTP`, etc.) |

**Notes:**
- Security Advisor is built into DSM
- Provides security recommendations
- Monitors login activity and failed attempts
- Checks for malware, weak passwords, outdated packages

