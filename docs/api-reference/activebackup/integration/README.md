# ActiveBackup - Integration APIs

**Category:** Data Protection

[← Back to ActiveBackup](../README.md)

---

**Endpoint:** `/webapi/entry.cgi`

---

## Overview

Integration APIs provide wrappers for domain, LDAP, and NFS integration to support agentless backup and authentication.

---

## API Categories

| Category | Description |
|----------|-------------|
| **[Domain](wrapper-domain.md)** | Active Directory domain integration |
| **[LDAP](wrapper-ldap.md)** | LDAP authentication integration |
| **[NFS](wrapper-nfs.md)** | NFS mount management |
| **[NFS Privilege](wrapper-nfsprivilege.md)** | NFS permission management |

---

## Common Parameters

**Session Management:**
- `_sid` - Session ID (required for all APIs)

---

## Notes

- Domain/LDAP integration enables agentless backup authentication
- NFS integration supports file server backup
- Wrapper APIs provide abstraction layer for system services
- Required for agentless backup of domain-joined devices

---

## See Also

- [Domain](wrapper-domain.md)
- [LDAP](wrapper-ldap.md)
- [NFS](wrapper-nfs.md)
- [NFS Privilege](wrapper-nfsprivilege.md)
