# Hyper Backup Vault

**Category:** Data Protection

[← Back to Hyper Backup](README.md)

---

**Endpoint:** `/webapi/entry.cgi`

**Hyper Backup Vault** is the *server* side: a Synology NAS acting as the **destination**
that receives multi-version backups from other Synology devices (the counterpart to the
client `SYNO.Backup.*` task APIs). It's a separate package (`HyperBackupVault`) and its
APIs only appear when it's installed.

> ⚠️ **Not captured here.** The NAS used for this reference does not run Hyper Backup
> Vault, so the methods/params below are **from the API registry + package purpose, not
> wire-captured**. Verify against a Vault-enabled NAS before relying on them. This file
> exists so the reference has no dead links and records the known surface.

---

## Server-side APIs (from `SYNO.API.Info`)

Enumerated via [`SYNO.API.Info?query=all`](../dsm-core/authentication.md). These are the
backup **server/receiver** endpoints (distinct from the client task APIs in
[tasks.md](tasks.md)):

| API | Ver | Role |
|-----|-----|------|
| `SYNO.Backup.Service.NetworkBackup` | 1 | Network-backup **service** (enable/receive rsync/HB server) |
| `SYNO.SDS.Backup.Server.Common.Log` | 1 | Vault-side task logs |
| `SYNO.SDS.Backup.Server.Common.Statistic` | 1 | Vault-side usage/statistics |
| `SYNO.SDS.Backup.Server.Explore.File` | — | Browse files in a received version (server side) |
| `SYNO.SDS.Backup.Server.Explore.Folder` | — | Browse folders in a received version (server side) |

The `SYNO.SDS.Backup.Server.Explore.*` family mirrors the client
[`Explore.*`](versions.md#restore--file-browse-recovery-path) family — the same
browse-a-version surface, but for versions **received** by this NAS as a Vault target.

---

## To document (capture on a Vault-enabled NAS)

1. Install **Hyper Backup Vault**, then re-run `SYNO.API.Info query=all` and diff for new
   `HyperBackupVault` / `SYNO.Backup.Service.*` / `SYNO.SDS.Backup.Server.*` entries.
2. Drive the Vault UI (task list, version explore, relink) and capture the real
   methods/params, then fill this file in the house format (see [tasks.md](tasks.md)).
