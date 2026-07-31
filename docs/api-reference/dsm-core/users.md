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
- **Methods that exist** (probed; `103` = absent): `get`, `set`, `status`, `stop`,
  `validate_set`. `status` needs a parameter (bare call returns `114`).
- **`requestFormat` is `JSON`** (per `SYNO.API.Info`). Params are still form-encoded, but
  each VALUE is parsed as JSON, so bare words are invalid — `synowebapi` says
  `Not a json value: volume1`. Quote strings (`location='"volume1"'`). Sending the whole
  request as a JSON *body* returns **101**.
- **`set` with NO params returns `success:true` and changes nothing** — a no-op. Useful
  as a control: it proves method, auth, session and encryption are all fine, so a failure
  with params is about the params, not the plumbing.
- `3103` — `location` missing entirely (`enable` alone is rejected).
- **`3327` vs `3101` splits purely on a leading slash**, across 11 tested values:

  | `location` | Code |
  |---|---|
  | `/volume1`, `/volume1/` | **3327** |
  | `volume1`, `volume_1`, `1`, `md2`, `reuse_1`, `internal`, `/dev/md2`†, `vol1`, `Volume1` | **3101** |

  († `/dev/md2` returns 3101, so the split is on a *volume-path* shape, not merely on a
  leading slash.) Read 3327 as "path-shaped but rejected" and 3101 as "not a volume
  reference" — 3327 is therefore the *closer* of the two.

  **Enabling User Home over the API is UNSOLVED as of 2026-07-31 (DSM 7.x).** Eliminated
  by direct test, so nobody repeats them:

  | Tried | Result |
  |---|---|
  | `validate_set`, both forms | success, **empty** `hard_reasons` and `soft_reasons` |
  | `force=true`, `enable_recycle_bin`, `encryption=0` | no change |
  | curl + valid `SynoToken` | 3101 |
  | real DSM UI session, token via `_S('SynoToken')` | 3101 |
  | local `synowebapi --exec`, `runner=SYSTEM_ADMIN` | 3101 |
  | **full `SYNO.API.Encryption` RSA+AES envelope** | 3101 — envelope accepted, so encryption is NOT the gap |
  | `/volume<n>/homes` present vs moved aside | 3101 both |
  | stale `homes` row in `synoshare.db` | none; DB clean |

  Note the params both known Ansible implementations send
  (`ppouliot/ansible-collection-synology`, `agaffney/ansible-synology-dsm`) are
  `enable` + `location: "/volume1"` + `enable_recycle_bin` — i.e. the 3327 form. Neither
  project reports the result of that call, so neither corroborates that it succeeds.

  Where to look next: the UI panel
  (`/usr/syno/synoman/webman/modules/AdminCenter/admin_center.js`) declares
  `webapi:{api:"SYNO.Core.User.Home",version:1,methods:{get:"get",set:"set"}}` **and**
  holds a `homePollingId` with a `stopHomePollingCallback` — so enabling is an async job
  the UI polls, and `status` (which exists but needs an undiscovered parameter) is
  presumably its poll. Recovering `status`'s parameter, or capturing a live UI
  interaction, is the open thread. No `method:"set"` call for this API appears anywhere
  in the shipped client JS, so the payload cannot be read from source alone.
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

