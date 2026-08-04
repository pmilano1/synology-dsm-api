# FileStation APIs (probed)

**Category:** File Services

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

## SYNO.FileStation.FormUpload

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 2

#### Method: `status`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.FileStation.FormUpload`
- `version` (required): `2`
- `method` (required): `status`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {}
}
```

## SYNO.FileStation.Mount.List

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.FileStation.Mount.List`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "isoList": "array<empty>",
    "mountConfig": {
      "enable_iso_mount": "boolean",
      "enable_remote_mount": "boolean"
    },
    "remoteList": "array<empty>"
  }
}
```

## SYNO.FileStation.Property

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `status`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.FileStation.Property`
- `version` (required): `1`
- `method` (required): `status`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "finished": "boolean"
  }
}
```

## SYNO.FileStation.Property.ACLOwner

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.FileStation.Property.ACLOwner`
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

## SYNO.FileStation.Property.CompressSize

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.FileStation.Property.CompressSize`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

Confirmed present: DSM returned error 401 rather than 103, so the method exists. What it additionally requires was not determined.
The exact signature was not determined; it is listed here so it is known to exist.

**Response:**

```json
{
  "success": false,
  "error": {
    "code": 401
  }
}
```

## SYNO.FileStation.Property.Mtime

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.FileStation.Property.Mtime`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

Confirmed present: DSM returned error 401 rather than 103, so the method exists. What it additionally requires was not determined.
The exact signature was not determined; it is listed here so it is known to exist.

**Response:**

```json
{
  "success": false,
  "error": {
    "code": 401
  }
}
```

## SYNO.FileStation.Search.History

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.FileStation.Search.History`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "history": [
      {
        "folder_path": "array",
        "pattern": "string",
        "recursive": "boolean",
        "timestamp": "integer"
      }
    ],
    "total": "integer"
  }
}
```

## SYNO.FileStation.Settings

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.FileStation.Settings`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "allow_normal_disable_html": "boolean",
    "bandwidth_enable": "string",
    "enable_list_usergrp": "boolean",
    "enable_send_email_attachment": "boolean",
    "enable_sharing_custom_setting": "string",
    "enable_view_google": "boolean",
    "enable_view_microsoft": "boolean",
    "file_request_allow": "string",
    "file_request_group_privilege": {
      "items": "array<empty>"
    },
    "file_request_privilege": {
      "items": "array<empty>"
    },
    "link_limit": "array<empty>",
    "rf_allow": "string",
    "runpgsql": "boolean",
    "schedule_plan": "string",
    "sharing_allow": "string",
    "sharing_default_limit": "string",
    "sharing_disable_html": "string",
    "sharing_gofile_protocol": "string",
    "sharing_group_privilege": {
      "items": "array<empty>"
    },
    "sharing_privilege": {
      "items": "array<empty>"
    },
    "transfer_log_enable": "boolean",
    "use_unix_default_perm": "boolean",
    "vd_allow": "string"
  }
}
```

## SYNO.FileStation.Snapshot

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1–2

#### Method: `list`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.FileStation.Snapshot`
- `version` (required): `2`
- `method` (required): `list`
- `_sid` (required): Session ID from `SYNO.API.Auth`

Confirmed present: DSM returned error 400 rather than 103, so the method exists. What it additionally requires was not determined.
The exact signature was not determined; it is listed here so it is known to exist.

**Response:**

```json
{
  "success": false,
  "error": {
    "code": 400
  }
}
```

## SYNO.FileStation.VFS.Connection

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.FileStation.VFS.Connection`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

Confirmed present: DSM returned error 400 rather than 103, so the method exists. What it additionally requires was not determined.
The exact signature was not determined; it is listed here so it is known to exist.

**Response:**

```json
{
  "success": false,
  "error": {
    "code": 400
  }
}
```

#### Method: `list`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.FileStation.VFS.Connection`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "connections": "array<empty>",
    "offset": "integer",
    "total": "integer"
  }
}
```

## SYNO.FileStation.VFS.File

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.FileStation.VFS.File`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

Confirmed present: DSM returned error 403 rather than 103, so the method exists. What it additionally requires was not determined.
The exact signature was not determined; it is listed here so it is known to exist.

**Response:**

```json
{
  "success": false,
  "error": {
    "code": 403
  }
}
```

## SYNO.FileStation.VFS.Profile

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.FileStation.VFS.Profile`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

Confirmed present: DSM returned error 400 rather than 103, so the method exists. What it additionally requires was not determined.
The exact signature was not determined; it is listed here so it is known to exist.

**Response:**

```json
{
  "success": false,
  "error": {
    "code": 400
  }
}
```

#### Method: `list`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.FileStation.VFS.Profile`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "offset": "integer",
    "profiles": "array<empty>",
    "total": "integer"
  }
}
```

## SYNO.FileStation.VFS.Protocol

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `list`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.FileStation.VFS.Protocol`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "protocols": [
      {
        "api": "string",
        "default_port": "integer",
        "enable_curl": "string",
        "has_server": "boolean",
        "name": "string",
        "protocol": "string"
      }
    ]
  }
}
```

## SYNO.FileStation.VFS.User

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.FileStation.VFS.User`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

Confirmed present: DSM returned error 400 rather than 103, so the method exists. What it additionally requires was not determined.
The exact signature was not determined; it is listed here so it is known to exist.

**Response:**

```json
{
  "success": false,
  "error": {
    "code": 400
  }
}
```

## SYNO.FileStation.VirtualFolder

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1–2

#### Method: `list`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.FileStation.VirtualFolder`
- `version` (required): `2`
- `method` (required): `list`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "folders": "array<empty>",
    "offset": "integer",
    "total": "integer"
  }
}
```
