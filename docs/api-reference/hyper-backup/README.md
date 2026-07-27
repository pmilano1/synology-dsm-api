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
| **[Tasks](tasks.md)** | `SYNO.Backup.Task` — list / get / status / backup / cancel / suspend / resume / delete |
| **[Versions, Sources & Restore](versions.md)** | `SYNO.Backup.Version`, `Source.Folder`, `App2.Backup`, and the restore / file-browse (`Explore.*`) surface |
| **[Repositories & Targets](repositories.md)** | `SYNO.Backup.Repository` + `SYNO.Backup.Target` (destination record & live state) |
| **[Integrity](integrity.md)** | Integrity-check operations (`Target.error_detect`) |
| **[Vault](vault.md)** | Hyper Backup Vault (server / receiver side) |

> Methods are verified against a live NAS (DSM 7.x) by capturing the Hyper Backup UI's
> own requests, or marked *community-confirmed* from [`N4S4/synology-api`](https://github.com/N4S4/synology-api).
> The full endpoint list comes from `SYNO.API.Info?query=all` (54 `SYNO.Backup.*` APIs).

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

