# ActiveBackup - Core APIs

**Category:** Data Protection

[← Back to ActiveBackup](../README.md)

---

**Endpoint:** `/webapi/entry.cgi`

---

## Overview

Core ActiveBackup APIs provide fundamental device management, backup task control, restore operations, settings management, and version tracking.

---

## API Categories

| Category | Description |
|----------|-------------|
| **[Device Management](device.md)** | List, add, remove backup devices |
| **[Backup Tasks](task.md)** | Create, run, cancel backup tasks |
| **[Restore Operations](restore.md)** | Restore files, folders, and full systems |
| **[Settings](setting.md)** | Configure ActiveBackup settings |
| **[Versions](version.md)** | Manage backup versions and retention |

---

## Common Parameters

**Session Management:**
- `_sid` - Session ID (required for all APIs)

**Device Identification:**
- `device_id` - Device ID
- `device_uuid` - Device UUID

**Task Identification:**
- `task_id` - Backup task ID

**Version Identification:**
- `version_id` - Backup version ID

---

## Error Codes

| Code | Description |
|------|-------------|
| 400 | Invalid parameter |
| 401 | Unknown error |
| 402 | ActiveBackup not enabled |
| 403 | Permission denied |
| 404 | Device/task not found |
| 405 | Task already running |
| 406 | Insufficient storage space |

---

## See Also

- [Device Management](device.md)
- [Backup Tasks](task.md)
- [Restore Operations](restore.md)
- [Settings](setting.md)
- [Versions](version.md)
