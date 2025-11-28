# Surveillance Station - PTZ Control

**Category:** Security & Surveillance

[← Back to Surveillance Station](README.md)

---

**Endpoint:** `/webapi/entry.cgi`

---

## SYNO.SurveillanceStation.PTZ

#### Method: `Move`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.SurveillanceStation.PTZ`
- `version` (required): `5`
- `method` (required): `Move`
- `cameraId` (required): Camera ID
- `direction` (required): Direction (`up`, `down`, `left`, `right`, `home`, `stop`)
- `speed` (optional): Movement speed (1-5, default: 3)
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true
}
```

**Notes:**
- Direction values: `up`, `down`, `left`, `right`, `upleft`, `upright`, `downleft`, `downright`, `home`, `stop`
- Speed range: 1 (slowest) to 5 (fastest)
- `home` moves camera to home position
- `stop` stops current movement

---

#### Method: `Zoom`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.SurveillanceStation.PTZ`
- `version` (required): `5`
- `method` (required): `Zoom`
- `cameraId` (required): Camera ID
- `control` (required): Zoom control (`in`, `out`, `stop`)
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true
}
```

---

#### Method: `Focus`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.SurveillanceStation.PTZ`
- `version` (required): `5`
- `method` (required): `Focus`
- `cameraId` (required): Camera ID
- `control` (required): Focus control (`in`, `out`, `auto`, `stop`)
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true
}
```

---

## SYNO.SurveillanceStation.PTZ.Preset

#### Method: `List`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.SurveillanceStation.PTZ.Preset`
- `version` (required): `1`
- `method` (required): `List`
- `cameraId` (required): Camera ID
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "presets": [
      {
        "id": 1,
        "name": "Front Gate",
        "position": 1
      },
      {
        "id": 2,
        "name": "Parking Lot",
        "position": 2
      }
    ]
  }
}
```

---

#### Method: `GoPreset`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.SurveillanceStation.PTZ.Preset`
- `version` (required): `1`
- `method` (required): `GoPreset`
- `cameraId` (required): Camera ID
- `presetId` (optional): Preset ID
- `position` (optional): Preset position number
- `speed` (optional): Movement speed (1-5)
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true
}
```

**Notes:**
- Use either `presetId` or `position` parameter
- Presets must be configured in Surveillance Station first

---

## SYNO.SurveillanceStation.PTZ.Patrol

#### Method: `List`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.SurveillanceStation.PTZ.Patrol`
- `version` (required): `1`
- `method` (required): `List`
- `cameraId` (required): Camera ID
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "patrols": [
      {
        "id": 1,
        "name": "Perimeter Scan",
        "preset_count": 4
      }
    ]
  }
}
```

---

#### Method: `RunPatrol`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.SurveillanceStation.PTZ.Patrol`
- `version` (required): `1`
- `method` (required): `RunPatrol`
- `cameraId` (required): Camera ID
- `patrolId` (required): Patrol ID
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true
}
```

**Notes:**
- Patrols are sequences of preset positions
- Camera automatically moves through patrol points
- Patrol continues until stopped or interrupted

