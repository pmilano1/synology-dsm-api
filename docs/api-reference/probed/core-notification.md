# Core · Notification APIs (probed)

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

## SYNO.Core.Notification.Advance.CustomizedData

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Notification.Advance.CustomizedData`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "content": "string",
    "default_content": "string",
    "default_subject": "string",
    "subject": "string"
  }
}
```

## SYNO.Core.Notification.Advance.FilterSettings

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1–2

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Notification.Advance.FilterSettings`
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

#### Method: `list`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Notification.Advance.FilterSettings`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "All": [
      {
        "appid": "string",
        "cms": "boolean",
        "desktop": "boolean",
        "format": "string",
        "group": "string",
        "level": "string",
        "mail": "boolean",
        "mobile": "boolean",
        "name": "string",
        "sms": "boolean",
        "source": "string",
        "tag": "string",
        "title": "string",
        "warnPercent": "integer"
      }
    ]
  }
}
```

## SYNO.Core.Notification.Advance.FilterSettings.Profile

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `list`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Notification.Advance.FilterSettings.Profile`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "profiles": "array<empty>"
  }
}
```

## SYNO.Core.Notification.Advance.FilterSettings.Template

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Notification.Advance.FilterSettings.Template`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

Confirmed present: DSM returned error 4731 rather than 103, so the method exists. What it additionally requires was not determined.
The exact signature was not determined; it is listed here so it is known to exist.

**Response:**

```json
{
  "success": false,
  "error": {
    "code": 4731
  }
}
```

#### Method: `list`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Notification.Advance.FilterSettings.Template`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "templates": [
      {
        "config": "object",
        "name": "string",
        "template_id": "integer",
        "used_by": "array<empty>"
      }
    ]
  }
}
```

## SYNO.Core.Notification.Advance.Variables

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Notification.Advance.Variables`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "company_name": "string",
    "http_url": "string"
  }
}
```

## SYNO.Core.Notification.CMS.Conf

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1–2

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Notification.CMS.Conf`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "cms_enable": "boolean",
    "join_dsm_cms": "boolean"
  }
}
```

## SYNO.Core.Notification.Mail.Auth

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Notification.Mail.Auth`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "smtp_auth": {
      "enable": "boolean",
      "user": "string"
    }
  }
}
```

## SYNO.Core.Notification.Mail.Conf

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1–2

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Notification.Mail.Conf`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "enable_mail": "boolean",
    "enable_oauth": "boolean",
    "in_use": "array<empty>",
    "mail": "array<empty>",
    "send_welcome_mail": "boolean",
    "sender_mail": "string",
    "sender_name": "string",
    "smtp_auth": {
      "enable": "boolean",
      "user": "string"
    },
    "smtp_info": {
      "port": "integer",
      "server": "string",
      "ssl": "boolean",
      "verifyCert": "boolean"
    },
    "subject_prefix": "string"
  }
}
```

## SYNO.Core.Notification.Push.AuthToken

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Notification.Push.AuthToken`
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
    "register_token": "string"
  }
}
```

## SYNO.Core.Notification.Push.Conf

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Notification.Push.Conf`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "mobile_enable": "boolean",
    "msn_account": "string",
    "msn_bot": "string",
    "msn_enable": "boolean",
    "skype_account": "string",
    "skype_bot": "string",
    "skype_enable": "boolean"
  }
}
```

#### Method: `status`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Notification.Push.Conf`
- `version` (required): `1`
- `method` (required): `status`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "infodata": {
      "service-list": "array<string>",
      "success": "boolean",
      "time": "integer"
    }
  }
}
```

## SYNO.Core.Notification.Push.Mail

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1–2

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Notification.Push.Mail`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "enable_mail": "boolean",
    "mail": "array<empty>",
    "subject_prefix": "string"
  }
}
```

#### Method: `status`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Notification.Push.Mail`
- `version` (required): `1`
- `method` (required): `status`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "verified_mail": "array<empty>"
  }
}
```

## SYNO.Core.Notification.Push.Mobile

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1–2

#### Method: `list`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Notification.Push.Mobile`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "count": "integer",
    "list": "array<empty>",
    "success": "boolean"
  }
}
```

## SYNO.Core.Notification.Push.Webhook.Provider

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1–2

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Notification.Push.Webhook.Provider`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

Confirmed present: DSM returned error 4681 rather than 103, so the method exists. What it additionally requires was not determined.
The exact signature was not determined; it is listed here so it is known to exist.

**Response:**

```json
{
  "success": false,
  "error": {
    "code": 4681
  }
}
```

#### Method: `list`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Notification.Push.Webhook.Provider`
- `version` (required): `1`
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

## SYNO.Core.Notification.SMS.Conf

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1–2

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Notification.SMS.Conf`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "api_id": "string",
    "enable_sms": "boolean",
    "msg_interval": "integer",
    "phone_info": "null",
    "provider_name": "string",
    "sender": "string",
    "user": "string"
  }
}
```

## SYNO.Core.Notification.SMS.Provider

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1–2

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Notification.SMS.Provider`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

Confirmed present: DSM returned error 4631 rather than 103, so the method exists. What it additionally requires was not determined.
The exact signature was not determined; it is listed here so it is known to exist.

**Response:**

```json
{
  "success": false,
  "error": {
    "code": 4631
  }
}
```

#### Method: `list`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Notification.SMS.Provider`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "provider_info": [
      {
        "api_id": "string",
        "provider_id": "string",
        "provider_name": "string",
        "template": "string"
      }
    ]
  }
}
```
