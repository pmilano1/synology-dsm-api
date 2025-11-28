# ActiveBackup for Business APIs

**Category:** Data Protection

[← Back to API Reference](../README.md)

---

**Endpoint:** `/webapi/entry.cgi`

---

## Overview

ActiveBackup for Business APIs provide comprehensive backup and restore capabilities for physical devices, virtual machines, and file servers with versioning, deduplication, and application-aware backups.

---

## API Categories

| Category | Description |
|----------|-------------|
| **[Core](core/)** | Device management, backup tasks, restore operations, settings, versions |
| **[Agent](agent/)** | Agent-based device backup, agentless backup |
| **[Virtual Machines](vm/)** | VM inventory, VM restore operations |
| **[Application-Aware Backup (AEM)](aem/)** | Exchange, SQL Server application-aware backups |
| **[System](system/)** | Activation, overview, logs, reports, storage, plans, shares |
| **[Integration](integration/)** | Domain, LDAP, NFS integration |
| **[Other](other/)** | Delegation, task templates, workload management |

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

## Notes

- ActiveBackup for Business package must be installed
- Supports Windows, Linux, macOS physical devices
- Supports VMware, Hyper-V virtual machines
- Application-aware backup for Exchange, SQL Server
- Versioning and deduplication reduce storage usage
- Instant restore for VMs
- File-level and bare-metal restore for physical devices

