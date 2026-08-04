# DSM 7.3 — APIs not covered by any existing client

**Category:** API Coverage

[← Back to API Reference](../README.md)

---


50 APIs present on **DSM 7.3.2** that appear in neither this repo nor the two
most complete open-source clients (`py-synologydsm-api`, `synology-api`). Established
by enumerating the appliance with `SYNO.API.Info?query=all` and cross-referencing.

34 of them are `SYNO.AI.*` — DSM 7.3's AI Console. No existing library covers it
because it is new, which is why this is where original documentation is worth doing
rather than importing.

## How these were confirmed

Method names were probed with **read-shaped methods only** (`list`, `get`, `info`,
`status`, `query`, `enum`) and **no arguments**. DSM distinguishes the two outcomes
that matter:

| Response | Meaning |
|---|---|
| `success: true` | method exists and returned data — sample recorded below |
| error `103` | method does not exist |
| any other error | method **exists**, but wants arguments or permissions |

That distinction is what makes confirmation possible without guessing. It is also
why the samples below are real payloads from a live appliance rather than invented
schemas.

**Version is validated before the method**, so an invalid version cannot be used to
test for a method's existence safely — probing requires a valid version, and a method
needing no arguments will therefore execute. Six APIs were excluded for that reason;
they are listed at the end and were never called.

## Confirmed, with response samples

| API | Versions | Method | Sample response |
|---|---|---|---|
| `SYNO.AI.Deid.Matcher` | 1-1 | `list` | `{"matchers":[{"custom":false,"name":"US_STATE_AL","type":"Keyword"},{"custom":false,"name":"US_DRIVERS_LICENSE` |
| `SYNO.AI.Deid.Recognizer` | 1-1 | `list` | `{"recognizers":[{"custom":false,"description":null,"enabled":false,"entity":"IE_PPS","min_confidence":"High","` |
| `SYNO.AI.Deid.Status` | 1-1 | `get` | `{"enabled_recognizers_count":0}` |
| `SYNO.AI.Permission` | 1-1 | `list` | `[]` |
| `SYNO.AI.Policy.Application` | 1-1 | `list` | `{"applications":[{"enable_policy":0,"ns":"Spreadsheet"}]}` |
| `SYNO.AI.Presidio.Memory.Info` | 1-1 | `get` | `{"can_run":true,"free_mem_in_kb":13486636}` |
| `SYNO.AI.Presidio.Setting` | 1-1 | `get` | `{"settings":{"dan":0,"enu":0,"fre":0,"ger":0,"ita":0,"jpn":0,"krn":0,"nld":0,"nor":0,"plk":0,"ptg":0,"rus":0,"` |
| `SYNO.AI.Presidio.Status` | 1-1 | `get` | `{"progress":0,"status":0}` |
| `SYNO.AI.Proxy.Provider` | 1-1 | `list` | `{"providers":[]}` |
| `SYNO.AI.Resource.Config` | 1-1 | `list` | `{"AIConsole":{"app-id":"SYNO.SDS.App.AI.Instance","templates":[{"name":"chat","relpath":"prompt/chat.tmpl"},{"` |
| `SYNO.AI.Statistics.Admin.Log.User` | 1-1 | `list` | `{"users":[]}` |
| `SYNO.AI.Statistics.Admin.Log` | 1-1 | `list` | `{"logs":[]}` |
| `SYNO.AI.Statistics.Request.Log.APIIntegration` | 1-1 | `list` | `{"api_integrations":[]}` |
| `SYNO.AI.Statistics.Request.Log.Action` | 1-1 | `list` | `{"actions":[]}` |
| `SYNO.AI.Statistics.Request.Log.Setting` | 1-1 | `get` | `{"max_size":100000,"retention_days":360,"save_content_output":false}` |
| `SYNO.AI.Statistics.Request.Log.User` | 1-1 | `list` | `{"users":[]}` |
| `SYNO.AI.Statistics.Request.Log` | 1-1 | `list` | `{"logs":[]}` |
| `SYNO.Backup.TieringShare` | 1-1 | `get` | `{}` |
| `SYNO.Core.Directory.Entra.SSO` | 1-1 | `get` | `{"azure_authorization_endpoint":"","azure_client_id":"","azure_logout_endpoint":"","azure_redirect_uri":"","az` |
| `SYNO.Core.FileServ.SMB.Kerberos` | 1-1 | `get` | `{"enabled":false,"keytabUsed":false}` |
| `SYNO.Core.System.GpuInfo` | 1-1 | `list` | `{"support_gpu":false}` |
| `SYNO.Personal.Application.Info.Local` | 1-1 | `get` | `{"applications":[],"total":0}` |

