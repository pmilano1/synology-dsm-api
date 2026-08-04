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
- `name` (required): Share name, **JSON-encoded — i.e. sent with its quotes**
  (`name="ci_cache"`, not `name=ci_cache`)
- `shareinfo` (required): JSON object carrying the actual settings (below)
- `_sid` (required): Session ID

> **`create` takes the same `shareinfo` envelope that `set` does, plus a
> JSON-quoted top-level `name`.** The flat form (`name=…&vol_path=…&desc=…`)
> that earlier revisions of this page documented is rejected with **403**.

`shareinfo` fields:

| Field | Type | Notes |
| --- | --- | --- |
| `name` | string | share name, repeated from the top-level `name` (unquoted here) |
| `vol_path` | string | volume path, e.g. `/volume1` |
| `desc` | string | description |
| `enable_recycle_bin` | bool | **must be `true` if `recycle_bin_admin_only` is `true`** — the contradictory pair fails with 3300 |
| `recycle_bin_admin_only` | bool | restrict recycle bin to admins |
| `enable_share_cow` | bool | Btrfs COW |
| `enable_share_compress` | bool | compression |
| `name_org` | string | `""` on create; DSM uses it to detect renames |

**Response:**
```json
{"data": {"name": "ci_cache"}, "success": true}
```

**Verified working call** (DSM 7.3.2, DS1525+, plain HTTPS session — see the
encryption note below):

```bash
curl -sk -X POST "https://nas:5001/webapi/entry.cgi" -H "X-SYNO-TOKEN: $TOK" \
  --data-urlencode "api=SYNO.Core.Share" --data-urlencode "version=1" \
  --data-urlencode "method=create" \
  --data-urlencode 'name="ci_cache"' \
  --data-urlencode 'shareinfo={"name":"ci_cache","vol_path":"/volume1","desc":"…","enable_recycle_bin":true,"recycle_bin_admin_only":true,"enable_share_cow":false,"enable_share_compress":false,"name_org":""}' \
  --data-urlencode "_sid=$SID"
```

**Error codes observed on `create`:**

| Code | Meaning |
| --- | --- |
| `403` | malformed request — flat params instead of the `shareinfo` envelope, or a missing/unquoted top-level `name`. Reads like a permission error; it is not. |
| `3300` | envelope accepted, payload invalid — e.g. `enable_recycle_bin:false` together with `recycle_bin_admin_only:true`, or a `vol_path` that has no `shareinfo` counterpart |
| `3301` | share already exists |

**Notes:**
- `create` targets a new folder and does **not** adopt an existing folder at
  `<vol_path>/<name>`.
- The `synoshare --add` CLI is **not** a working substitute on Btrfs volumes with
  share-level ACLs: it fails with `share create failed.[0x0D00 share_is_acl_share.c:49]`.
  Use the Web API.
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

**Local execution** — `synowebapi --exec api=SYNO.Core.Share method=set version=1 name=<share> shareinfo='{…}'` runs as SYSTEM_ADMIN.

> ⚠️ **`create`/`set` do NOT require `SYNO.API.Encryption`.** An earlier revision
> of this page claimed the `shareinfo` param had to be encrypted over the Web
> API. That is wrong, and it sends readers down a long detour building an
> RSA+AES envelope they do not need. **Verified on DSM 7.3.2 (DS1525+):**
> `create` and `SharePrivilege save` both succeed with **plaintext**
> `shareinfo`/`rule` over an ordinary HTTPS session. What is genuinely required
> is the **`X-SYNO-TOKEN` header** (from `enable_syno_token=yes` at login) — a
> missing token is one of the things that surfaces as the same generic `403`
> as a malformed envelope, which is probably how the encryption theory started.
>
> Note also that `synowebapi --exec ... method=create` returns **403** even as
> SYSTEM_ADMIN when given flat params, so the local CLI is not a way around the
> envelope requirement either.

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
| `root_squash` | `"root"` \| `"admin"` \| `"guest"` \| `"all_admin"` \| `"all_guest"` | ⚠️ **`"root"` means "No mapping" and emits `no_root_squash` — root is NOT squashed.** The value names describe *what root is mapped to*, not the exports keyword. Full table below. |

##### `root_squash` values — what each one actually emits

Every value below was set on a live share and the generated `/etc/exports` line
read back (DSM 7.3.2, DS1525+):

| API value | UI label | `/etc/exports` | `anonuid` |
| --- | --- | --- | --- |
| `"root"` | No mapping | `no_root_squash` | 1025 |
| `"admin"` | Map root to admin | `root_squash` | 1024 |
| `"guest"` | Map root to guest | `root_squash` | 1025 |
| `"all_admin"` | Map all users to admin | `all_squash` | 1024 |
| `"all_guest"` | Map all users to guest | `all_squash` | 1025 |

> 🔑 **Two traps here, and this is the second gotcha on this API after
> `security_flavor`.**
>
> 1. **`"root"` is the value that DISABLES squashing.** It names the identity
>    root keeps, not the exports flag. If you want containers to write to the
>    share as root — which is what every Docker/NFS setup needs — this is the
>    value you want. Every share on this fleet that is written to as root
>    (`docker`, `registry`, `backups`, `ci_cache`) carries `root_squash: "root"`.
> 2. **The exports keywords are NOT accepted as input.** Passing
>    `"no_root_squash"`, `"root_squash"` or `"all_squash"` — the obvious guess,
>    since that is what lands in the file — fails with **2301**. So do
>    `"no_mapping"` and `"all"`, which earlier revisions of this page listed as
>    the valid set; they are not valid on DSM 7.3.2.
>
> Because a rejected `save` leaves the **previous rule in place** and returns
> only `{"error":{"code":2301}}`, an unchecked write looks indistinguishable
> from a successful one when you inspect `/etc/exports` afterwards. Always
> assert on `success` rather than on the resulting exports line.
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

