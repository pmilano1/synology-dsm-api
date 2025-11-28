# ActiveBackup - Agent APIs

**Category:** Data Protection

[← Back to ActiveBackup](../README.md)

---

**Endpoint:** `/webapi/entry.cgi`

---

## Overview

Agent APIs provide backup capabilities for physical devices using either agent-based (with installed software) or agentless (using network protocols) approaches.

---

## API Categories

| Category | Description |
|----------|-------------|
| **[Agent](agent.md)** | Agent-based backup management |
| **[Agent Device](agent-device.md)** | Device management for agent-based backups |
| **[Agentless](agentless.md)** | Agentless backup using SMB/NFS |

---

## Common Parameters

**Session Management:**
- `_sid` - Session ID (required for all APIs)

**Device Identification:**
- `device_id` - Device ID
- `device_uuid` - Device UUID

---

## Notes

- **Agent-based backup** requires ActiveBackup Agent installed on target device
- **Agentless backup** uses SMB/NFS protocols without agent installation
- Agent-based provides application-aware backup (Exchange, SQL Server)
- Agentless is suitable for file-level backup only

---

## See Also

- [Agent](agent.md)
- [Agent Device](agent-device.md)
- [Agentless](agentless.md)
