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
    "client": "192.168.1.0/24",
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

> ⚠️ **DSM 7.2+ uses a different API and rule schema for NFS.** The `shareinfo.nfs_rule`
> form above is legacy. The current DSM UI (current on **DSM 7.2+**) does **not** set NFS rules through `SYNO.Core.Share set` — it uses the
> dedicated [`SYNO.Core.FileServ.NFS.SharePrivilege`](#syno-core-fileserv-nfs-shareprivilege)
> API, whose rule object has different field **names and value casing**
> (`privilege:"rw"` lowercase, `root_squash:"root"` instead of `squash`, and
> `security_flavor` as an **object of booleans** instead of the `security` string).
> Prefer `SharePrivilege` on DSM 7.2+. See below.

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

## SYNO.Core.FileServ.NFS.SharePrivilege

Per-share NFS export rules on **DSM 7.2+**. This is what the DSM UI
(Control Panel → Shared Folder → *edit* → **NFS Permissions**) actually calls —
it superseded the legacy [`SYNO.Core.Share set` → `shareinfo.nfs_rule`](#nfs_rule--nfs-export-rules)
path. Setting a non-empty rule makes DSM (re)generate `/etc/exports` and apply it
(**do not hand-edit `/etc/exports`** — DSM owns and regenerates it).

*Verified on DSM 7.2+: adding a rule via `save` produces a working NFS export
(confirmed with `showmount -e`).*

#### Method: `load`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.Core.FileServ.NFS.SharePrivilege`
- `version` (required): `1`
- `method` (required): `load`
- `share_name` (required): Share name — **note: `share_name`, not `name`**, and quoted as a JSON string (`share_name="backups"`)
- `_sid` (required): Session ID

**Response:** the current rule set (empty array when the share is not exported):
```json
{ "success": true, "data": { "rule": [] } }
```

#### Method: `save`

**HTTP Method:** POST

Replaces the **entire** rule set for the share (send all rules you want; an empty
`rule:[]` removes the export).

**Parameters:**
- `api` (required): `SYNO.Core.FileServ.NFS.SharePrivilege`
- `version` (required): `1`
- `method` (required): `save`
- `share_name` (required): Share name
- `rule` (required): JSON array of rule objects (schema below)
- `_sid` (required): Session ID

**Rule object** (⚠️ different from the legacy `nfs_rule` schema):
```json
{
  "client": "192.168.1.0/24",
  "privilege": "rw",
  "root_squash": "root",
  "async": true,
  "insecure": false,
  "crossmnt": false,
  "security_flavor": {
    "kerberos": false,
    "kerberos_integrity": false,
    "kerberos_privacy": false,
    "sys": true
  }
}
```

| Field | Type / Values | Notes |
| --- | --- | --- |
| `client` | IP / subnet (`192.168.1.0/24`) / hostname / `*` | one object per client |
| `privilege` | `"rw"` \| `"ro"` | **lowercase** (legacy `nfs_rule` used `RW`/`RO`) |
| `root_squash` | `"root"` \| `"no_mapping"` \| `"all"` | maps to `root_squash` / `no_root_squash` / `all_squash` in `/etc/exports`. `"root"` = **No mapping** in the UI (root stays root) |
| `async` | bool | async writes |
| `insecure` | bool | allow connections from non-privileged ports (>1024) |
| `crossmnt` | bool | allow access to mounted subfolders |
| `security_flavor` | **object of booleans** | `{kerberos, kerberos_integrity, kerberos_privacy, sys}` — set `sys:true` for standard AUTH_SYS |

> 🔑 **The `security_flavor` object is the gotcha.** Sending it as a string
> (`"sys"`) or array (`["sys"]`) — the shape you'd guess from the legacy
> `security` field — fails with **error 2301** (which reads like a generic save
> failure). It **must** be the four-boolean object above. This single field is why
> naive `SharePrivilege save` attempts fail.

**How the UI actually sends it — `SYNO.Entry.Request` compound.** The DSM UI does
not call `save` directly; it batches it with a `SYNO.Core.Share set` in one
compound request so the share record and its NFS rules commit together:

```json
api=SYNO.Entry.Request&method=request&version=1&stop_when_error=true&mode="sequential"&compound=[
  {
    "api": "SYNO.Core.FileServ.NFS.SharePrivilege", "method": "save", "version": "1",
    "share_name": "backups",
    "rule": [
      { "client": "192.168.1.0/24", "privilege": "rw", "root_squash": "root",
        "async": true, "insecure": false, "crossmnt": false,
        "security_flavor": { "kerberos": false, "kerberos_integrity": false,
                             "kerberos_privacy": false, "sys": true } }
    ]
  },
  {
    "api": "SYNO.Core.Share", "method": "set", "version": 1, "name": "backups",
    "shareinfo": { "name": "backups", "vol_path": "/volume1",
                   "desc": "…", "enable_share_cow": false,
                   "enable_share_compress": false, "encryption": false, "enc_passwd": "" }
  }
]
```

Calling `SharePrivilege save` on its own also works; the compound is just how the
UI keeps the two writes atomic. See [`SYNO.Entry.Request`](../dsm-core/README.md)
for the compound envelope.

**Response:**
```json
{ "success": true }
```

**Related:** `SYNO.Core.FileServ.NFS` (`get`/`set`) controls the **global** NFS
service (enable NFS, NFSv4 domain, max protocol). The per-share panel loads it
alongside `SharePrivilege load`; a share export only takes effect when the global
NFS service is enabled.

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

