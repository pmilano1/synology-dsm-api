# DSM API error codes

**Category:** Reference

[← Back to Probed APIs](README.md)

---

Every code below was either **observed on a live DSM 7.4 appliance** during the API
probe, or is one of the two codes the probe deliberately swallows (103 and 104 — see
the traps section, it matters). Meanings come from Synology's published guides and
from open-source clients; each row cites where.

Codes whose meaning could not be established are listed as **UNKNOWN** rather than
guessed. In a reference table a plausible invention is worse than an admission,
because nothing downstream can tell the two apart.

---

## The traps

Three behaviours account for most misreadings of this API.

**103 does not only mean "no such method".** It is also what DSM returns when the
`SynoToken` header is missing. A caller without the token sees every method on every
API report as non-existent, which looks like a firmware difference rather than an
auth mistake.

**104 is evaluated before the method name.** DSM validates `version` first, so
probing an API at a version it does not support answers 104 for *every* method —
indistinguishable from "this API has no methods" unless you sweep the version range.
This is not hypothetical: an earlier pass of this documentation lost 30 APIs and 71
methods to exactly that, because it stopped at the first 103 instead of trying lower
versions.

**The same number means different things on different APIs.** 400/401/403/404/407 on
`SYNO.API.Auth` are credential, 2FA and IP-block failures; the same numbers on
FileStation and Core APIs are file and permission errors. Never treat these as global.

---

## Global codes

Apply to any API.

| Code | Meaning | Seen | Confidence |
|---:|---|---:|---|
| 100 | Unknown error. | — | high |
| 101 | No parameter of API, method or version. | 14 | high |
| 102 | The requested API does not exist. | — | high |
| 103 | The requested method does not exist. | — | high |
| 104 | The requested version does not support the functionality. | — | high |
| 105 | The logged in session does not have permission. | 3 | high |
| 111 | The network connection is unstable or the system is busy. | 3 | high |
| 114 | Lost parameters for this API (missing required parameter). | 33 | high |
| 117 | The network connection is unstable or the system is busy. | 3 | medium |
| 120 | Officially reserved ('Preserve for other purpose'); in practice used by individual packages as a package-specific error, most commonly 'missing/invalid required parameter'. | 35 | medium |

---

## API-specific codes

Meaningful only in the context of the API that returned them.

| Code | Meaning | Seen | Confidence |
|---:|---|---:|---|
| 400 | Invalid parameter of file operation. | 8 | high |
| 401 | Family-dependent: 'Unknown error of file operation' for FileStation (per file_station_error_codes), but also observed on non-FileStation APIs (SYNO.DR.Node.Credential.get, SYNO.SecurityAdvisor.Conf.Location.get) where the FileStation meaning does not obviously apply. | 5 | medium |
| 403 | Family-dependent: closest documented analogue is FileStation's 'Invalid user does this file operation' (i.e., insufficient privilege for this specific object). Observed mostly on Core.File/Core.Share/Core.SmartBlock.Device family APIs that deal with share/file/device permissions, which fits that reading; on SYNO.API.Auth specifically, 403 instead means '2-factor authentication code required' (official DSM_Login_Web_API_Guide_enu.pdf, API Error Codes table, p.18) -- an entirely different meaning. | 9 | medium |
| 407 | Family-dependent: FileStation's 'Operation not permitted' fits the observed context (FileStation.Property.ACLOwner.get plus two FolderSharing.* calls, all permission/ACL-adjacent). On SYNO.API.Auth, 407 instead means 'Blocked IP source' (official PDF) -- a different meaning entirely. | 3 | medium |
| 1500 | The operation failed. Please sign in to DSM again and retry. | 2 | medium |
| 2624 | Likely part of the Active Directory domain-join/trust error family (documented range 2601-2628 covers invalid domain, wrong DC IP, wrong credentials, account disabled/expired, etc.), but the literal value 2624 itself is not in the published subset of that range. | 2 | medium |
| 2701 | Returned by SYNO.Core.Directory.LDAP.BaseDN.list (and related LDAP config APIs) when LDAP is not configured on the appliance. | 2 | high |
| 3000 | Unable to perform this operation, possibly because the network connection is unstable or the system is busy. Please try again later. | 1 | high |
| 3103 | Not directly documented; inferred to be part of the same generic 'operation failed / system busy' bucket that core_error_codes.py explicitly assigns to the neighboring low numbers of several other families (e.g. 3400-3402, 4300-4302 below) -- here for the User-management family, whose documented range starts at 3106. | 2 | medium |
| 3201 | Not directly documented; inferred to be part of the same generic bucket pattern as 3103 above, here for the Group-management family, whose documented range starts at 3204 (core_error_codes.py:408). | 2 | medium |
| 3400 | Unable to perform this operation, possibly because the network connection is unstable or the system is busy. Please try again later. | 3 | high |
| 3600 | Not directly documented at 3600 itself; inferred to be the generic 'not available/busy' head of the Printer family, whose documented members (3603-3611, e.g. 'account or password invalid', 'IP address already used by another network printer') begin a few numbers later. | 3 | medium |
| 4000 | Unable to perform this operation. Please try again later. | 1 | high |
| 4100 | Unable to perform this operation. Please try again later. | 1 | high |
| 4302 | Unable to perform this operation, possibly because the network connection is unstable or the system is busy. Please try again later. | 11 | high |
| 4500 | Unable to perform this operation, possibly because the network connection is unstable or the system is busy. Please try again later. | 1 | high |
| 4501 | Unable to perform this operation, possibly because the network connection is unstable or the system is busy. Please try again later. | 1 | high |
| 4631 | Unable to perform this operation, possibly because the network connection is unstable or the system is busy. Please try again later. | 1 | high |
| 4683 | This webhook provider cannot be found. Please choose a different one. | — | high |
| 4800 | Unable to perform task. Please try again later or contact us for technical support if the issue persists. | 1 | high |
| 5021 | Unable to load system settings, possibly because the network connection is unstable or the system is busy. Please try again later. | 1 | high |
| 5100 | Unable to perform this operation. Please try again later. | 1 | high |
| 5103 | Unable to perform this operation. Please try again later. | 1 | high |
| 5300 | Unable to perform this operation. Please try again later. | 3 | high |
| 18990004 | Bad parameter. | 2 | high |
| 18990505 | Bad LUN UUID. | 1 | high |
| 18990710 | Bad target ID. | 2 | high |

