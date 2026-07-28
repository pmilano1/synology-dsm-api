# Storage - Pool & Volume Creation

**Category:** Storage Management

[← Back to API Reference](../README.md)

---

**Endpoint:** `/webapi/entry.cgi`
**Request format:** JSON (params are JSON-typed; array params like `disk_id` are JSON arrays)

> **Reverse-engineered from a live Synology NAS running DSM 7.x** (June 2026 build).
> Every fact below is tagged **[CONFIRMED]** (seen directly in DSM code, `strings`
> output, or CLI `--help`) or **[INFERRED]** (best guess from context / naming,
> not directly observed). The wizard is a **read-only investigation** — no pool or
> volume was ever created. The exact wire payload for `create` was recovered by
> statically reading the Storage Manager UI JavaScript that *builds* the request;
> it was **not** captured on the wire. Where the payload cannot be fully pinned
> down from static sources, that is called out explicitly.

### Sources mined
- **[CONFIRMED]** Method map: `/usr/syno/synoman/webapi/SYNO.Storage.CGI.lib` (JSON) — exact method names + versions.
- **[CONFIRMED]** Compiled CGI: `/usr/syno/synoman/webapi/lib/libStorage.so` — `strings` shows parameter tokens.
- **[CONFIRMED]** Storage Manager UI JS: `/usr/local/packages/@appstore/StorageManager/ui/storage_panel.js` (Vue) — builds the actual JSON request bodies. This is the authoritative source for the payload shapes below.
- **[CONFIRMED]** CLI tools: `/usr/syno/sbin/synostgpool --help`, `synostgvolume --help`, `synospace --help` — RAID level names + disk-path semantics.
- **[CONFIRMED]** Live `SYNO.API.Info` query + read-only `SYNO.Storage.CGI.Storage load_info` — API versions and disk-id format.

---

## Overview

Three version-1 APIs cover storage-pool and volume lifecycle. All route through
`entry.cgi` and take/return JSON.

| API | maxVersion | Purpose |
| --- | --- | --- |
| `SYNO.Storage.CGI.Pool` | 1 | Create / expand / migrate / repair **storage pools** (RAID arrays) |
| `SYNO.Storage.CGI.Volume` | 1 | Create / expand / manage **volumes** (filesystems on pools), incl. combined pool+volume create |
| `SYNO.Storage.CGI.Storage` | 1 | Read-only overview (`load_info`), system-partition repair, scheduling |

**[CONFIRMED]** via live `SYNO.API.Info`:

```json
{
  "SYNO.Storage.CGI.Pool":    { "minVersion": 1, "maxVersion": 1, "path": "entry.cgi", "requestFormat": "JSON" },
  "SYNO.Storage.CGI.Volume":  { "minVersion": 1, "maxVersion": 1, "path": "entry.cgi", "requestFormat": "JSON" },
  "SYNO.Storage.CGI.Storage": { "minVersion": 1, "maxVersion": 1, "path": "entry.cgi", "requestFormat": "JSON" }
}
```

### DSM storage model (how create actually works)

DSM separates the **storage pool** (the RAID array / SHR device) from the
**volume** (the Btrfs/ext4 filesystem placed on the pool):

- On **multi-bay** systems the UI can create a pool first (`Pool.create`) and a
  volume afterward (`Volume.create_on_existing_pool` or `Volume.deploy_unused`).
- On a **single-bay** system, or the "1 pool = 1 volume" quick path, the UI
  creates **both at once** by calling **`Volume.create`**, which internally
  provisions the pool and the volume together. **[CONFIRMED]** — the JS
  `doCreatePoolAndVolume()` calls `SYNO.Storage.CGI.Volume/create` with disk +
  RAID params; `doCreatePool()` calls `SYNO.Storage.CGI.Pool/create`.

---

## Authentication

Standard DSM session auth. Obtain a `sid`, then pass `_sid` (or a cookie) on each call.

