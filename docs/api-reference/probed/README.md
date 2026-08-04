# Probed APIs

**Category:** Reference

[← Back to API Reference](../README.md)

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

**320 APIs** across 43 pages, **351 confirmed methods**.

| Page | APIs | Methods |
|---|---:|---:|
| [API](api.md) | 4 | 4 |
| [Core-other](core-other.md) | 38 | 39 |
| [Core · AppPriv](core-apppriv.md) | 3 | 4 |
| [Core · BandwidthControl](core-bandwidthcontrol.md) | 3 | 3 |
| [Core · CMS](core-cms.md) | 3 | 3 |
| [Core · DDNS](core-ddns.md) | 4 | 4 |
| [Core · Directory](core-directory.md) | 13 | 15 |
| [Core · ExternalDevice](core-externaldevice.md) | 15 | 16 |
| [Core · FileServ](core-fileserv.md) | 12 | 13 |
| [Core · Hardware](core-hardware.md) | 11 | 11 |
| [Core · ISCSI](core-iscsi.md) | 7 | 12 |
| [Core · MediaIndexing](core-mediaindexing.md) | 5 | 5 |
| [Core · MyDSCenter](core-mydscenter.md) | 3 | 3 |
| [Core · Network](core-network.md) | 19 | 23 |
| [Core · Notification](core-notification.md) | 15 | 20 |
| [Core · Package](core-package.md) | 12 | 7 |
| [Core · PersonalNotification](core-personalnotification.md) | 4 | 4 |
| [Core · PortForwarding](core-portforwarding.md) | 3 | 4 |
| [Core · QuickConnect](core-quickconnect.md) | 3 | 3 |
| [Core · Region](core-region.md) | 3 | 3 |
| [Core · Security](core-security.md) | 12 | 16 |
| [Core · Share](core-share.md) | 3 | 3 |
| [Core · Sharing](core-sharing.md) | 3 | 3 |
| [Core · SmartBlock](core-smartblock.md) | 5 | 5 |
| [Core · Storage](core-storage.md) | 3 | 4 |
| [Core · SupportForm](core-supportform.md) | 3 | 3 |
| [Core · SyslogClient](core-syslogclient.md) | 3 | 3 |
| [Core · System](core-system.md) | 3 | 3 |
| [Core · Theme](core-theme.md) | 5 | 5 |
| [Core · Web](core-web.md) | 4 | 4 |
| [Docker](docker.md) | 3 | 4 |
| [FileStation](filestation.md) | 15 | 17 |
| [OAUTH](oauth.md) | 4 | 5 |
| [PersonMailAccount](personmailaccount.md) | 3 | 3 |
| [Personal](personal.md) | 14 | 15 |
| [Remote](remote.md) | 3 | 3 |
| [ResourceMonitor](resourcemonitor.md) | 3 | 4 |
| [S2S](s2s.md) | 3 | 5 |
| [SAS](sas.md) | 4 | 4 |
| [SecureSignIn](securesignin.md) | 15 | 15 |
| [SecurityAdvisor](securityadvisor.md) | 6 | 6 |
| [Storage](storage.md) | 6 | 7 |
| [other](other.md) | 17 | 18 |

---

## How this was produced

`SYNO.API.Info` (`query`, `SYNO.API.` prefix) enumerates every API the appliance
exposes with its path and version range. Each was then called with each read-shaped
method name. DSM's error codes make the result unambiguous:

- **103** — method does not exist. The API is real; that verb is not.
- **104** — version unsupported. Validated *before* the method, so probing at the
  wrong version reports nothing useful; each API is probed at its own advertised version.
- **120 / 114 / 101** — the method exists and wants arguments. Still a positive.
- **success** — the method exists and returned data, from which the shape is derived.
