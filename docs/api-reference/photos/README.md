# Photos APIs

**Category:** Media Management

[← Back to API Reference](../README.md)

---

**Endpoint:** `/webapi/entry.cgi`

---

## API Categories

| Category | Description |
|----------|-------------|
| **[Folders](folders.md)** | Folder browsing and management |
| **[Albums](albums.md)** | Album creation and management |
| **[Items](items.md)** | Photo and video item management |
| **[Sharing](sharing.md)** | Share albums and folders |

---

## Common Parameters

**Session Management:**
- `_sid` - Session ID (required for all APIs)

**Pagination:**
- `offset` - Starting index
- `limit` - Maximum results

**Additional Fields:**
- `thumbnail` - Include thumbnail info
- `resolution` - Include resolution info
- `orientation` - Include orientation info
- `video_convert` - Include video conversion info
- `video_meta` - Include video metadata

---

## Error Codes

| Code | Description |
|------|-------------|
| 400 | Invalid parameter |
| 401 | Unknown error |
| 402 | Photos not enabled |
| 403 | Permission denied |
| 404 | Item/folder/album not found |

---

## Notes

- Synology Photos package must be installed
- Personal Space and Team Space are separate
- Album conditions use JSON format
- Sharing requires appropriate permissions

