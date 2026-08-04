# Storage APIs (probed)

**Category:** Storage

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

## SYNO.Storage.CGI.HddMan

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Storage.CGI.HddMan`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "BadSctrThrEn": "boolean",
    "RemainLifeThrEn": "boolean",
    "RemainLifeThrVal": "integer",
    "SBMonthLeftThrEn": "boolean",
    "SBMonthLeftThrVal": "integer",
    "WddaEn": "boolean",
    "chkMailSetting": "boolean",
    "db_last_update_time": "integer",
    "healthReportEn": "boolean"
  }
}
```

## SYNO.Storage.CGI.KMIP

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Storage.CGI.KMIP`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "client_cert_info": "null",
    "client_enable": "boolean",
    "conn_success": "boolean",
    "conn_time": "string",
    "kmip_conn_server_desc": "string",
    "kmip_conn_server_port": "string",
    "kmip_db_loc": "string",
    "kmip_enabled": "string",
    "kmip_mode": "string",
    "kmip_server": "string",
    "kmip_server_port": "string",
    "server_cert_info": "null",
    "server_enable": "boolean",
    "support_kmip": "string"
  }
}
```

## SYNO.Storage.CGI.Smart

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `list`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Storage.CGI.Smart`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID from `SYNO.API.Auth`

Confirmed present: DSM returned error 121 rather than 103, so the method exists. What it additionally requires was not determined.
The exact signature was not determined; it is listed here so it is known to exist.

**Response:**

```json
{
  "success": false,
  "error": {
    "code": 121
  }
}
```

## SYNO.Storage.CGI.Smart.Scheduler

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Storage.CGI.Smart.Scheduler`
- `version` (required): `1`
- `method` (required): `get`
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

#### Method: `list`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Storage.CGI.Smart.Scheduler`
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

## SYNO.Storage.CGI.Spare

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `list`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Storage.CGI.Spare`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "hotSpares": "array<empty>"
  }
}
```

## SYNO.Storage.CGI.Spare.Conf

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Storage.CGI.Spare.Conf`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "auto_replacement": "boolean"
  }
}
```
