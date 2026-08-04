# API APIs (probed)

**Category:** Core Protocol

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

## SYNO.API.Auth.Key

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 7

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.API.Auth.Key`
- `version` (required): `7`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "auth_key": "string"
  }
}
```

## SYNO.API.Auth.Key.Code

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 7

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.API.Auth.Key.Code`
- `version` (required): `7`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

Confirmed present, but not callable with the common parameters alone — it the session lacks permission for this method.
The exact signature was not determined; it is listed here so it is known to exist.

**Response:**

```json
{
  "success": false,
  "error": {
    "code": 105
  }
}
```

## SYNO.API.Auth.Type

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.API.Auth.Type`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": [
    {
      "type": "string"
    }
  ]
}
```

## SYNO.API.Auth.UIConfig

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.API.Auth.UIConfig`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": [
    {
      "jsPath": "string",
      "texts": {
        "authenticator": "object"
      },
      "version": "string"
    }
  ]
}
```