```
GET /webapi/auth.cgi?api=SYNO.API.Auth&version=6&method=login
    &account=<user>&passwd=<pw>&session=Core&format=sid
→ { "success": true, "data": { "sid": "..." } }
```

Pool/volume create requires **administrator** privileges (`allowUser`:
`admin.local`, `admin.ldap`, `admin.domain` — **[CONFIRMED]** from the `.lib`).

---

## Method inventory (from `SYNO.Storage.CGI.lib`) — [CONFIRMED]

**`SYNO.Storage.CGI.Pool` v1**

`pre_delete_check`, `cancel_data_scrubbing`, `pause_data_scrubbing`, **`create`**,
`data_scrubbing`, `data_scrubbing_plain`, `delete`, `deactivate`, `edit_desc`,
`get_setting`, `set_setting`, `enum_resource`, **`estimate_size`**,
**`expand_by_add_disk`**, `expand_unallocated`, `expand_unfinished_shr`,
`migrate`, `repair`, `replace`, `check_fast_repair`, `is_disk_detected_old_info`,
`reassemble`, `remove_missing_pool`, `update_raid_sb_cache`, `remove_raid_sb_cache`

**`SYNO.Storage.CGI.Volume` v1**

`pre_delete_check`, `cancel_data_scrubbing`, `pause_data_scrubbing`,
`cancel_defrag`, `cancel_fs_scrubbing`, **`create_on_existing_pool`**, **`create`**,
`data_scrubbing`, `defrag`, `delete`, **`deploy_unused`**, `enum_resource`,
**`estimate_size`**, **`expand_by_add_disk`**, `expand_pool_child`,
`expand_unallocated`, `expand_unfinished_shr`, `convert_shr_to_pool`,
`convert_shr_without_drive`, `fs_scrubbing`, `migrate`, `next_trim_time_get`,
`repair`, `ssd_trim_get`, `ssd_trim_save`, `vol_extent_size_get`,
`vol_extent_size_set`, `transfer_to_rw`, `get_space_usage`, `enable_space_usage`,
`disable_space_usage`, `set_setting`, `failover_keep_rw`, `get_dump_volumes`,
`unlock_by_vault`, `get_recovery_key`, `export_recovery_key`,
`fs_info_on_pool_meta_set`, `fs_info_on_pool_meta_update`, `change_recovery_key`,
`set_dek`, `clean_dek`, `unlock_by_recovery_key`, `get_recovery_key_info`,
`unlock_by_vault_password_key`

**`SYNO.Storage.CGI.Storage` v1**

`load_info`, `load_bad_disks`, `login_check`, `repair_sys_partition`,
`repair_system_partition`, `repair_system_partition_list`, `repair_rootbackup`,
`set_schedule_plan`, `get_schedule_plan`, `set_resync_speed`, `get_resync_speed`,
`set_data_scrubbing_schedule`, `set_data_scrubbing_schedule_status`,
`set_fast_repair_config`, `get_fast_repair_config`, `set_auto_repair_config`,
`get_auto_repair_config`, `get_sche_task_list`, `reload_raid_config`,
`get_space_reclaim_status`, `get_space_reclaim_schedule`,
`set_space_reclaim_schedule`, `delay_space_reclaim`,
`delete_space_reclaim_background_task`, `get_mib_collector_result`,
`load_eunit_topology`

---

## Key enum: RAID / SHR type (`device_type`)

The wire parameter is **`device_type`** **[CONFIRMED]** — a token in `libStorage.so`
and the exact key sent by the UI. The UI uses a short "raidType" internally and
maps it to the `device_type` string actually sent.

### `device_type` values sent to the API — [CONFIRMED]

