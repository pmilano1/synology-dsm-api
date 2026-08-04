# other APIs (probed)

**Category:** DSM Services

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

## SYNO.Auth.ForgotPwd

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Auth.ForgotPwd`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

Confirmed present: DSM returned error 404 rather than 103, so the method exists. What it additionally requires was not determined.
The exact signature was not determined; it is listed here so it is known to exist.

**Response:**

```json
{
  "success": false,
  "error": {
    "code": 404
  }
}
```

## SYNO.Auth.RescueEmail

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Auth.RescueEmail`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "verified": "boolean"
  }
}
```

## SYNO.DSM.Network

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 2

#### Method: `list`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.DSM.Network`
- `version` (required): `2`
- `method` (required): `list`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "dns": "array<string>",
    "gateway": "string",
    "hostname": "string",
    "interfaces": [
      {
        "id": "string",
        "ip": "array",
        "mac": "string",
        "type": "string"
      }
    ],
    "workgroup": "string"
  }
}
```

## SYNO.DisasterRecovery.Log

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `list`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.DisasterRecovery.Log`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "error_count": "integer",
    "info_count": "integer",
    "log_list": "array<empty>",
    "offset": "integer",
    "total": "integer",
    "warn_count": "integer"
  }
}
```

## SYNO.DisasterRecovery.Retention

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.DisasterRecovery.Retention`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

Confirmed present: DSM returned error 1001 rather than 103, so the method exists. What it additionally requires was not determined.
The exact signature was not determined; it is listed here so it is known to exist.

**Response:**

```json
{
  "success": false,
  "error": {
    "code": 1001
  }
}
```

#### Method: `info`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.DisasterRecovery.Retention`
- `version` (required): `1`
- `method` (required): `info`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "adv_features": "array<string>",
    "compatible_versions": "array<integer>",
    "default_retain_recently": "integer",
    "version": "integer"
  }
}
```

## SYNO.Entry.Request.Polling

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `list`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Entry.Request.Polling`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID from `SYNO.API.Auth`

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

#### Method: `status`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Entry.Request.Polling`
- `version` (required): `1`
- `method` (required): `status`
- `_sid` (required): Session ID from `SYNO.API.Auth`

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

## SYNO.FolderSharing.List

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1–2

#### Method: `list`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.FolderSharing.List`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID from `SYNO.API.Auth`

Confirmed present: DSM returned error 407 rather than 103, so the method exists. What it additionally requires was not determined.
The exact signature was not determined; it is listed here so it is known to exist.

**Response:**

```json
{
  "success": false,
  "error": {
    "code": 407
  }
}
```

## SYNO.FolderSharing.Thumb

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1–2

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.FolderSharing.Thumb`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

Confirmed present: DSM returned error 407 rather than 103, so the method exists. What it additionally requires was not determined.
The exact signature was not determined; it is listed here so it is known to exist.

**Response:**

```json
{
  "success": false,
  "error": {
    "code": 407
  }
}
```

## SYNO.Package

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `list`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Package`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "packages": [
      {
        "additional": "object",
        "id": "string",
        "name": "string",
        "timestamp": "integer",
        "version": "string"
      }
    ],
    "total": "integer"
  }
}
```

## SYNO.SDS.Backup.Client.Common.Log

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `list`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.SDS.Backup.Client.Common.Log`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID from `SYNO.API.Auth`

Additional parameters, from open-source client implementations rather than
from this probe (`synology-api/synology_api/core_backup.py:346`):
- `filter_date_from` (optional)
- `filter_date_to` (optional)
- `filter_keyword` (optional)
- `limit` (optional)
- `offset` (optional)

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

## SYNO.SDS.Backup.Client.Common.Statistic

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.SDS.Backup.Client.Common.Statistic`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

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

## SYNO.Snap.Usage.Share

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `status`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Snap.Usage.Share`
- `version` (required): `1`
- `method` (required): `status`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "share_list": "array<empty>"
  }
}
```

## SYNO.SupportService.Setting

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1–2

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.SupportService.Setting`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "fast_support": "boolean"
  }
}
```

## SYNO.VideoPlayer.Subtitle

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

## SYNO.VideoPlayer.SynologyDrive.Subtitle

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1
