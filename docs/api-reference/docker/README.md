# Docker APIs

**Category:** Container Management

[← Back to API Reference](../README.md)

---

**Endpoint:** `/webapi/entry.cgi`

---

## API Categories

| Category | Description |
|----------|-------------|
| **[Containers](containers.md)** | Container management (list, start, stop, create, delete) |
| **[Images](images.md)** | Image management (list, pull, delete, search) |
| **[Networks](networks.md)** | Network management |
| **[Volumes](volumes.md)** | Volume management |

---

## Common Parameters

**Session Management:**
- `_sid` - Session ID (required for all APIs)

**Pagination:**
- `offset` - Starting index
- `limit` - Maximum results (default: -1 = all)

---

## Error Codes

| Code | Description |
|------|-------------|
| 400 | Invalid parameter |
| 401 | Unknown error |
| 402 | Docker not running |
| 403 | Permission denied |
| 404 | Container/image not found |
| 405 | Container already running |
| 406 | Container already stopped |

---

## Notes

- Docker package must be installed and running
- All APIs require authentication
- Container names must be unique
- Image tags follow Docker naming conventions

