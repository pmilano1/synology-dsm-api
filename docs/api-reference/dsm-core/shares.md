# DSM Core - Shares

**Category:** System Management

[← Back to DSM Core](README.md)

---

**Endpoint:** `/webapi/entry.cgi`

---

## SYNO.Core.Share

#### Method: `list`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.Core.Share`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID
- `share_type` (optional): Share type (`all`, `user`, `system`)
- `additional` (optional): Additional fields (comma-separated): `hidden`, `encryption`, `is_aclmode`, `recyclebin`, `share_quota`, `enable_share_compress`, `enable_share_cow`

**Response:**
```json
{
  "success": true,
  "data": {
    "total": 5,
    "shares": [
      {
        "name": "docker",
        "path": "/volume1/docker",
        "vol_path": "/volume1",
        "description": "Docker shared folder",
        "encryption": false,
        "hidden": false,
        "recyclebin": true,
        "share_quota": 0
      }
    ]
  }
}
```

---

#### Method: `get`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.Core.Share`
- `version` (required): `1`
- `method` (required): `get`
- `name` (required): Share name
- `_sid` (required): Session ID
- `additional` (optional): Additional fields

**Response:**
```json
{
  "success": true,
  "data": {
    "share": {
      "name": "docker",
      "path": "/volume1/docker",
      "vol_path": "/volume1",
      "description": "Docker shared folder"
    }
  }
}
```

---

#### Method: `create`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Share`
- `version` (required): `1`
- `method` (required): `create`
- `name` (required): Share name
- `vol_path` (required): Volume path (e.g., `/volume1`)
- `_sid` (required): Session ID
- `desc` (optional): Description
- `encryption` (optional): Enable encryption (default: false)
- `enable_share_compress` (optional): Enable compression (default: false)
- `enable_share_cow` (optional): Enable Btrfs COW (default: false)
- `recyclebin` (optional): Enable recycle bin (default: false)

**Response:**
```json
{
  "success": true
}
```

**Notes:**
- `create` targets a new folder and does **not** adopt an existing folder at
  `<vol_path>/<name>`. If the folder already exists on disk, `create` fails with
  **403** (via a local privileged session) or **119** (via an authenticated
  `_sid`+`SynoToken` session).
- **Reserved share names** — `photo`, `homes`, `home`, `music`, `video`,
  `surveillance`, `web` and similar are owned by their packages/services and are
  created when the owning feature is enabled (Synology Photos creates `photo`;
  [User Home](users.md#syno-core-user-home) creates `homes`/`home`), not via `create`.

---

#### Method: `set`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Share`
- `version` (required): `1`
- `method` (required): `set`
- `name` (required): Share name
- `shareinfo` (required): JSON object with the fields to change (see below) — **the settings must be wrapped in `shareinfo`, not passed flat**
- `_sid` (required): Session ID

The `shareinfo` object carries the actual settings. At minimum include `name` and `vol_path`; add only the fields you want to change:

| `shareinfo` field | Type | Description |
| --- | --- | --- |
| `name` | string | Share name (repeat of the top-level `name`) |
| `vol_path` | string | Volume path, e.g. `/volume1` |
| `desc` | string | Description |
| `recyclebin` | bool | Enable recycle bin |
| `enable_share_compress` | bool | Enable compression |
| `enable_share_cow` | bool | Enable Btrfs COW |
| `nfs_rule` | array | NFS export rules (see below) |

> **The `shareinfo` wrapper is mandatory.** Passing settings flat (e.g. `nfs_rule=[…]` alongside `name`) is rejected with **error 403**, which looks like a permission problem but is actually the malformed request being refused. Wrapping them in `shareinfo` succeeds.

##### `nfs_rule` — NFS export rules

Each element of the `nfs_rule` array is one client rule. Setting it makes DSM
(re)generate `/etc/exports` and apply it — this is the supported, persistent way
to add NFS exports (do **not** hand-edit `/etc/exports`; DSM regenerates it):

```json
"nfs_rule": [
  {
    "client": "192.168.20.0/24",
    "privilege": "RW",
    "squash": "no_root_squash",
    "security": "sys",
    "async": true,
    "crossmnt": false,
    "insecure": true
  }
]
```

| Field | Values | Notes |
| --- | --- | --- |
| `client` | IP / subnet (`192.168.1.0/24`) / hostname / `*` | one rule per client |
| `privilege` | `RW` \| `RO` | |
| `squash` | `no_root_squash` \| `root_squash` \| `all_squash` | |
| `security` | `sys` (+ `krb5`, `krb5i`, `krb5p`) | |
| `async` | bool | async writes |
| `crossmnt` | bool | allow access to mounted subfolders |
| `insecure` | bool | allow connections from non-privileged ports (>1024) |

**Local execution** — `synowebapi --exec api=SYNO.Core.Share method=set version=1 name=<share> shareinfo='{…}'` works directly as SYSTEM_ADMIN (no encryption). **Over the Web API**, `set`/`create` additionally require the `shareinfo` param to be **encrypted** via [`SYNO.API.Encryption`](authentication.md#syno-api-encryption) plus a valid `SynoToken`.

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
- `api` (required): `SYNO.Core.Share`
- `version` (required): `1`
- `method` (required): `delete`
- `name` (required): Share name (comma-separated for multiple)
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true
}
```

---

## SYNO.Core.Share.Permission

#### Method: `get`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.Core.Share.Permission`
- `version` (required): `1`
- `method` (required): `get`
- `name` (required): Share name
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "permissions": [
      {
        "name": "admin",
        "is_group": false,
        "permission": "RW"
      },
      {
        "name": "users",
        "is_group": true,
        "permission": "RO"
      }
    ]
  }
}
```

---

#### Method: `set`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Share.Permission`
- `version` (required): `1`
- `method` (required): `set`
- `name` (required): Share name
- `_sid` (required): Session ID
- `permissions` (required): JSON array of permissions

**Notes:**
- Permission values: `RW` (read/write), `RO` (read-only), `NA` (no access)

**Response:**
```json
{
  "success": true
}
```

