# System Services APIs

**Category:** System Management

[← Back to API Reference](../README.md)

---

**Endpoint:** `/webapi/entry.cgi`

---

## Overview

System Services APIs provide access to various DSM system services including DHCP server, Log Center, and Security Advisor.

---

## API Categories

| Category | Description |
|----------|-------------|
| **[DHCP Server](dhcp-server.md)** | DHCP server configuration, client list, reservations |
| **[Log Center](log-center.md)** | System logs, remote logging, log archives |
| **[Security Advisor](security-advisor.md)** | Security scans, checklist, login activity |

---

## Common Parameters

**Session Management:**
- `_sid` - Session ID (required for all APIs)

**Pagination:**
- `offset` - Starting index
- `limit` - Maximum results

---

## Error Codes

| Code | Description |
|------|-------------|
| 400 | Invalid parameter |
| 401 | Unknown error |
| 402 | Service not enabled |
| 403 | Permission denied |

---

## Notes

- DHCP Server package must be installed for DHCP APIs
- Log Center package must be installed for log APIs
- Security Advisor is built into DSM
- Administrator privileges required for most operations

