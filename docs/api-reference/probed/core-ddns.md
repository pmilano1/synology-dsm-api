# Core · DDNS APIs (probed)

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

## SYNO.Core.DDNS.Ethernet

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `list`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.DDNS.Ethernet`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": [
    {
      "ifname": "string",
      "ip": "string",
      "ipv6": "array<empty>"
    }
  ]
}
```

## SYNO.Core.DDNS.ExtIP

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1–2

#### Method: `list`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.DDNS.ExtIP`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID from `SYNO.API.Auth`

Additional parameters, from open-source client implementations rather than
from this probe (`synology-api/synology_api/core_sys_info.py:1419`):
- `retry` (required)

**Response:**

```json
{
  "success": true,
  "data": [
    {
      "ip": "string",
      "ipv6": "string",
      "type": "string"
    }
  ]
}
```

## SYNO.Core.DDNS.Provider

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `list`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.DDNS.Provider`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "providers": [
      {
        "id": "string",
        "provider": "string",
        "website": "string"
      }
    ]
  }
}
```

## SYNO.Core.DDNS.Record

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `list`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.DDNS.Record`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "next_update_time": "string",
    "records": "array<empty>"
  }
}
```