| `device_type` (wire value) | UI label | Min drives | Fault tolerance |
| --- | --- | --- | --- |
| `shr_without_disk_protect` | SHR (no redundancy, e.g. 1 disk) | 1 | 0 |
| `shr_with_1_disk_protect` | SHR (1-disk redundancy, "SHR-1") | 2 | 1 |
| `shr_with_2_disk_protect` | SHR-2 | 4 | 2 |
| `basic` | Basic | 1 | 0 |
| `raid_0` | RAID 0 | 2 | 0 |
| `raid_1` | RAID 1 | 2 (max 4) | n−1 |
| `raid_5` | RAID 5 | 3 | 1 |
| `raid_6` | RAID 6 | 4 | 2 |
| `raid_10` | RAID 10 | 4 | n/2 |
| `raid_f1` | RAID F1 (SSD) | 3 | 1 |
| `raid_linear` | JBOD / Linear | 1 (2 if RAID-group mode) | 0 |

**[CONFIRMED]** UI-internal short names and the exact mapping (from
`storage_panel.js`, `genRaidTypeSupportTable` / `raidType2DeviceType` /
`deviceType2RaidType`):

```
raidType "shr"        + tolerance 1  → device_type "shr_without_disk_protect"
raidType "shr"        + tolerance ≥2 → device_type "shr_with_1_disk_protect"
raidType "shr_2"                     → device_type "shr_with_2_disk_protect"
raidType "basic|raid_0|raid_1|raid_5|raid_6|raid_10|raid_f1|raid_linear" → same string
```

> **Note on SHR naming:** a single-disk SHR pool is `shr_without_disk_protect`
> (no redundancy). Adding a second disk to reach 1-drive fault tolerance produces
> `shr_with_1_disk_protect`. `deviceType2RaidType` collapses both back to the
> UI's `"shr"` bucket. **[CONFIRMED]**

### CLI RAID-level names (different vocabulary) — [CONFIRMED]

`synostgpool --create` uses a *different* set of level tokens than the Web API.
Do **not** send these to the Web API — they are the CLI's own vocabulary:

```
RAID_LEVEL : SHR1, SHR2, basic, raid0, raid1, raid5, raid6, raid10, linear, raid_f1
Usage: synostgpool --create -t <POOL_TYPE> -l <RAID_LEVEL> [-c] [-d DESC] DISK_PATH_1 DISK_PATH_2 ...
       (-t single ⇒ create an "unused" pool; -c ⇒ run disk check after create)
  e.g. synostgpool --create -t single -l 5 -c -d "my storage pool" /dev/sda3 /dev/sdb3 /dev/sdc3
```

---

## Disk identifiers (the `disk_id` format) — [CONFIRMED]

The Web API identifies disks by their **DSM disk id string**, not a Linux device
node. From a live read-only `SYNO.Storage.CGI.Storage/load_info` on this unit:

| `id` | `num_id` | `device` | container.type |
| --- | --- | --- | --- |
| `sata1` | 1 | `/dev/sata1` | internal |
| `sata2` | 4 | `/dev/sata2` | internal |
| `nvme0n1` | 1 | `/dev/nvme0n1` | internal (M.2) |
| `nvme1n1` | 2 | `/dev/nvme1n1` | internal (M.2) |

- **`disk_id`** is a **JSON array of these id strings**, e.g. `["sata2"]` or
  `["sata1","sata2","sata3"]`. **[CONFIRMED]** — `disk_id:this.selectDisks.map(d=>d.id)`.
- The bay number is `num_id`; the id string is `sata<bay>` for SATA bays and
  `nvme<n>n1` for M.2. **[CONFIRMED]** (`num_id` and `sata` are also tokens in
  `libStorage.so`).
- Internally the CGI resolves each id to a `/dev/<id>` device path and partition
  (`GetDiskPath`, `ValidVolumeCreateDiskPath`, `DiskPathParse`). **[CONFIRMED]**

---

## `SYNO.Storage.CGI.Pool` — `create`

#### Method: `create`

Creates a **storage pool only** (no filesystem). Use this on multi-bay systems
when you want to add a volume separately afterward.

**HTTP Method:** POST

Recovered from `storage_panel.js` `doCreatePool()`. Names tagged **[CONFIRMED-JS]**
were seen built into the request; those also present as tokens in `libStorage.so`
are additionally **[CONFIRMED-BIN]**.

