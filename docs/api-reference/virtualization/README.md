# Virtual Machine Manager APIs

**Category:** Virtualization

[← Back to API Reference](../README.md)

---

**Endpoint:** `/webapi/entry.cgi`

---

## Overview

Virtual Machine Manager APIs provide comprehensive VM lifecycle management, including creation, power control, configuration, and image management.

---

## API Categories

| Category | Description |
|----------|-------------|
| **[Virtual Machines](virtual-machines.md)** | VM listing, info, power control, configuration |
| **[Images](images.md)** | VM image management and creation |
| **[Tasks](tasks.md)** | Task monitoring and management |

---

## Common Parameters

**Session Management:**
- `_sid` - Session ID (required for all APIs)

**VM Identification:**
- `guest_id` - Virtual machine ID
- `guest_name` - Virtual machine name

**Image Identification:**
- `image_id` - VM image ID
- `image_name` - VM image name

---

## Error Codes

| Code | Description |
|------|-------------|
| 400 | Invalid parameter |
| 401 | Unknown error |
| 402 | Virtual Machine Manager not enabled |
| 403 | Permission denied |
| 404 | VM not found |
| 405 | Insufficient resources |

---

## Notes

- Virtual Machine Manager package must be installed
- Requires sufficient CPU, RAM, and storage resources
- VMs can run Windows, Linux, or other operating systems
- Network configuration required for VM connectivity
- Images can be imported from ISO files or created from VMs

