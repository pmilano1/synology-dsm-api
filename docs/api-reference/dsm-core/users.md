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
- `force` (optional): Proceed past the **soft** warnings reported by `validate_set` (e.g. "Synology Photos/Drive use the home service"). Without it, `set` is rejected with **3101** when soft reasons are present.
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true
}
```

**Error codes / notes:**
- `3103` — missing the required `location` parameter (`enable` alone is rejected).
- **`requestFormat` is `JSON`** for this API (per DSM's own `SYNO.API.Info`). Params are
  still **form-encoded**, but each VALUE is parsed as JSON — so a bare word is invalid.
  `synowebapi` says so out loud: `Not a json value: volume1`. Quote strings
  (`location='"volume1"'`); booleans and numbers are already valid JSON unquoted.
  Sending the whole request as a JSON *body* to `entry.cgi` does NOT work — that
  returns **101** (`No parameter of API, method or version`).
- `3103` — missing the required `location` parameter (`enable` alone is rejected).
- `3327` — returned for `location="/volume1"` (a leading-slash volume path).
- `3101` — returned for `location="volume1"` and `location="volume_1"`.

  **Enabling User Home over the API is UNSOLVED as of 2026-07-30 (DSM 7.x).** Recorded
  so nobody repeats this: `get` works fine from the same session that `set` rejects, so
  it is not auth, session, token, or privilege. Ruled out by direct test:

  | Tried | Result |
  |---|---|
  | `validate_set` (both location forms) | success, **empty** `hard_reasons` and `soft_reasons` |
  | `force=true` | 3101 |
  | curl + valid `SynoToken` | 3101 |
  | real DSM UI session + token from `_S('SynoToken')` | 3101 |
  | local `synowebapi --exec`, `runner=SYSTEM_ADMIN` | 3101 |
  | `/volume<n>/homes` present vs moved aside | 3101 **both** |
  | JSON-quoted `location` | 3101 (the parse warning clears, the code does not) |
  | stale `homes` row in `/usr/syno/etc/synoshare.db` | none — DB is clean |

  `SYNO.API.Encryption` is NOT the missing piece: APIs needing it fail with **403**
  (`SYNO.Core.Share` `create` does exactly that), and a local `synowebapi --exec`
  needs no encryption yet still returns 3101.

  What the UI does, from `/usr/syno/synoman/webman/modules/AdminCenter/admin_center.js`:
  the panel declares `webapi:{api:"SYNO.Core.User.Home",version:1,methods:{get:"get",
  set:"set"},params:{get:{additional:["personal_photo_enable"]}}}`, its form fields are
  `enable` and `location` (a store-backed combo, `valueField:"value"`), and it holds a
  `homePollingId` with a `stopHomePollingCallback` — so **enabling is an async job the
  UI polls**, not a synchronous set. That polling half is the most likely missing piece
  and is where to look next. No `method:"set"` call for this API appears anywhere in the
  shipped client JS, so the exact payload has not been recovered from source alone;
  capturing it from a live UI interaction is the remaining route.

  Until then: enable it in Control Panel → User & Group → Advanced → User Home.
- **Must run through the encrypted Web session.** Like `SYNO.Core.Share.set`, enabling User Home via local `synowebapi --exec` may return `success:true` **without** actually flipping `userHomeEnable` — issue it over the authenticated Web API (with [param encryption](authentication.md#syno-api-encryption) + `SynoToken`).

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