**Parameters:**

| Param | Type | Required | Meaning | Confidence |
| --- | --- | --- | --- | --- |
| `api` | string | yes | `SYNO.Storage.CGI.Pool` | CONFIRMED |
| `version` | int | yes | `1` | CONFIRMED |
| `method` | string | yes | `create` | CONFIRMED |
| `disk_id` | JSON array of string | yes | Disks to consume, e.g. `["sata2"]` | CONFIRMED-JS + BIN |
| `device_type` | string | yes | RAID/SHR type — see enum above (e.g. `shr_without_disk_protect`) | CONFIRMED-JS + BIN |
| `is_disk_check` | bool | yes | Run a disk (bad-sector) check during/after create. UI sends the boolean from a "perform drive check" checkbox | CONFIRMED-JS + BIN |
| `is_pool_child` | bool | yes | `false` for a plain pool create | CONFIRMED-JS + BIN |
| `allocate_size` | string | yes | `"0"` = allocate all available space (pool create always sends `"0"`) | CONFIRMED-JS + BIN |
| `spare_disk_count` | string | yes | Number of hot-spare disks to reserve; `"0"` = none | CONFIRMED-JS + BIN |
| `desc` | string | no | Human description for the pool | CONFIRMED-JS |
| `is_unused` | bool | yes | `true` when the pool is created for the "single-volume" quick path (`selectPoolType === "pool_type_single_volume"`); an "unused"/single pool (cf. CLI `-t single`) | CONFIRMED-JS (semantics INFERRED) |
| `limitNum` | string | yes | Max disks per RAID group. `"24"` when not using RAID-group mode; otherwise `maxDiskNumPerRaidGroup`. **Note camelCase** | CONFIRMED-JS |
| `force` | bool | yes | Override feasibility warnings; UI retries with `true` after a confirmable warning (see Feasibility below) | CONFIRMED-JS |
| `diskGroups` | JSON array | no | Only for multi-RAID-group SHR/large pools: `[{ "isNew": true, "raidPath": "new_raid", "disks": ["sata1","sata2",...] }, ...]`. **Note camelCase** | CONFIRMED-JS |

> **INFERRED:** parameter *types on the wire.* DSM CGIs commonly accept JSON
> arrays/booleans directly under `entry.cgi`, but some deployments stringify
> arrays/bools. The UI passes native JS arrays/booleans to `synowebapi`, so the
> serializer handles encoding. If a raw HTTP client fails, try JSON-encoding
> `disk_id`/`diskGroups` as strings.

**Response:**
```json
{ "success": true }
```
The create promise resolves to a plain success; RAID construction then runs as a
background build polled via `SYNO.Storage.CGI.Storage/load_info`. The full response
body (fields beyond `success`) was not captured — no pool was created (read-only).

---

## `SYNO.Storage.CGI.Volume` — `create` (combined pool + volume)

#### Method: `create`

Creates a **pool and a Btrfs/ext4 volume together** in one call. This is what the
single-bay path and the "1 pool = 1 volume" quick wizard use.

**HTTP Method:** POST

From `doCreatePoolAndVolume()` [CONFIRMED-JS]. Superset of `Pool.create` plus
filesystem params:

**Parameters:**

