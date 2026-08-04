# Personal APIs (probed)

**Category:** Personal Settings

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

## SYNO.Personal.MailAccount

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Personal.MailAccount`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "data": "array<empty>"
  }
}
```

## SYNO.Personal.MailAccount.Contacts

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `list`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Personal.MailAccount.Contacts`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID from `SYNO.API.Auth`

Confirmed present: DSM returned error 8004 rather than 103, so the method exists. What it additionally requires was not determined.
The exact signature was not determined; it is listed here so it is known to exist.

**Response:**

```json
{
  "success": false,
  "error": {
    "code": 8004
  }
}
```

## SYNO.Personal.MailAccount.Mail

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `status`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Personal.MailAccount.Mail`
- `version` (required): `1`
- `method` (required): `status`
- `_sid` (required): Session ID from `SYNO.API.Auth`

Confirmed present: DSM returned error 8004 rather than 103, so the method exists. What it additionally requires was not determined.
The exact signature was not determined; it is listed here so it is known to exist.

**Response:**

```json
{
  "success": false,
  "error": {
    "code": 8004
  }
}
```

## SYNO.Personal.Notification.Conf

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1–2

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Personal.Notification.Conf`
- `version` (required): `2`
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

## SYNO.Personal.Notification.Device

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1–2

#### Method: `list`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Personal.Notification.Device`
- `version` (required): `2`
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

## SYNO.Personal.Notification.Event

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1–2

#### Method: `list`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Personal.Notification.Event`
- `version` (required): `2`
- `method` (required): `list`
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

## SYNO.Personal.Notification.Filter

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `list`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Personal.Notification.Filter`
- `version` (required): `1`
- `method` (required): `list`
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

## SYNO.Personal.Notification.GDPR

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Personal.Notification.GDPR`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "read": "boolean",
    "version": "integer"
  }
}
```

## SYNO.Personal.Notification.Identifier

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Personal.Notification.Identifier`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "id": "string"
  }
}
```

## SYNO.Personal.Notification.Settings

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1–2

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Personal.Notification.Settings`
- `version` (required): `2`
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

## SYNO.Personal.Notification.Token

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Personal.Notification.Token`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "oauth_id": "integer",
    "pushbrowser_server": "string",
    "site": "string",
    "token": "string"
  }
}
```

## SYNO.Personal.Notification.VapidPublicKey

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Personal.Notification.VapidPublicKey`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "public_key": "string"
  }
}
```

## SYNO.Personal.Profile

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1–3

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Personal.Profile`
- `version` (required): `3`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "email": "string",
    "emails": "array<empty>",
    "id": "string",
    "isGuest": "boolean",
    "nickName": "string",
    "photo": "string",
    "photoHash": "string",
    "preferredColor": "string",
    "preferredLanguage": "string",
    "timezone": "string",
    "timezoneDef": "string",
    "title": "string",
    "uid": "integer",
    "userName": "string"
  }
}
```

#### Method: `list`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Personal.Profile`
- `version` (required): `3`
- `method` (required): `list`
- `_sid` (required): Session ID from `SYNO.API.Auth`

Confirmed present, but not callable with the four parameters above — it requires additional parameters — DSM names the missing one in `error.errors`.
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

## SYNO.Personal.Profile.Photo

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1–2

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Personal.Profile.Photo`
- `version` (required): `2`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

Confirmed present, but not callable with the four parameters above — it requires additional parameters — DSM names the missing one in `error.errors`.
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
