# Synology Drive APIs

**Category:** File Collaboration

[← Back to API Reference](../README.md)

---

**Endpoint:** `/webapi/entry.cgi`

---

## Overview

Synology Drive APIs provide comprehensive file collaboration and synchronization management including connection monitoring, logs, and database usage.

---

## API Categories

| Category | Description |
|----------|-------------|
| **[Status & Configuration](status-config.md)** | Drive status, configuration, settings |
| **[Connections](connections.md)** | Active connections, sync connections, user profiles |
| **[Logs & Monitoring](logs-monitoring.md)** | Activity logs, database usage, deletion status |

---

## Common Parameters

**Session Management:**
- `_sid` - Session ID (required for all APIs)

**Filtering:**
- `share_type` - Share type filter (`all`, `team_folder`, `personal`)
- `offset` - Starting index
- `limit` - Max results

---

## Error Codes

| Code | Description |
|------|-------------|
| 400 | Invalid parameter |
| 401 | Unknown error |
| 402 | Drive not enabled |
| 403 | Permission denied |

---

## Notes

- Synology Drive package must be installed
- Requires administrator privileges for most APIs
- Drive supports file sync, sharing, and collaboration
- Team folders provide shared workspaces
- Personal folders are user-specific

