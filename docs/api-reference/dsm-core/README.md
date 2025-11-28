# DSM Core APIs

**Category:** System Management

[← Back to API Reference](../README.md)

---

**Endpoint:** `/webapi/auth.cgi` (authentication) or `/webapi/entry.cgi` (other APIs)

---

## API Categories

| Category | Description |
|----------|-------------|
| **[Authentication](authentication.md)** | Login, logout, session management |
| **[System Info](system-info.md)** | System information, status, resources |
| **[Users](users.md)** | User management |
| **[Groups](groups.md)** | Group management |
| **[Packages](packages.md)** | Package/application management |
| **[Shares](shares.md)** | Shared folder management |
| **[Certificates](certificates.md)** | SSL certificate management |

---

## Common Parameters

**Session Management:**
- `_sid` - Session ID (required for authenticated APIs)
- `session` - Session name (e.g., `FileStation`, `DownloadStation`)

**Pagination:**
- `offset` - Starting index
- `limit` - Maximum results

---

## Error Codes

| Code | Description |
|------|-------------|
| 100 | Unknown error |
| 101 | Invalid parameter |
| 102 | API does not exist |
| 103 | Method does not exist |
| 104 | Not supported version |
| 105 | Permission denied |
| 106 | Session timeout |
| 107 | Multiple login detected |
| 400 | Invalid parameter |
| 401 | Unknown error |
| 402 | Invalid user or password |
| 403 | Permission denied |
| 404 | Failed to authenticate 2-factor authentication code |

---

## Notes

- All DSM Core APIs require authentication except login
- Session IDs expire after inactivity (default: 15 minutes)
- Use appropriate session names for different applications
- 2FA codes are required if enabled on the account