| Param | Type | Required | Meaning | Confidence |
| --- | --- | --- | --- | --- |
| `api` / `version` / `method` | — | yes | `SYNO.Storage.CGI.Volume` / `1` / `create` | CONFIRMED |
| `disk_id` | JSON array of string | yes | Disks, e.g. `["sata2"]` | CONFIRMED-JS + BIN |
| `device_type` | string | yes | RAID/SHR type (enum above) | CONFIRMED-JS + BIN |
| `fs_type` | string | yes | Filesystem: `btrfs` or `ext4` | CONFIRMED-JS + BIN |
| `pool_path` | string | yes | `""` (empty) when creating a brand-new pool inline | CONFIRMED-JS |
| `is_disk_check` | bool | yes | Drive check | CONFIRMED-JS + BIN |
| `is_pool_child` | bool | yes | `true` unless `selectPoolType === "pool_type_single_volume"` (i.e. `true` when the volume is a child of a multi-volume-capable pool) | CONFIRMED-JS + BIN |
| `allocate_size` | string | yes | Volume size to allocate. `"0"` = use all. UI computes `String(1024 * volumeAllocateSize)` where `volumeAllocateSize` is in **GiB** ⇒ value is in **MiB** | CONFIRMED-JS (unit INFERRED: MiB) |
| `vol_desc` | string | no | Volume description | CONFIRMED-JS + BIN |
| `desc` | string | no | Pool description (`optionalDescInput`) | CONFIRMED-JS |
| `vol_attr` | string | maybe | Volume attribute; `"generic"` in the existing-pool path. Likely also applies here | CONFIRMED-BIN (value "generic" CONFIRMED-JS in create_on_existing_pool) |
| `atime_opt` | string | yes | Access-time mount option; UI sends `"noatime"` | CONFIRMED-JS + BIN |
| `enable_dedupe` | bool | no | Enable Btrfs dedupe on the new volume | CONFIRMED-JS |
| `spare_disk_count` | string | yes | Hot spares; `"0"` = none | CONFIRMED-JS + BIN |
| `limitNum` | string | yes | Max disks per RAID group (`"24"` default). camelCase | CONFIRMED-JS |
| `force` | bool | yes | Override feasibility warnings | CONFIRMED-JS |
| `blocking` | bool | no | Whether to run synchronously/block for a post-create hook (`hasCreatePostHook`). `false` in the common case | CONFIRMED-JS + BIN |
| `diskGroups` | JSON array | no | Multi-RAID-group layout (same shape as Pool.create) | CONFIRMED-JS |
| encryption params | — | no | If encrypting: extra `encParams` merged in and an `encryption:` envelope flag set. Exact keys not enumerated here | INFERRED (getEncryptedVolumeParamsAndEncryption exists) |

**Filesystem enum (`fs_type`)** — **[CONFIRMED]** `btrfs`, `ext4` (both appear in
`libStorage.so` and the UI; `"Invalid fs_type"` is the reject string).

**Response:**
```json
{ "success": true }
```
Plain success (same as `Pool.create`); the build runs in the background. Full
response body was not captured — no volume was created (read-only).

---

## `SYNO.Storage.CGI.Volume` — `create_on_existing_pool` / `deploy_unused`

#### Methods: `create_on_existing_pool`, `deploy_unused`

Adds a volume to a pool that already exists (multi-bay two-step flow).
**[CONFIRMED-JS]** from `doCreateVolume()`:

- `create_on_existing_pool` — for a pool that supports multiple volumes. Sends
  `pool_path` (the existing pool path) + `allocate_size`.
- `deploy_unused` — for an "unused"/single pool. Sends `space_path` instead of
  `pool_path`.

**HTTP Method:** POST

Common params (object `o`): `fs_type`, `vol_attr: "generic"`, `vol_desc`,
`atime_opt: "noatime"`, `force`, `enable_dedupe`, plus `allocate_size` (=`String(1024*volumeAllocateSize)`),
and either `pool_path` or `space_path`. **[CONFIRMED-JS]**

**Parameters:**

| Param | Method | Meaning | Confidence |
| --- | --- | --- | --- |
| `pool_path` | create_on_existing_pool | Existing pool's space path (e.g. `/volume-path` / internal pool id) | CONFIRMED-JS |
| `space_path` | deploy_unused | The unused pool's space path | CONFIRMED-JS |
| `allocate_size` | both | MiB to allocate; `"0"` = all | CONFIRMED-JS (unit INFERRED) |
| `fs_type` | both | `btrfs` / `ext4` | CONFIRMED-JS + BIN |
| `vol_attr` | both | `"generic"` | CONFIRMED-JS + BIN |
| `vol_desc` | both | Description | CONFIRMED-JS + BIN |
| `atime_opt` | both | `"noatime"` | CONFIRMED-JS + BIN |
| `enable_dedupe` | both | Btrfs dedupe on/off | CONFIRMED-JS |
| `force` | both | Override feasibility warnings | CONFIRMED-JS |

