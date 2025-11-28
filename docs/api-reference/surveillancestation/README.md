# Surveillance Station APIs

**Category:** Security & Surveillance

[← Back to API Reference](../README.md)

---

**Endpoint:** `/webapi/entry.cgi`

---

## Overview

Surveillance Station APIs provide comprehensive camera management, recording control, event monitoring, and live view access. This documentation covers the most commonly used APIs.

---

## API Categories

| Category | Description |
|----------|-------------|
| **[Info & Cameras](info-cameras.md)** | Station info, camera list, camera control (enable/disable) |
| **[Live View](live-view.md)** | Live camera streams, snapshots |
| **[PTZ Control](ptz-control.md)** | Pan/tilt/zoom camera control, presets, patrols |
| **[Recording](recording.md)** | Recording management, playback, download |
| **[Events](events.md)** | Event query, motion detection, event management |

---

## Common Parameters

**Session Management:**
- `_sid` - Session ID (required for all APIs)

**Camera Identification:**
- `cameraId` - Camera ID
- `idList` - Comma-separated camera IDs

**Pagination:**
- `offset` - Starting index
- `limit` - Maximum results

**Time Range:**
- `fromTime` - Start timestamp (Unix time)
- `toTime` - End timestamp (Unix time)

---

## Error Codes

| Code | Description |
|------|-------------|
| 400 | Invalid parameter |
| 401 | Unknown error |
| 402 | Surveillance Station not enabled |
| 403 | Permission denied |
| 404 | Camera not found |
| 405 | Camera offline |

---

## Notes

- Surveillance Station package must be installed
- Camera licenses required for each camera
- PTZ control requires PTZ-capable cameras
- Recording requires storage volume configured
- Live view streams use MJPEG or H.264 format

