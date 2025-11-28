# Hyper Backup APIs

**Category:** Data Protection

[← Back to API Reference](../README.md)

---

**Endpoint:** `/webapi/entry.cgi`

---

## Overview

Hyper Backup APIs provide comprehensive backup management including task control, repository management, integrity checks, and Hyper Backup Vault operations.

---

## API Categories

| Category | Description |
|----------|-------------|
| **[Tasks](tasks.md)** | Backup task management, run, cancel, suspend, resume |
| **[Repositories](repositories.md)** | Repository information and management |
| **[Integrity](integrity.md)** | Integrity check operations |
| **[Vault](vault.md)** | Hyper Backup Vault management |

---

## Common Parameters

**Session Management:**
- `_sid` - Session ID (required for all APIs)

**Task Identification:**
- `task_id` - Task ID

**Repository Identification:**
- `target_id` - Repository/target ID

---

## Error Codes

| Code | Description |
|------|-------------|
| 400 | Invalid parameter |
| 401 | Unknown error |
| 402 | Hyper Backup not enabled |
| 403 | Permission denied |
| 404 | Task/repository not found |
| 405 | Task already running |

---

## Notes

- Hyper Backup package must be installed
- Supports local, remote, and cloud backup destinations
- Versioning and deduplication supported
- Integrity checks verify backup data
- Vault provides centralized backup management

