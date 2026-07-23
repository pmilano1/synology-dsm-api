# DSM Core - Users

**Category:** System Management

[← Back to DSM Core](README.md)

---

**Endpoint:** `/webapi/entry.cgi`

---

## SYNO.Core.User

#### Method: `list`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.Core.User`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID
- `offset` (optional): Starting index (default: 0)
- `limit` (optional): Max results (default: -1 = all)
- `sort_by` (optional): Sort field (default: `name`)
- `sort_direction` (optional): `ASC` or `DESC` (default: `ASC`)
- `additional` (optional): Additional fields (comma-separated): `description`, `email`, `expired`, `cannot_chg_passwd`, `passwd_never_expire`, `password_last_change`, `groups`, `2fa_status`

**Response:**
```json
{
  "success": true,
  "data": {
    "offset": 0,
    "total": 3,
    "users": [
      {
        "name": "admin",
        "description": "System default user",
        "email": "admin@example.com",
        "expired": false,
        "passwd_never_expire": true,
        "groups": ["administrators"],
        "2fa_status": "enabled"
      }
    ]
  }
}
```

---

#### Method: `get`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.Core.User`
- `version` (required): `1`
- `method` (required): `get`
- `name` (required): Username
- `_sid` (required): Session ID
- `additional` (optional): Additional fields

**Response:**
```json
{
  "success": true,
  "data": {
    "user": {
      "name": "admin",
      "description": "System default user",
      "email": "admin@example.com",
      "expired": false,
      "passwd_never_expire": true
    }
  }
}
```

---

#### Method: `create`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.User`
- `version` (required): `1`
- `method` (required): `create`
- `name` (required): Username
- `password` (required): Password
- `_sid` (required): Session ID
- `description` (optional): User description
- `email` (optional): Email address
- `expired` (optional): Account expiration (`never`, `date`)
- `groups` (optional): Group names (comma-separated)

**Response:**
```json
{
  "success": true
}
```

---

#### Method: `set`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.User`
- `version` (required): `1`
- `method` (required): `set`
- `name` (required): Username
- `_sid` (required): Session ID
- `password` (optional): New password
- `description` (optional): User description
- `email` (optional): Email address
- `expired` (optional): Account expiration

**Response:**
```json
{
  "success": true
}
```

---

#### Method: `delete`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.User`
- `version` (required): `1`
- `method` (required): `delete`
- `name` (required): Username (comma-separated for multiple)
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true
}
```

---

## SYNO.Core.User.PasswordPolicy

#### Method: `get`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.Core.User.PasswordPolicy`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "enable_pass_history": true,
    "enable_strong_password": true,
    "min_password_length": 8,
    "password_history_count": 5
  }
}
```

---

## SYNO.Core.User.PasswordExpiry

#### Method: `get`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.Core.User.PasswordExpiry`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "enable": true,
    "expiry_days": 90,
    "warn_days": 7
  }
}
```

---

## SYNO.Core.User.Home

Controls the User Home service (per-user home folders under the `homes` shared folder).

#### Method: `get`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.Core.User.Home`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID
- `additional` (optional): Additional fields (comma-separated): `personal_photo_enable`

**Response:**
```json
{
  "success": true,
  "data": {
    "enable": false
  }
}
```

---

#### Method: `validate_set`

**HTTP Method:** POST

Validates a proposed User Home change before applying it. Returns hard/soft blocking reasons.

**Parameters:**
- `api` (required): `SYNO.Core.User.Home`
- `version` (required): `1`
- `method` (required): `validate_set`
- `enable` (required): Enable User Home (`true`/`false`)
- `location` (required): Volume that hosts the `homes` folder (e.g. `volume1`)
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "hard_reasons": [],
    "soft_reasons": []
  }
}
```

---

#### Method: `set`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.User.Home`
- `version` (required): `1`
- `method` (required): `set`
- `enable` (required): Enable User Home (`true`/`false`)
- `location` (required): Volume that hosts the `homes` folder (e.g. `volume1`)
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true
}
```

**Error codes:**
- `3103` — missing the required `location` parameter (`enable` alone is rejected).
- `3101` — cannot create the `homes` shared folder (e.g. `/volume<n>/homes` already exists on disk). Enabling User Home creates the reserved `homes` share; an existing folder at that path blocks it.

---

#### Method: `stop`

**HTTP Method:** POST

Stops the User Home service.

**Parameters:**
- `api` (required): `SYNO.Core.User.Home`
- `version` (required): `1`
- `method` (required): `stop`
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true
}
```

