# API Reference

[← Back to Documentation](../../README.md)

Complete reference for all Synology DSM APIs.

---

## DSM Core APIs

### [Authentication](dsm-core/authentication.md)
Login, logout, session management, API discovery

### [System Info](dsm-core/system-info.md)
System information, utilization, file services, hardware status

### [Users](dsm-core/users.md)
User management, password policies, password expiry

### [Groups](dsm-core/groups.md)
Group management, membership, permissions

### [Packages](dsm-core/packages.md)
Package installation, control, updates

### [Shares](dsm-core/shares.md)
Shared folder management, permissions

### [Certificates](dsm-core/certificates.md)
SSL certificate management, Let's Encrypt

---

## FileStation APIs

### [Info & Listing](filestation/info-listing.md)
FileStation info, list files/folders, get file info

### [Search](filestation/search.md)
Search files and folders

### [File Operations](filestation/file-operations.md)
Create, rename, copy, move, delete files and folders

### [Upload & Download](filestation/upload-download.md)
Upload and download files

### [Sharing](filestation/sharing.md)
Create and manage sharing links

### [Compression](filestation/compression.md)
Compress and extract files

### [Favorites](filestation/favorites.md)
Manage favorite files and folders

### [Background Tasks](filestation/background-tasks.md)
Background task management, directory size, MD5 calculation

---

## DownloadStation APIs

### [Info & Config](downloadstation/info-config.md)
DownloadStation info, configuration, schedule

### [Tasks](downloadstation/tasks.md)
Download task management

### [Statistics](downloadstation/statistics.md)
Download statistics

### [RSS](downloadstation/rss.md)
RSS feed management

### [BT Search](downloadstation/bt-search.md)
BitTorrent search

---

## Docker APIs

### [Containers](docker/containers.md)
Container management (list, start, stop, create, delete)

### [Images](docker/images.md)
Image management (list, pull, delete, search)

### [Networks](docker/networks.md)
Network management

### [Volumes](docker/volumes.md)
Volume management

---

## Photos APIs

### [Folders](photos/folders.md)
Folder browsing and management

### [Albums](photos/albums.md)
Album creation and management

---

## Surveillance Station APIs

### [Info & Cameras](surveillancestation/info-cameras.md)
Station info, camera list, camera control

### [Live View](surveillancestation/live-view.md)
Live camera streams, snapshots

### [PTZ Control](surveillancestation/ptz-control.md)
Pan/tilt/zoom camera control, presets, patrols

### [Recording](surveillancestation/recording.md)
Recording management, playback, download

### [Events](surveillancestation/events.md)
Event query, motion detection, event management

---

## AudioStation APIs

### [Info & Playlists](audiostation/info-playlists.md)
AudioStation info, playlists, pinned songs

### [Remote Players](audiostation/remote-players.md)
Remote player control (play, stop, next, prev)

---

## VPN Server APIs

### [Settings & Status](vpn/settings-status.md)
VPN server settings, active connections, logs

### [Network & Security](vpn/network-security.md)
Network interface settings, security autoblock, permissions

### [Protocols](vpn/protocols.md)
PPTP, OpenVPN, L2TP settings and configuration export

---

## ActiveBackup for Business APIs

### Core

- **[SYNO.ActiveBackup.Device](activebackup/core/device.md)**
- **[SYNO.ActiveBackup.Restore](activebackup/core/restore.md)**
- **[SYNO.ActiveBackup.Setting](activebackup/core/setting.md)**
- **[SYNO.ActiveBackup.Task](activebackup/core/task.md)**
- **[SYNO.ActiveBackup.Version](activebackup/core/version.md)**

### Aem

- **[SYNO.ActiveBackup.AEM](activebackup/aem/aem.md)**
- **[SYNO.ActiveBackup.AEM.Activity](activebackup/aem/aem-activity.md)**
- **[SYNO.ActiveBackup.AEM.AgentInstaller](activebackup/aem/aem-agentinstaller.md)**
- **[SYNO.ActiveBackup.AEM.NFS](activebackup/aem/aem-nfs.md)**
- **[SYNO.ActiveBackup.AEM.Script](activebackup/aem/aem-script.md)**
- **[SYNO.ActiveBackup.AEM.Task](activebackup/aem/aem-task.md)**
- **[SYNO.ActiveBackup.AEM.TaskTemplate](activebackup/aem/aem-tasktemplate.md)**
- **[SYNO.ActiveBackup.AEM.Version](activebackup/aem/aem-version.md)**

### Vm

- **[SYNO.ActiveBackup.Inventory](activebackup/vm/inventory.md)**
- **[SYNO.ActiveBackup.RestoreVM](activebackup/vm/restorevm.md)**

### System

- **[SYNO.ActiveBackup.Activation](activebackup/system/activation.md)**
- **[SYNO.ActiveBackup.General](activebackup/system/general.md)**
- **[SYNO.ActiveBackup.Log](activebackup/system/log.md)**
- **[SYNO.ActiveBackup.Overview](activebackup/system/overview.md)**
- **[SYNO.ActiveBackup.Plan](activebackup/system/plan.md)**
- **[SYNO.ActiveBackup.Report](activebackup/system/report.md)**
- **[SYNO.ActiveBackup.ReportConfig](activebackup/system/reportconfig.md)**
- **[SYNO.ActiveBackup.Share](activebackup/system/share.md)**
- **[SYNO.ActiveBackup.Storage](activebackup/system/storage.md)**
- **[SYNO.ActiveBackup.UserGroup](activebackup/system/usergroup.md)**

### Agent

- **[SYNO.ActiveBackup.Agent](activebackup/agent/agent.md)**
- **[SYNO.ActiveBackup.Agent.Device](activebackup/agent/agent-device.md)**
- **[SYNO.ActiveBackup.Agentless](activebackup/agent/agentless.md)**

### Integration

- **[SYNO.ActiveBackup.Wrapper.Domain](activebackup/integration/wrapper-domain.md)**
- **[SYNO.ActiveBackup.Wrapper.LDAP](activebackup/integration/wrapper-ldap.md)**
- **[SYNO.ActiveBackup.Wrapper.NFS](activebackup/integration/wrapper-nfs.md)**
- **[SYNO.ActiveBackup.Wrapper.NFSPrivilege](activebackup/integration/wrapper-nfsprivilege.md)**

### Other

- **[SYNO.ActiveBackup.Delegation](activebackup/other/delegation.md)**
- **[SYNO.ActiveBackup.TaskTemplate](activebackup/other/tasktemplate.md)**
- **[SYNO.ActiveBackup.Workload](activebackup/other/workload.md)**

