# SAS APIs (probed)

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

## SYNO.SAS.Encryption

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `status`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.SAS.Encryption`
- `version` (required): `1`
- `method` (required): `status`
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

## SYNO.SAS.Group

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.SAS.Group`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

Confirmed present, but not callable with the common parameters alone — it rejected the call as invalid without the method's own parameters.
The exact signature was not determined; it is listed here so it is known to exist.

**Response:**

```json
{
  "success": false,
  "error": {
    "code": 101
  }
}
```

## SYNO.SAS.Group.Members

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `list`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.SAS.Group.Members`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID from `SYNO.API.Auth`

Confirmed present, but not callable with the common parameters alone — it rejected the call as invalid without the method's own parameters.
The exact signature was not determined; it is listed here so it is known to exist.

**Response:**

```json
{
  "success": false,
  "error": {
    "code": 101
  }
}
```

## SYNO.SAS.Guest

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.SAS.Guest`
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
