# ActiveBackup - System APIs

**Category:** Data Protection

[← Back to ActiveBackup](../README.md)

---

**Endpoint:** `/webapi/entry.cgi`

---

## Overview

System APIs provide ActiveBackup system management including activation, configuration, logging, reporting, storage management, and user permissions.

---

## API Categories

| Category | Description |
|----------|-------------|
| **[Activation](activation.md)** | License activation and management |
| **[General](general.md)** | General system settings |
| **[Log](log.md)** | Backup activity logs |
| **[Overview](overview.md)** | System overview and statistics |
| **[Plan](plan.md)** | Backup plan management |
| **[Report](report.md)** | Backup reports |
| **[Report Config](reportconfig.md)** | Report configuration |
| **[Share](share.md)** | Backup destination share management |
| **[Storage](storage.md)** | Storage usage and management |
| **[User Group](usergroup.md)** | User and group permissions |

---

## Common Parameters

**Session Management:**
- `_sid` - Session ID (required for all APIs)

---

## Notes

- Activation required for full functionality
- Logs provide detailed backup activity history
- Reports can be scheduled and emailed
- Storage management includes deduplication statistics
- User/group permissions control backup access

---

## See Also

- [Activation](activation.md)
- [Overview](overview.md)
- [Log](log.md)
- [Report](report.md)
- [Storage](storage.md)
