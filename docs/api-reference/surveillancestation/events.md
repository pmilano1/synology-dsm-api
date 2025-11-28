# Surveillance Station - Events

**Category:** Security & Surveillance

[← Back to Surveillance Station](README.md)

---

**Endpoint:** `/webapi/entry.cgi`

---

## SYNO.SurveillanceStation.Event

#### Method: `Query`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.SurveillanceStation.Event`
- `version` (required): `4`
- `method` (required): `Query`
- `offset` (optional): Starting index (default: 0)
- `limit` (optional): Max results (default: 100)
- `cameraIds` (optional): Camera IDs (comma-separated)
- `fromTime` (optional): Start timestamp (Unix time)
- `toTime` (optional): End timestamp (Unix time)
- `reason` (optional): Event reason filter (comma-separated)
- `locked` (optional): Locked status (0=unlocked, 1=locked)
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "events": [
      {
        "id": 54321,
        "camera_id": 1,
        "camera_name": "Front Door",
        "time": 1732752000,
        "reason": "motion",
        "locked": false,
        "has_snapshot": true
      }
    ],
    "total": 1
  }
}
```

**Response Fields:**

| Field | Type | Description |
|-------|------|-------------|
| `id` | integer | Event ID |
| `camera_id` | integer | Camera ID |
| `camera_name` | string | Camera name |
| `time` | integer | Event timestamp (Unix time) |
| `reason` | string | Event reason (motion, manual, alarm, etc.) |
| `locked` | boolean | Event locked (protected from deletion) |
| `has_snapshot` | boolean | Snapshot available |

---

#### Method: `Delete`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.SurveillanceStation.Event`
- `version` (required): `4`
- `method` (required): `Delete`
- `reason` (optional): Event reason filter
- `cameraIds` (optional): Camera IDs (comma-separated)
- `fromTime` (optional): Start timestamp
- `toTime` (optional): End timestamp
- `locked` (optional): Locked status filter
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true
}
```

---

#### Method: `Lock`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.SurveillanceStation.Event`
- `version` (required): `4`
- `method` (required): `Lock`
- `reason` (optional): Event reason filter
- `cameraIds` (optional): Camera IDs (comma-separated)
- `fromTime` (optional): Start timestamp
- `toTime` (optional): End timestamp
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true
}
```

---

#### Method: `Unlock`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.SurveillanceStation.Event`
- `version` (required): `4`
- `method` (required): `Unlock`
- `idList` (required): Event IDs (comma-separated)
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true
}
```

---

## SYNO.SurveillanceStation.Event.Detection

#### Method: `MotionEnum`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.SurveillanceStation.Event.Detection`
- `version` (required): `1`
- `method` (required): `MotionEnum`
- `camId` (required): Camera ID
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "motion_detection": {
      "enabled": true,
      "sensitivity": 80,
      "threshold": 10,
      "object_size": 5
    }
  }
}
```

**Notes:**
- Event reasons: `motion`, `manual`, `alarm`, `continuous`
- Locked events cannot be deleted
- Motion detection settings are camera-specific
- Events can be filtered by multiple criteria

