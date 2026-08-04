# Docker APIs (probed)

**Category:** Containers

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

## SYNO.Docker.Container.Log

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Docker.Container.Log`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

Additional parameters, from open-source client implementations rather than
from this probe (`synology-api/synology_api/docker_api.py:1076`):
- `from` (optional)
- `keyword` (optional)
- `level` (optional)
- `limit` (optional)
- `name` (optional)
- `offset` (optional)
- `sort_dir` (optional)
- `to` (optional)

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

## SYNO.Docker.Log

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `list`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Docker.Log`
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

## SYNO.Docker.Project

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Docker.Project`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

Additional parameters, from open-source client implementations rather than
from this probe (`synology-api/synology_api/docker_api.py:590`):
- `id` (optional)

Confirmed present: DSM returned error 2104 rather than 103, so the method exists. What it additionally requires was not determined.
The exact signature was not determined; it is listed here so it is known to exist.

**Response:**

```json
{
  "success": false,
  "error": {
    "code": 2104
  }
}
```

#### Method: `list`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Docker.Project`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {}
}
```

## SYNO.Docker.Registry

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1–2

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Docker.Registry`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "offset": "integer",
    "registries": [
      {
        "enable_registry_mirror": "boolean",
        "enable_trust_SSC": "boolean",
        "mirror_urls": "array<empty>",
        "name": "string",
        "syno": "boolean",
        "url": "string"
      }
    ],
    "total": "integer",
    "using": "string"
  }
}
```