---

## Observed but unidentified

Returned by a real appliance; no source establishes what they mean. Listed so the
next person recognises them instead of rediscovering the mystery.

| Code | Seen | Where it appeared |
|---:|---:|---|
| 2 | 1 | Single-digit code far outside every documented range (100-199 common, 400+ API-specific). Observed once on SYNO.Core.ActionPriv.get. Possibly a raw in |
| 121 | 1 | UNKNOWN (officially reserved, 'Preserve for other purpose'; no package-specific documentation found for this exact value). |
| 404 | 1 | Family-dependent: on SYNO.API.Auth, 404 = 'Failed to authenticate 2-factor authentication code' (official PDF). The single observed occurrence is on S |
| 1001 | 1 | UNKNOWN for SYNO.DisasterRecovery.Retention. (Coincidentally, code 1001 in the unrelated Virtualization error table means 'Need Virtual Machine Manage |
| 1005 | 1 | UNKNOWN for SYNO.Core.Sharing. |
| 2104 | 1 | UNKNOWN for SYNO.Docker.Project. |
| 3794 | 1 | UNKNOWN; likely within the Hardware family (documented neighbors: 3712 'Unsupported fan speed mode', 3795 'One of the port numbers is used by another  |
| 4203 | 3 | UNKNOWN for the OTP (one-time-password / MFA policy) family. |
| 4400 | 18 | UNKNOWN for the Backup/MultiVerLun-version family. |
| 4571 | 1 | UNKNOWN, but likely account/serial-related given proximity to the documented neighbor 4570 ('The serial number of your Synology NAS is either incorrec |
| 4731 | 1 | UNKNOWN for the Notification Advance/Template family. |
| 5403 | 1 | UNKNOWN for the Quota family. |
| 8004 | 4 | UNKNOWN for the PersonMailAccount / Personal.MailAccount (MailPlus-adjacent personal mail/contacts) family. |
| 18990831 | 1 | UNKNOWN; likely part of an iSCSI Replication sub-family (the documented 1899xxxx space is organized by hundreds: 03xx=Btrfs/space, 05xx=LUN, 06xx=LUN- |

---

## Caveats worth carrying

- **2** — Single-digit code far outside every documented range (100-199 common, 400+ API-specific). Observed once on SYNO.Core.ActionPriv.get. Possibly a raw internal/errno passthrough rather than a standard SYNO error code. Do not guess a meaning.
- **100** — Not observed in schema_results.json (probe never triggered it) but included because it anchors the global 100-199 table referenced for 102/103/104 below.
- **101** — None. Consistent across official PDF and both client libraries.
- **102** — Not observed in schema_results.json. The probe (schema_full.py/schema_template.py) only ever calls methods against APIs already confirmed to exist from a prior inventory pass, so 102 was structurally never reachable here -- its absence is a property of the probe, not evidence the code is rare.
- **105** — None beyond minor wording differences between sources.
- **111** — This is a generic placeholder string Synology reuses for 109/110/111/117/118 -- it does not diagnose the actual cause. Observed here on SYNO.Core.ExternalDevice.Bluetooth.* which is more consistent with 'feature/hardware not present on this appliance' than an actual network hiccup; treat the official text as boilerplate, not a literal diagnosis.
- **114** — Highest-count code in the dataset by far -- expected, since the probe calls .get/.list/.status generically without supplying each API's specific required parameters (id, name, etc).
- **117** — Sources disagree: synology-api's error_codes.py matches the official PDF text above, but py-synologydsm-api's const.py ERROR_COMMON instead lists 117 as 'Unknown internal error'. The official PDF is authoritative here, but the divergence shows community libraries are not fully reliable for this range. Also boilerplate/uninformative like 109-111/118.
- **120** — Second-highest-count code in the dataset. Because 120-149 is officially reserved rather than commonly defined, its real meaning is package-defined and must be looked up per-API family, not assumed globally -- the ActiveBackup docs' 'missing parameter' reading is only confirmed for that one package family, though it is broadly consistent with what a bare .get/.list probe would trigger across the AI.*, Docker-adjacent, Backup.*, and Personal.* APIs where it was observed.
- **121** — Only one occurrence (SYNO.Storage.CGI.Smart.list) and no library or doc gives 121 a concrete meaning the way ActiveBackup's docs do for 120. Do not infer 'missing parameter' here without separate confirmation.
- **400** — All 8 observed occurrences are on SYNO.FileStation.* methods, matching this family cleanly. The number 400 means something entirely different on SYNO.API.Auth (see auth 400 = 'no such account/incorrect password') -- code 400 is NOT a global code, its meaning depends entirely on which API family issued it.
- **401** — Mixed evidence: 3 of 4 occurrences are FileStation.Property.* (fits the documented FileStation table), but SYNO.DR.Node.Credential.get and SYNO.SecurityAdvisor.Conf.Location.get are not FileStation APIs and have no published 401 table of their own -- their actual meaning is UNKNOWN, only guessable by analogy to the widely-reused 400-421 idiom Synology packages copy from the FileStation/Calendar convention.
- **403** — None of the 7 observed occurrences are on SYNO.API.Auth itself, so the Auth '2FA required' meaning does not apply here -- but this is exactly the kind of cross-family collision to watch for: the same numeric code means unrelated things on Auth vs. File/Share-permission-adjacent APIs.
- **404** — SYNO.Auth.ForgotPwd is a different API name than the documented SYNO.API.Auth, so the official 400-410 table for SYNO.API.Auth is not guaranteed to carry over verbatim. Treat the meaning here as unverified.
- **407** — None of the 3 occurrences are on SYNO.API.Auth, so 'Blocked IP source' does not apply here -- another cross-family collision like 403/404 above.
- **1001** — Do not reuse the Virtualization 1001 meaning here; it is an unrelated API family that happens to share the number.
- **1005** — The 1000s block in core_error_codes.py starts at 1101 (firewall); 1000-1100 is simply a gap in the scraped bundle, not evidence the code is undefined.
- **1500** — core_error_codes.py also separately documents 1500-1530 as a router/port-forwarding family ('router database', 'port forwarding rules') elsewhere in the same file -- observed here on SYNO.Core.PortForwarding.RouterList.get, which fits that family, but the specific string captured at key 1500 is the generic session-expiry message, not a port-forwarding-specific one. Likely means the probe's session/token was rejected for this call rather than a router-specific failure.
- **2104** — Docker/Container Manager ships as a separate installable package with its own JS bundle; the same gap likely explains other Docker-adjacent UNKNOWNs in this dataset.
- **2624** — 2624 falls inside the documented 2601-2628 span but is one of the specific integers NOT listed (2617-2625 and 2627 are gaps in the scraped table) -- family membership is a reasonable inference from the range, not a confirmed literal meaning. Observed on SYNO.Core.Directory.Domain.Trust.list/get, consistent with a trust-relationship-specific error within that family.
- **2701** — This is the strongest API-specific citation in the dataset: it names the exact API (SYNO.Core.Directory.LDAP.BaseDN.list) and exact scenario (no active LDAP config) that produced it, matching schema_results.json precisely.
- **3000** — Generic boilerplate text reused across many families (see 3400, 4302, 4500/4501, 4631 below) -- observed on SYNO.Core.MyDSCenter.Purchase.list, consistent with the documented Synology-Account-server family even though the string itself is uninformative about the specific cause.
- **3103** — This is an inference by numbering convention, not a directly sourced meaning -- 3103 itself does not appear in any scraped table. Observed on SYNO.Core.User.get and SYNO.Core.User.Group.get.
- **3201** — Inference by numbering convention only. Observed on SYNO.Core.Group.ExtraAdmin.get and SYNO.Core.Group.Member.list.
- **3400** — Generic boilerplate text, but this is a direct, exact match (not inferred) -- 3400 literally appears in the scraped table. Observed on SYNO.Core.AppPriv.* which is consistent with this family.
- **3600** — 3600-3602 are a gap in the scraped table (3603 is the first documented member) -- inferred by the same generic-bucket-per-family pattern seen at 3400/4300/4500 etc. Observed on SYNO.Core.ExternalDevice.Printer.* which matches the family.
- **3794** — Observed on SYNO.Core.Hardware.OOBManagement.get (out-of-band management, e.g. IPMI-style remote hardware control) -- plausible this is an 'unsupported on this model' style error given the family pattern, but that is a guess, not a citation.
- **4000** — Exact match. Generic boilerplate text again; observed on SYNO.Core.Theme.Image.list.
- **4100** — Exact match, same generic boilerplate. Observed on SYNO.Core.Theme.AppPortalLogin.get.
- **4203** — Clean gap in every source checked. Observed on SYNO.Core.OTP.Admin.get and SYNO.Core.OTP.EnforcePolicy.list.
- **4302** — Exact match, third-highest occurrence count in the dataset (11 of the 47 codes, all on SYNO.Core.Network.* APIs -- Bond, Ethernet, IPv6, MACClone, PPPoE, Router, UPnPServer, etc). Boilerplate text, uninformative about the specific network subsystem involved.
- **4400** — Observed on SYNO.Backup.MultiVerLun.Version.list, SYNO.Backup.Version.list, and SYNO.SDS.Backup.Client.Common.MultiVerLun.Version.get -- consistently a Backup/HyperBackup-adjacent versioning family, but that package's own bundle was not captured by either scraped source.
- **4500** — Exact match, generic boilerplate. Observed on SYNO.Core.Package.Progress.get.
- **4501** — Exact match, same generic boilerplate. Observed on SYNO.Core.Package.Setting.Volume.get.
- **4571** — Observed on SYNO.Core.Package.MyDS.get -- MyDS ties DSM to a Synology Account/serial number, so the 4570 neighbor is a plausible but unconfirmed family match.
- **4631** — Exact match, generic boilerplate. Observed on SYNO.Core.Notification.SMS.Provider.get.
- **4683** — Exact match and, unusually for this dataset, a specific/meaningful message rather than generic boilerplate. Observed on SYNO.Core.Notification.Push.Webhook.Provider.get, which fits precisely (probe requested a webhook provider that does not exist on this appliance).
- **4731** — Observed on SYNO.Core.Notification.Advance.FilterSettings.Template.get -- consistent placement within the broader Notification numbering block, but the specific code is an undocumented gap.
- **4800** — Exact match. Observed on SYNO.Core.TaskScheduler.get.
- **5021** — Exact match, generic boilerplate. Observed on SYNO.Core.SyslogClient.PersonalActivity.get.
- **5100** — Exact match, generic boilerplate. Observed on SYNO.Core.Security.AutoBlock.Rules.list.
- **5103** — Exact match, same generic boilerplate. Observed on SYNO.Core.Security.AutoBlock.Rules.get.
- **5300** — Exact match, generic boilerplate. Observed on SYNO.Core.BandwidthControl.get and SYNO.Core.BandwidthControl.Protocol.get.
- **5403** — Observed on SYNO.Core.Quota.get. No source covers this range.
- **8004** — core_error_codes.py's 8000-8231 range documents an entirely unrelated WiFi/network-daemon/PPPoE family; 8004 is numerically adjacent to that family ('The max characters have been reached' at 8003) purely by coincidence -- do not assume the WiFi-family meaning carries over to PersonMailAccount, a completely different package. Observed identically on both the SYNO.PersonMailAccount.* and SYNO.Personal.MailAccount.* API name variants, suggesting these are aliases of the same underlying package.
- **18990004** — Exact match. Observed on SYNO.Core.ISCSI.Host.get and SYNO.Core.ISCSI.Lunbkp.get -- both outside the specifically-documented LUN (1899050x) and Target (1899070x) ranges, consistent with 18990004 being the shared generic 'bad parameter' code for the whole iSCSI error space rather than LUN- or Target-specific.
- **18990505** — Exact match. Observed on SYNO.Core.ISCSI.LUN.get.
- **18990710** — Exact match. Observed on SYNO.Core.ISCSI.FCTarget.get and SYNO.Core.ISCSI.Target.get.
- **18990831** — Observed on SYNO.Core.ISCSI.Replication.get, which supports the 'Replication sub-family' guess, but neither client library nor any official PDF found via web search documents this specific value -- treat the family guess as inference, not a citation.
