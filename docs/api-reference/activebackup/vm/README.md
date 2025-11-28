# ActiveBackup - Virtual Machine APIs

**Category:** Data Protection

[← Back to ActiveBackup](../README.md)

---

**Endpoint:** `/webapi/entry.cgi`

---

## Overview

Virtual Machine APIs provide backup and restore capabilities for VMware and Hyper-V virtual machines with instant restore and application-aware backup support.

---

## API Categories

| Category | Description |
|----------|-------------|
| **[Inventory](inventory.md)** | VM discovery, inventory management |
| **[Restore VM](restorevm.md)** | VM restore operations, instant restore |

---

## Common Parameters

**Session Management:**
- `_sid` - Session ID (required for all APIs)

**Inventory Identification:**
- `inventory_id` - Hypervisor inventory ID

**VM Identification:**
- `vm_id` - Virtual machine ID
- `vm_uuid` - Virtual machine UUID

---

## Notes

- Supports VMware vSphere and Microsoft Hyper-V
- Instant restore allows VMs to run directly from backup storage
- Application-aware backup for Exchange, SQL Server in VMs
- Changed Block Tracking (CBT) for incremental backups
- Supports VM-level and disk-level restore

---

## See Also

- [Inventory](inventory.md)
- [Restore VM](restorevm.md)
