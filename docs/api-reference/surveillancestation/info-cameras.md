# Surveillance Station - Info & Cameras

**Category:** Security & Surveillance

[← Back to Surveillance Station](README.md)

---

**Endpoint:** `/webapi/entry.cgi`

---

## SYNO.SurveillanceStation.Info

#### Method: `GetInfo`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.SurveillanceStation.Info`
- `version` (required): `1`
- `method` (required): `GetInfo`
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "version": "9.2.0-9289",
    "camera_number": 4,
    "license_number": 4,
    "recording_enabled": true
  }
}
```

---

## SYNO.SurveillanceStation.Camera

#### Method: `List`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.SurveillanceStation.Camera`
- `version` (required): `9`
- `method` (required): `List`
- `offset` (optional): Starting index (default: 0)
- `limit` (optional): Max results (default: 100)
- `blIncludeDeletedCam` (optional): Include deleted cameras (default: false)
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "cameras": [
      {
        "id": 1,
        "name": "Front Door",
        "model": "DS-2CD2142FWD-I",
        "vendor": "Hikvision",
        "ip": "192.168.1.100",
        "port": 80,
        "enabled": true,
        "status": 1,
        "recording_status": 1,
        "ptz_capable": false
      }
    ],
    "total": 1
  }
}
```

**Response Fields:**

| Field | Type | Description |
|-------|------|-------------|
| `id` | integer | Camera ID |
| `name` | string | Camera name |
| `model` | string | Camera model |
| `vendor` | string | Camera vendor |
| `ip` | string | Camera IP address |
| `port` | integer | Camera port |
| `enabled` | boolean | Camera enabled |
| `status` | integer | Camera status (1=normal, 2=disconnected) |
| `recording_status` | integer | Recording status (1=recording, 2=not recording) |
| `ptz_capable` | boolean | PTZ capability |

---

#### Method: `GetInfo`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.SurveillanceStation.Camera`
- `version` (required): `9`
- `method` (required): `GetInfo`
- `cameraIds` (required): Camera ID (comma-separated for multiple)
- `basic` (optional): Include basic info (default: true)
- `streamInfo` (optional): Include stream info (default: false)
- `optimize` (optional): Include optimization info (default: false)
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "cameras": [
      {
        "id": 1,
        "name": "Front Door",
        "enabled": true,
        "status": 1,
        "streams": [
          {
            "id": 0,
            "resolution": "1920x1080",
            "fps": 30,
            "quality": "high"
          }
        ]
      }
    ]
  }
}
```

---

#### Method: `Enable`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.SurveillanceStation.Camera`
- `version` (required): `9`
- `method` (required): `Enable`
- `idList` (required): Camera IDs (comma-separated)
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true
}
```

---

#### Method: `Disable`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.SurveillanceStation.Camera`
- `version` (required): `9`
- `method` (required): `Disable`
- `idList` (required): Camera IDs (comma-separated)
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true
}
```

**Notes:**
- Camera status: 1=normal, 2=disconnected, 3=unavailable
- Recording status: 1=recording, 2=not recording, 3=motion detection
- Enable/Disable affects camera recording and live view