**Response:**
```json
{ "success": true }
```
Plain success; not fired during this read-only investigation.

---

## `SYNO.Storage.CGI.Pool` — `estimate_size` (pre-create sizing)

#### Method: `estimate_size`

Before create, the UI estimates usable capacity. **[CONFIRMED-JS]** — issued as a
**parallel compound request** (`SYNO.Entry.Request` / `request`) with one entry per
RAID group.

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Storage.CGI.Pool`
- `version` (required): `1`
- `method` (required): `estimate_size`
- `estimate_for` (required): `"create"`
- `disk_id` (required): JSON array of disk ids, e.g. `["sata2"]`
- `device_type` (required): RAID/SHR type (enum above)

Example params object (one entry of the compound request):

```json
{
  "api": "SYNO.Storage.CGI.Pool",
  "method": "estimate_size",
  "version": 1,
  "params": { "estimate_for": "create", "disk_id": ["sata2"], "device_type": "shr_without_disk_protect" }
}
```

**Response:**
```json
{ "success": true, "data": { "size": 0 } }
```
Each response entry carries `data.size` (bytes), which the UI sums. **[CONFIRMED-JS]**
`estimate_for` and `device_type` are also **[CONFIRMED-BIN]** tokens.

---

## Expanding an existing SHR pool by adding a disk

**API/method:** `SYNO.Storage.CGI.Pool` → **`expand_by_add_disk`** (v1). **[CONFIRMED]**
(The UI's `addDisk` manage-mode maps to `apiMethodName: "expand_by_add_disk"`.)

This is the operation that takes a 1-disk SHR pool (`shr_without_disk_protect`) and,
by adding a second disk, grows it toward 1-disk redundancy
(`shr_with_1_disk_protect`). The RAID type is **not** re-specified — DSM upgrades
the SHR protection automatically based on the new disk count.

### Parameters — [CONFIRMED-JS] (`getActionParams()` + base object)

| Param | Type | Meaning | Confidence |
| --- | --- | --- | --- |
| `api`/`version`/`method` | — | `SYNO.Storage.CGI.Pool` / `1` / `expand_by_add_disk` | CONFIRMED |
| `space_id` | string | Target pool's space id (from `load_info`, e.g. `reuse_1` / pool space id) | CONFIRMED-JS |
| `disk_id` | JSON array of string | **New** disks to add, e.g. `["sata2"]` | CONFIRMED-JS + BIN |
| `do_expand_child_volume` | bool | Also auto-expand the child volume filesystem after the array grows (`triggerAutoExpand`) | CONFIRMED-JS |
| `force` | bool | Override feasibility warnings | CONFIRMED-JS |
| `diskGroups` | JSON array | Empty `[]` for SHR (SHR has no explicit RAID groups) | CONFIRMED-JS |

> Related expand methods (**[CONFIRMED]** names, params not fully mined):
> `Pool.expand_unallocated`, `Pool.expand_unfinished_shr` (takes `shr_action`),
> `Pool.migrate` (change RAID type — takes `migrate_type`, `disk_id`, `limit_num`,
> `do_expand_child_volume`), `Volume.expand_by_add_disk`, `Volume.expand_pool_child`.

---

## Change RAID Type — SHR → SHR-2 (migrate) — [LIVE-OBSERVED 2026-07-24]

**API/method:** `SYNO.Storage.CGI.Pool` → **`migrate`** (v1). In the UI this is the
pool action **"Change RAID Type"** (menu `pool-<space_id>-more-btn` → *Change RAID
Type*). The wizard: pick target `device_type` (dropdown defaults to the recommended
upgrade) → select the **new** drives to add → confirm summary → an *"All the data on
the newly added drive will be erased"* prompt → migrate begins. Existing pool data is
preserved; only the **added** disks are wiped.

Live run: a 2-disk **SHR (1-disk protection)** pool (`reuse_1`, disks `sata1`,`sata2`)
was migrated to **SHR-2** by adding `sata3`,`sata4`,`sata5` (5×12TB → est. 32.7 TB
usable). Feasibility is exposed beforehand by `load_info` per-pool
`can_do.migrate = { to_shr2: 2 }` (and `expand_by_disk`).

### Parameters — [PARTIAL] (names from `SYNO.Storage.CGI.lib` + expand analogy; exact wire body NOT captured this run — the UI's XHR was not interceptable from the top window)

| Param | Type | Meaning | Confidence |
| --- | --- | --- | --- |
| `api`/`version`/`method` | — | `SYNO.Storage.CGI.Pool` / `1` / `migrate` | CONFIRMED (method name) |
| `space_id` | string | Target pool space id (e.g. `reuse_1`) | INFERRED (expand analogy) |
| `disk_id` | JSON array of string | **New** disks to add, e.g. `["sata3","sata4","sata5"]` | INFERRED |
| `migrate_type` / `device_type` | string | Target RAID/SHR — `shr_with_2_disk_protect` for SHR-2 (see enum above) | INFERRED |
| `do_expand_child_volume` | bool | Auto-expand the child volume after migrate | CONFIRMED (name) |
| `limit_num` | int | (present in lib; purpose unconfirmed) | CONFIRMED (name only) |

> **TODO to reach CONFIRMED:** capture the real body. DSM fires it via `synowebapi`
> from the Storage Manager app context; a top-`window` XHR/fetch hook did **not** see
> it and there is **no** iframe. Next time, hook from DevTools/proxy, or intercept in
> the app's own JS realm, *before* clicking the final **OK**.

### Progress / status machine — [CONFIRMED via `load_info` polling]

While migrating, the pool's `status` becomes **`migrate_to_shr2`** and `disks` already
lists all member drives. Poll `SYNO.Storage.CGI.Storage/load_info` and read the pool's
`progress`:

```json
"status": "migrate_to_shr2",
"disks": ["sata1","sata2","sata3","sata4","sata5"],
"progress": { "step": "join_system", "cur_step": 0, "total_step": 3,
              "percent": "85.25", "remaining_time": 6,
              "is_resync_speed_limited": false }
