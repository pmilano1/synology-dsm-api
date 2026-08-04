# Core · Web APIs (probed)

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

## SYNO.Core.Web.DSM

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1–2

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Web.DSM`
- `version` (required): `2`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "enable_avahi": "boolean",
    "enable_custom_domain": "boolean",
    "enable_hsts": "boolean",
    "enable_https_redirect": "boolean",
    "enable_max_connections": "boolean",
    "enable_reuseport": "boolean",
    "enable_server_header": "boolean",
    "enable_spdy": "boolean",
    "enable_ssdp": "boolean",
    "fqdn": "null",
    "http_port": "integer",
    "https_port": "integer",
    "main_app": "string",
    "max_connections": "integer",
    "max_connections_limit": {
      "lower": "integer",
      "upper": "integer"
    },
    "server_header": "string",
    "support_reuseport": "boolean"
  }
}
```

## SYNO.Core.Web.DSM.External

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Web.DSM.External`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "hostname": "string"
  }
}
```

## SYNO.Core.Web.Security.HTTPCompression

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Web.Security.HTTPCompression`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "http_compression": "boolean"
  }
}
```

## SYNO.Core.Web.Security.TLSProfile

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Web.Security.TLSProfile`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "default-level": "integer",
    "services": {
      "ReverseProxy_4fe9e13f-595f-4a89-819d-d43934b94175": {
        "current-level": "integer",
        "display-name": "string"
      },
      "dsm": {
        "current-level": "integer",
        "display-name": "string",
        "display-name-i18n": "string"
      },
      "smbftpd": {
        "current-level": "integer",
        "display-name": "string",
        "display-name-i18n": "string"
      }
    }
  }
}
```
