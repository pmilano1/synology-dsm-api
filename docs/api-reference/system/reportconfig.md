# SYNO.ActiveBackup.ReportConfig

**Category:** System

[← Back to API Reference](../README.md)

---


**Endpoint:** `entry.cgi`
**Versions:** 1-2


#### Method: `get`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.ReportConfig`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from login

**Response:**
```json
{
  "data": {
    "configs": {
      "email": "",
      "interval": 1,
      "repeat_hour": 0,
      "repeat_type": "Weekly",
      "report_type": 1,
      "run_hour": 0,
      "run_min": 0,
      "run_weekday": [],
      "sched_id": 0,
      "schedule_setting_type": 0,
      "start_day": 0,
      "start_month": 0,
      "start_year": 0
    }
  },
  "success": true
}
```


#### Method: `set`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.ReportConfig`
- `version` (required): `1`
- `method` (required): `set`
- `_sid` (required): Session ID from login

**Response:**
```json
{
  "success": true
}
```


---
