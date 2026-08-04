# Core · SupportForm APIs (probed)

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

## SYNO.Core.SupportForm.Form

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1–2

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.SupportForm.Form`
- `version` (required): `2`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "buildphase": "string",
    "model": "string",
    "server_baseurl": "string",
    "sn": "string",
    "timestamp": "integer",
    "version": "string"
  }
}
```

## SYNO.Core.SupportForm.Log

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `status`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.SupportForm.Log`
- `version` (required): `1`
- `method` (required): `status`
- `_sid` (required): Session ID from `SYNO.API.Auth`

Confirmed present, but not callable with the four parameters above — it requires additional parameters.
The exact signature was not determined; it is listed here so it is known to exist.

**Response:**

```json
{
  "success": false,
  "error": {
    "code": 114
  }
}
```

## SYNO.Core.SupportForm.Service

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.SupportForm.Service`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "app_list": [
      {
        "enable": "boolean",
        "id": "string",
        "name": "string"
      }
    ],
    "enable_support_channel": "boolean",
    "expiredate": "null",
    "fan_debug_en": "boolean",
    "fan_num": "integer",
    "hibernation_debug_en": "boolean",
    "hibernation_debug_level": "integer",
    "log_level_up": "boolean",
    "sns_identifier_key": "null",
    "sysstat_dump_en": "boolean"
  }
}
```