```

`total_step: 3` — step 0 `join_system` (fast), then the array grow + **parity resync**
(the long phase, hours→a day for 12 TB disks). `raidType` still reports the *old* type
(`single`/SHR) until the migration completes.

---

## Example A — single-disk SHR **Btrfs** pool + volume on disk `sata2`

Single call (combined pool + volume, the single-bay / quick-wizard path).
Shape is **[CONFIRMED-JS]**; exact wire encoding of arrays/bools is **[INFERRED]**.

```http
POST /webapi/entry.cgi HTTP/1.1
Content-Type: application/x-www-form-urlencoded
```
```
api=SYNO.Storage.CGI.Volume
version=1
method=create
disk_id=["sata2"]
device_type=shr_without_disk_protect
fs_type=btrfs
pool_path=
is_disk_check=false
is_pool_child=false
allocate_size=0
vol_desc=
atime_opt=noatime
enable_dedupe=false
spare_disk_count=0
limitNum=24
force=false
```

Equivalent JSON params object the UI builds:

```json
{
  "disk_id": ["sata2"],
  "pool_path": "",
  "fs_type": "btrfs",
  "device_type": "shr_without_disk_protect",
  "is_disk_check": false,
  "is_pool_child": false,
  "allocate_size": "0",
  "vol_desc": "",
  "enable_dedupe": false,
  "atime_opt": "noatime",
  "spare_disk_count": "0",
  "desc": "",
  "force": false,
  "limitNum": "24",
  "blocking": false
}
```

> If you instead want the two-step form: `POST Pool.create` with
> `{ "disk_id": ["sata2"], "device_type": "shr_without_disk_protect",
> "is_disk_check": false, "is_pool_child": false, "allocate_size": "0",
> "spare_disk_count": "0", "is_unused": false, "limitNum": "24", "force": false }`,
> then `POST Volume.create_on_existing_pool` (or `deploy_unused`) with the returned
> pool/space path + `fs_type: "btrfs"`, `allocate_size: "0"`, `vol_attr: "generic"`.

---

## Example B — add disk `sata3` to expand the SHR pool to 1-disk redundancy

Adds a second (or third) disk to an existing SHR pool; DSM promotes
`shr_without_disk_protect` → `shr_with_1_disk_protect` automatically.

```
api=SYNO.Storage.CGI.Pool
version=1
method=expand_by_add_disk
space_id=<pool space id from load_info>
disk_id=["sata3"]
do_expand_child_volume=true
force=false
diskGroups=[]
```

JSON params:

```json
{
  "space_id": "reuse_1",
  "disk_id": ["sata3"],
  "do_expand_child_volume": true,
  "force": false,
  "diskGroups": []
}
```

---

## Feasibility failures & the `force` retry — [CONFIRMED]

`create`/expand may return a **feasibility failure** (e.g. mixed disk sizes, HCL
warnings, capacity caveats). The UI detects this (`IsFeasibilityFail`), shows a
confirmation dialog, and — if the user accepts — **re-issues the identical request
with `force: true`**. So expect a two-attempt pattern: first call may fail with a
confirmable warning; resend with `force=true` to proceed. There is **no separate
"confirm" method** — `force` is the mechanism.

---

## Task / polling behaviour — [CONFIRMED where noted, otherwise INFERRED]

- **[CONFIRMED]** The `create` promise resolves to a **plain success** (the UI's
  success handler just emits `apply-success` and closes the wizard). No explicit
  `task_id` is read back from the create response in this UI flow.
- **[CONFIRMED]** RAID construction runs as a **background build task**: the
  Storage Manager then polls **`SYNO.Storage.CGI.Storage/load_info`** and renders
  the pool's *building* status/progress from that data. `synostgpool
  --restore-building-tasks` ("respawn process for committed tasks") confirms create
  commits a persistent background build.
- **[CONFIRMED-BIN]** Internal build state is modeled by `_space_building_task_` /
  `_space_building_step_` in `libStorage.so` — i.e. create kicks off a
  multi-step background build, not a synchronous operation.
- **[INFERRED]** To track progress from a script: after a successful `create`,
  poll `Storage/load_info` and read the target pool/volume's status + percent from
  `storagePools` / `detected_pools` / `volumes`. A large parity RAID stays in a
  "building/resyncing" state for hours while remaining usable.
- **[CONFIRMED-JS]** `blocking: true` (with a post-create hook) makes the call
  wait for the hook; the default path is non-blocking.

---

## What could NOT be fully determined from static sources

- **Exact on-the-wire encoding** of `disk_id`/`diskGroups`/booleans (native JSON
  vs stringified) under `entry.cgi` — the UI delegates to `synowebapi`'s
  serializer. A **live request capture** (browser devtools while creating a pool,
  or a proxy) would confirm this definitively. *(Investigation was read-only; no
  create was performed.)*
- **`allocate_size` unit** is inferred as **MiB** (UI multiplies a GiB value by
  1024). Not directly labeled in the binary.
- **Encryption parameter keys** for encrypted-volume create were not enumerated
  (only the presence of `getEncryptedVolumeParamsAndEncryption` + an `encryption`
  envelope flag is confirmed).
- **Full `Volume.create` response body** (fields beyond `success`) was not
  captured, since no create was run.

---

*Reverse-engineered 2026-07-23 against a Synology NAS / DSM 7.x. Read-only: no
storage pool or volume was created, modified, or deleted during this work.*