## Confirmed to exist, arguments required

The method is real — DSM answered with something other than 103 — but a bare call is
rejected. Parameters are not documented here because guessing them means calling with
made-up arguments, which is where a read stops being a read.

| API | Versions | Method(s) | Response |
|---|---|---|---|
| `SYNO.AI.App.String` | 1-1 | `get` | error 120 |
| `SYNO.AI.Config` | 1-1 | `get` | error 120 |
| `SYNO.AI.Metrics` | 1-1 | `get` | error 120 |
| `SYNO.AI.Proxy.Provider.Azure.Deployment` | 1-1 | `list` | error 120 |
| `SYNO.AI.Proxy.Provider.Bedrock.Model` | 1-1 | `list` | error 120 |
| `SYNO.AI.Proxy.Provider.OpenAICompat.Model` | 1-1 | `list` | error 120 |
| `SYNO.AI.Statistics.Request.Log.Count` | 1-1 | `get` | error  |
| `SYNO.AI.Statistics.Request.Log.Image` | 1-1 | `get` | error 120 |
| `SYNO.AI.Statistics.Request.Log.RetentionRate` | 1-1 | `get` | error 120 |
| `SYNO.AI.Statistics.Request.Log.Tokens` | 1-1 | `get` | error  |
| `SYNO.Backup.MultiVerLun.Version` | 1-1 | `list` | error 4400 |
| `SYNO.FileStation.ThumbInfo` | 1-1 | `get` | error 101 |
| `SYNO.SDS.Backup.Client.Common.MultiVerLun.Version` | 1-1 | `get` | error 4400 |

## No read-shaped method found

Present on the appliance, but none of `list`/`get`/`info`/`status`/`query`/`enum`
exists. Their methods are presumably writes, and finding them requires capturing the
DSM UI rather than probing.

| API | Versions |
|---|---|
| `SYNO.AI.Completion` | 1-1 |
| `SYNO.AI.Deid.Recognizer.Status` | 1-1 |
| `SYNO.AI.Deid.Regex` | 1-1 |
| `SYNO.AI.Presidio` | 1-1 |
| `SYNO.AI.Thread` | 1-1 |
| `SYNO.Backup.MultiVerLun` | 1-1 |
| `SYNO.Backup.TieringShare.Feasibility` | 1-1 |
| `SYNO.Core.Hardware.EunitConnectionType` | 1-1 |
| `SYNO.OAUTH.Scope` | 1-1 |

## Deliberately not probed

Calling these with no arguments could act rather than report. They are confirmed to
exist by the inventory; nothing was sent to them.

| API | Versions | Why |
|---|---|---|
| `SYNO.AI.Activation` | 1-1 | not probed — activation is a state change |
| `SYNO.AI.Welcome.Wizard` | 1-1 | not probed — wizards complete setup steps |
| `SYNO.Core.Package.Eula` | 1-2 | not probed — accepting a licence is a write |
| `SYNO.Storage.CGI.VolumeReduction` | 1-1 | not probed — could begin shrinking a volume |
| `SYNO.SupportService.Registration` | 1-2 | not probed — registers the appliance with Synology |
| `SYNO.SupportService.RemoteActionFramework` | 1-2 | not probed — triggers remote support actions |
