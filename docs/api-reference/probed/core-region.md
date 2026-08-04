# Core · Region APIs (probed)

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

## SYNO.Core.Region.Language

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Region.Language`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "codepage": "string",
    "language": "string",
    "maillang": "string"
  }
}
```

## SYNO.Core.Region.NTP

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1–3

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Region.NTP`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "date": "string",
    "enable_ntp": "string",
    "hour": "integer",
    "minute": "integer",
    "now": "string",
    "second": "integer",
    "server": "string",
    "timestamp": "integer",
    "timezone": "string"
  }
}
```

#### Method: `status`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Region.NTP`
- `version` (required): `1`
- `method` (required): `status`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "ntp_status": "boolean"
  }
}
```

## SYNO.Core.Region.NTP.Server

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Region.NTP.Server`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "enable": "boolean"
  }
}
```
