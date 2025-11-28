# ActiveBackup - Additional APIs

**Category:** Data Protection

[← Back to ActiveBackup](../README.md)

---

**Endpoint:** `/webapi/entry.cgi`

---

## Overview

Additional ActiveBackup APIs for delegation, task templates, and workload management.

---

## API Categories

| Category | Description |
|----------|-------------|
| **[Delegation](delegation.md)** | Delegate backup management to users |
| **[Task Template](tasktemplate.md)** | Backup task templates |
| **[Workload](workload.md)** | Workload management and monitoring |

---

## Common Parameters

**Session Management:**
- `_sid` - Session ID (required for all APIs)

---

## Notes

- Delegation allows non-admin users to manage specific backups
- Task templates simplify creating similar backup tasks
- Workload management helps balance backup operations

---

## See Also

- [Delegation](delegation.md)
- [Task Template](tasktemplate.md)
- [Workload](workload.md)
