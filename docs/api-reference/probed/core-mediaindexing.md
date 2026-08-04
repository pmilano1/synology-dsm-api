# Core · MediaIndexing APIs (probed)

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

## SYNO.Core.MediaIndexing

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `status`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.MediaIndexing`
- `version` (required): `1`
- `method` (required): `status`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "reindexing": "boolean"
  }
}
```

## SYNO.Core.MediaIndexing.IndexFolder

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.MediaIndexing.IndexFolder`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "folders": [
      {
        "default": "boolean",
        "exist": "boolean",
        "name": "string",
        "path": "string",
        "types": "array"
      }
    ]
  }
}
```

## SYNO.Core.MediaIndexing.MediaConverter

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1–2

#### Method: `status`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.MediaIndexing.MediaConverter`
- `version` (required): `1`
- `method` (required): `status`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "photo_remain": "integer",
    "photo_total": "integer",
    "resume_time": "integer",
    "status": "string",
    "thumb_remain": "integer",
    "thumb_total": "integer",
    "video_remain": "integer",
    "video_total": "integer"
  }
}
```

## SYNO.Core.MediaIndexing.Scheduler

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.MediaIndexing.Scheduler`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "duration": "integer",
    "manual_action_by_user": "string",
    "mode": "string",
    "start": {
      "hour": "integer"
    },
    "week": "array<boolean>"
  }
}
```

## SYNO.Core.MediaIndexing.ThumbnailQuality

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.MediaIndexing.ThumbnailQuality`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "packages": "array<empty>",
    "thumbnail_quality": "string"
  }
}
```
