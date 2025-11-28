# Surveillance Station - Recording

**Category:** Security & Surveillance

[← Back to Surveillance Station](README.md)

---

**Endpoint:** `/webapi/entry.cgi`

---

## SYNO.SurveillanceStation.Recording

#### Method: `Query`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.SurveillanceStation.Recording`
- `version` (required): `5`
- `method` (required): `Query`
- `cameraIds` (required): Camera IDs (comma-separated)
- `fromTime` (required): Start timestamp (Unix time)
- `toTime` (required): End timestamp (Unix time)
- `offset` (optional): Starting index (default: 0)
- `limit` (optional): Max results (default: 100)
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "recordings": [
      {
        "id": 12345,
        "camera_id": 1,
        "start_time": 1732752000,
        "end_time": 1732755600,
        "size": 104857600,
        "locked": false,
        "type": "continuous"
      }
    ],
    "total": 1
  }
}
```

**Response Fields:**

| Field | Type | Description |
|-------|------|-------------|
| `id` | integer | Recording ID |
| `camera_id` | integer | Camera ID |
| `start_time` | integer | Recording start time (Unix time) |
| `end_time` | integer | Recording end time (Unix time) |
| `size` | integer | Recording size (bytes) |
| `locked` | boolean | Recording locked (protected from deletion) |
| `type` | string | Recording type (`continuous`, `motion`, `manual`) |

---

#### Method: `Delete`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.SurveillanceStation.Recording`
- `version` (required): `5`
- `method` (required): `Delete`
- `idList` (required): Recording IDs (comma-separated)
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
- `api` (required): `SYNO.SurveillanceStation.Recording`
- `version` (required): `5`
- `method` (required): `Lock`
- `idList` (required): Recording IDs (comma-separated)
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
- `api` (required): `SYNO.SurveillanceStation.Recording`
- `version` (required): `5`
- `method` (required): `Unlock`
- `idList` (required): Recording IDs (comma-separated)
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true
}
```

---

#### Method: `Download`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.SurveillanceStation.Recording`
- `version` (required): `5`
- `method` (required): `Download`
- `id` (required): Recording ID
- `mountId` (optional): Mount ID (for external storage)
- `_sid` (required): Session ID

**Response:**
Binary video file data (MP4 format)

**Notes:**
- Response is a video file, not JSON
- Large recordings may take time to download
- Locked recordings cannot be deleted

---

## SYNO.SurveillanceStation.Recording.Export

#### Method: `Save`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.SurveillanceStation.Recording.Export`
- `version` (required): `2`
- `method` (required): `Save`
- `camId` (required): Camera ID
- `fromTime` (required): Start timestamp (Unix time)
- `toTime` (required): End timestamp (Unix time)
- `fileName` (optional): Export filename
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "task_id": "export_123"
  }
}
```

**Notes:**
- Creates an export task for downloading recordings
- Use task_id to check export progress
- Exported files are saved to designated folder

