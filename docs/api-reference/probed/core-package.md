# Core · Package APIs (probed)

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

## SYNO.Core.Package.FakeIFrame

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

## SYNO.Core.Package.Feed

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `list`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Package.Feed`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "items": "array<empty>",
    "total": "integer"
  }
}
```

## SYNO.Core.Package.Info

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Package.Info`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "config": {
      "blBetaChannel": "boolean",
      "blOtherServer": "boolean",
      "def_void": "string",
      "ds_build": "string",
      "ds_major": "string",
      "ds_minor": "string",
      "ds_timezone": "string",
      "ds_unique": "string",
      "myPayBaseURL": "string",
      "myds_id": "string",
      "success": "boolean"
    },
    "prerelease": {
      "agreed": "boolean",
      "success": "boolean"
    },
    "term": {
      "curr_term_version": "string",
      "success": "boolean"
    }
  }
}
```

## SYNO.Core.Package.Log

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Package.Log`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

Additional parameters, from open-source client implementations rather than
from this probe (`synology-api/synology_api/core_service_hw.py:647`):
- `id` (optional)

Confirmed present, but not callable with the common parameters alone — it requires additional parameters; DSM names the missing one in `error.errors`.
The exact signature was not determined; it is listed here so it is known to exist.

**Response:**

```json
{
  "success": false,
  "error": {
    "code": 120
  }
}
```

## SYNO.Core.Package.MyDS

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Package.MyDS`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

Confirmed present: DSM returned error 4571 rather than 103, so the method exists. What it additionally requires was not determined.
The exact signature was not determined; it is listed here so it is known to exist.

**Response:**

```json
{
  "success": false,
  "error": {
    "code": 4571
  }
}
```

## SYNO.Core.Package.Progress

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Package.Progress`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

Additional parameters, from open-source client implementations rather than
from this probe (`synology-api/synology_api/core_service_hw.py:696`):
- `taskid` (optional)

Confirmed present: DSM returned error 4500 rather than 103, so the method exists. What it additionally requires was not determined.
The exact signature was not determined; it is listed here so it is known to exist.

**Response:**

```json
{
  "success": false,
  "error": {
    "code": 4500
  }
}
```

## SYNO.Core.Package.Screenshot

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

## SYNO.Core.Package.Screenshot.Server

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

## SYNO.Core.Package.Setting

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Package.Setting`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "autoupdateall": "boolean",
    "autoupdateimportant": "boolean",
    "enable_autoupdate": "boolean",
    "enable_dsm": "boolean",
    "enable_email": "boolean",
    "mailset": "boolean",
    "show_disable_autoupdate": "boolean",
    "trust_level": "integer",
    "update_channel": "boolean",
    "volume_count": "integer",
    "volume_list": [
      {
        "desc": "string",
        "display": "string",
        "mount_point": "string",
        "size_free": "string",
        "size_total": "string",
        "vol_desc": "string",
        "volume_features": "array<empty>"
      }
    ],
    "volume_status": "string"
  }
}
```

## SYNO.Core.Package.Setting.Volume

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Package.Setting.Volume`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

Confirmed present: DSM returned error 4501 rather than 103, so the method exists. What it additionally requires was not determined.
The exact signature was not determined; it is listed here so it is known to exist.

**Response:**

```json
{
  "success": false,
  "error": {
    "code": 4501
  }
}
```

## SYNO.Core.Package.Thumb

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

## SYNO.Core.Package.Thumb.Server

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1
