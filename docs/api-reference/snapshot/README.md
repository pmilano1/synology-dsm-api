# Snapshot Replication APIs

**Category:** Storage Management

[← Back to API Reference](../README.md)

---

**Endpoint:** `/webapi/entry.cgi`

---

## Overview

Snapshot Replication APIs provide volume snapshot management, LUN snapshot management, and replication plan control for data protection and disaster recovery.

---

## API Categories

| Category | Description |
|----------|-------------|
| **[Volume Snapshots](volume-snapshots.md)** | Create, list, delete volume snapshots |
| **[LUN Snapshots](lun-snapshots.md)** | Create, list, delete LUN snapshots |
| **[Replication](replication.md)** | Replication plan management and synchronization |

---

## Common Parameters

**Session Management:**
- `_sid` - Session ID (required for all APIs)

**Snapshot Identification:**
- `share_name` - Shared folder name
- `snapshot_id` - Snapshot ID
- `lun_id` - LUN ID
- `snapshot_uuid` - Snapshot UUID

**Replication:**
- `plan_id` - Replication plan ID

---

## Error Codes

| Code | Description |
|------|-------------|
| 400 | Invalid parameter |
| 401 | Unknown error |
| 402 | Snapshot Replication not enabled |
| 403 | Permission denied |
| 404 | Snapshot not found |
| 405 | Insufficient storage space |

---

## Notes

- Snapshot Replication package must be installed
- Btrfs file system required for volume snapshots
- LUN snapshots require iSCSI Manager
- Snapshots consume storage space
- Replication requires source and destination NAS

