# Core · System APIs (probed)

**Category:** System Management

[← Back to Probed APIs](README.md)

---

These APIs were confirmed against a live DSM 7.4 appliance by probing every
read-shaped method (`list`, `get`, `info`, `status`, `query`, `enum`) at the version the
appliance itself advertises. An entry appears here only because DSM answered for it.

Response blocks are **shapes, not captures** — key names and value *types*, derived on the
appliance so no real hostname, account, share, serial or key ever left it. Where a method
exists but needs arguments, that is stated with the error code rather than guessed at.

Write-shaped methods were not probed: DSM validates `version` *before* `method`, so a
no-argument call to an unknown write method executes it. Those need a disposable appliance.

---

## SYNO.Core.System.Process

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `list`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.System.Process`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "process": [
      {
        "command": "string",
        "cpu": "integer",
        "mem": "integer",
        "mem_shared": "integer",
        "pid": "integer",
        "status": "string"
      }
    ]
  }
}
```

## SYNO.Core.System.ProcessGroup

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `list`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.System.ProcessGroup`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID from `SYNO.API.Auth`

Additional parameters, from open-source client implementations rather than
from this probe (`synology-api/synology_api/core_sys_info.py:1962`):
- `interval` (optional)
- `node` (required)

**Response:**

```json
{
  "success": true,
  "data": {
    "slices": [
      {
        "byte_read_per_sec": "integer",
        "byte_write_per_sec": "integer",
        "cpu_time": "number",
        "cpu_utilization": "integer",
        "icon": "object",
        "memory": "integer",
        "name": "string",
        "name_i18n": "string",
        "process": "array",
        "unit_name": "string"
      }
    ]
  }
}
```

## SYNO.Core.System.Status

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.System.Status`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "ext_nic_is_incompatible": "boolean",
    "is_system_crashed": "boolean",
    "upgrade_ready": "boolean"
  }
}
```
