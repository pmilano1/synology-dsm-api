# Core · PersonalNotification APIs (probed)

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

## SYNO.Core.PersonalNotification.Device

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `list`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.PersonalNotification.Device`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "count": "integer",
    "list": "array<empty>"
  }
}
```

## SYNO.Core.PersonalNotification.Filter

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `list`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.PersonalNotification.Filter`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID from `SYNO.API.Auth`

Confirmed present, but not callable with the common parameters alone — it requires additional parameters.
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

## SYNO.Core.PersonalNotification.Mobile

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `list`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.PersonalNotification.Mobile`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID from `SYNO.API.Auth`

Confirmed present, but not callable with the common parameters alone — it requires additional parameters.
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

## SYNO.Core.PersonalNotification.Settings

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.PersonalNotification.Settings`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

Confirmed present, but not callable with the common parameters alone — it requires additional parameters.
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
