# Surveillance Station - Live View

**Category:** Security & Surveillance

[← Back to Surveillance Station](README.md)

---

**Endpoint:** `/webapi/entry.cgi`

---

## SYNO.SurveillanceStation.Camera

#### Method: `GetSnapshot`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.SurveillanceStation.Camera`
- `version` (required): `9`
- `method` (required): `GetSnapshot`
- `id` (optional): Camera ID
- `name` (optional): Camera name (alternative to ID)
- `profileType` (optional): Profile type (0=high quality, 1=balanced, 2=low bandwidth, default: 1)
- `_sid` (required): Session ID

**Response:**
Binary JPEG image data

**Notes:**
- Response is a JPEG image, not JSON
- Use either `id` or `name` parameter
- Profile type affects image quality and size

---

#### Method: `GetLiveViewPath`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.SurveillanceStation.Camera`
- `version` (required): `9`
- `method` (required): `GetLiveViewPath`
- `idList` (required): Camera IDs (comma-separated)
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "cameras": [
      {
        "id": 1,
        "mjpeg_path": "/webapi/entry.cgi?api=SYNO.SurveillanceStation.VideoStream&version=1&method=Stream&cameraId=1&format=mjpeg",
        "rtsp_path": "rtsp://192.168.1.1:554/live/1",
        "multicast_path": ""
      }
    ]
  }
}
```

**Response Fields:**

| Field | Type | Description |
|-------|------|-------------|
| `id` | integer | Camera ID |
| `mjpeg_path` | string | MJPEG stream path |
| `rtsp_path` | string | RTSP stream URL |
| `multicast_path` | string | Multicast stream path (if enabled) |

---

## SYNO.SurveillanceStation.VideoStream

#### Method: `Stream`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.SurveillanceStation.VideoStream`
- `version` (required): `1`
- `method` (required): `Stream`
- `cameraId` (required): Camera ID
- `format` (required): Stream format (`mjpeg`, `multipart`)
- `_sid` (required): Session ID

**Response:**
Binary video stream data (MJPEG format)

**Notes:**
- Response is a continuous MJPEG stream
- Use `multipart` format for HTTP multipart stream
- Stream continues until connection is closed

---

## SYNO.SurveillanceStation.Camera.Group

#### Method: `Enum`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.SurveillanceStation.Camera.Group`
- `version` (required): `1`
- `method` (required): `Enum`
- `privCamType` (optional): Camera type filter (default: 1)
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "groups": [
      {
        "id": 1,
        "name": "Front Cameras",
        "camera_ids": [1, 2, 3]
      },
      {
        "id": 2,
        "name": "Back Cameras",
        "camera_ids": [4, 5]
      }
    ]
  }
}
```

**Notes:**
- Camera groups organize cameras for easier management
- Groups can be used for batch operations
- Live view can display multiple cameras from a group

