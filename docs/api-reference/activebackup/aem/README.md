# ActiveBackup - Application-Aware Backup (AEM) APIs

**Category:** Data Protection

[← Back to ActiveBackup](../README.md)

---

**Endpoint:** `/webapi/entry.cgi`

---

## Overview

Application-Aware Backup (AEM) APIs provide application-consistent backup for Microsoft Exchange and SQL Server with granular restore capabilities.

---

## API Categories

| Category | Description |
|----------|-------------|
| **[AEM](aem.md)** | Application-aware backup management |
| **[Activity](aem-activity.md)** | AEM activity monitoring |
| **[Agent Installer](aem-agentinstaller.md)** | AEM agent installation |
| **[NFS](aem-nfs.md)** | NFS mount management for AEM |
| **[Script](aem-script.md)** | Pre/post backup scripts |
| **[Task](aem-task.md)** | AEM backup task management |
| **[Task Template](aem-tasktemplate.md)** | AEM task templates |
| **[Version](aem-version.md)** | AEM backup version management |

---

## Common Parameters

**Session Management:**
- `_sid` - Session ID (required for all APIs)

**Task Identification:**
- `task_id` - AEM backup task ID

**Version Identification:**
- `version_id` - AEM backup version ID

---

## Notes

- **AEM** = Application-Aware Backup for Exchange and SQL Server
- Provides application-consistent backups with transaction log support
- Supports granular restore (individual mailboxes, databases)
- Requires ActiveBackup Agent with AEM module installed
- Supports Exchange mailbox-level restore
- Supports SQL Server database-level restore
- Pre/post backup scripts for custom workflows

---

## See Also

- [AEM](aem.md)
- [Activity](aem-activity.md)
- [Agent Installer](aem-agentinstaller.md)
- [Task](aem-task.md)
- [Version](aem-version.md)
