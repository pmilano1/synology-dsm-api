# Directory Server APIs

**Category:** Identity Management

[← Back to API Reference](../README.md)

---

**Endpoint:** `/webapi/entry.cgi`

---

## Overview

Directory Server APIs provide comprehensive LDAP/Active Directory management including user and group management, password resets, and domain synchronization.

---

## API Categories

| Category | Description |
|----------|-------------|
| **[Directory Management](directory-management.md)** | Directory info, object listing, domain sync |
| **[User Management](user-management.md)** | Create, modify, delete users, password management |
| **[Group Management](group-management.md)** | Create, modify, delete groups, member management |

---

## Common Parameters

**Session Management:**
- `_sid` - Session ID (required for all APIs)

**Distinguished Names:**
- `dn` - Distinguished Name (e.g., `CN=John Doe,OU=Users,DC=example,DC=com`)
- `basedn` - Base Distinguished Name for searches

---

## Error Codes

| Code | Description |
|------|-------------|
| 400 | Invalid parameter |
| 401 | Unknown error |
| 403 | Permission denied |
| 404 | Object not found |
| 405 | Object already exists |

---

## Notes

- Directory Server package must be installed
- Requires administrator privileges
- Supports LDAP and Active Directory
- DN format follows LDAP standards
- Changes sync to connected domain controllers

