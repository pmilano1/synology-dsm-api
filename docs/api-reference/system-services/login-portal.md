# Login Portal - Application Portal & Reverse Proxy

**Category:** System Services

[← Back to System Services](README.md)

> Reverse-engineered 2026-07-26 (not in Synology's public docs). Covers DSM 7.x
> Control Panel → **Login Portal → Applications** and **→ Advanced → Reverse Proxy**.

---

**Endpoint:** `/webapi/entry.cgi`

Auth: log in first (`SYNO.API.Auth` v7, `session=FileStation`, `format=sid`) and pass `_sid` on every call. All methods below require an admin session.

---

## SYNO.Core.AppPortal.ReverseProxy

DSM's **Reverse Proxy** (Login Portal → Advanced → Reverse Proxy). Entries render to nginx server blocks on the NAS.

#### Method: `list`
- `api`: `SYNO.Core.AppPortal.ReverseProxy` · `version`: `1` · `method`: `list` · `_sid`
- Returns `{ "entries": [ ... ] }`.

#### Method: `create`

**Parameters:**
- `api` (required): `SYNO.Core.AppPortal.ReverseProxy`
- `version` (required): `1`
- `method` (required): `create`
- `_sid` (required): Session ID
- `entry` (required): a **JSON-encoded string** (not a nested object) of the rule:

```json
{
  "description": "Synology Photos",
  "frontend": { "fqdn": "photos.example.com", "port": 443, "protocol": 1, "https": { "hsts": false }, "acl": null },
  "backend":  { "fqdn": "localhost", "port": 5001, "protocol": 1 },
  "proxy_connect_timeout": 60,
  "proxy_read_timeout": 60,
  "proxy_send_timeout": 60,
  "proxy_http_version": 1,
  "proxy_intercept_errors": false,
  "customize_headers": []
}
```

**Field notes:**

| Field | Type | Description |
|-------|------|-------------|
| `frontend.fqdn` | string | Incoming hostname (SNI/Host) |
| `frontend.port` | int | Listen port (usually 443) |
| `frontend.protocol` | int | **1 = HTTPS, 0 = HTTP** |
| `frontend.https.hsts` | bool | Enable HSTS |
| `backend.fqdn` | string | Upstream host (e.g. `localhost`) |
| `backend.port` | int | Upstream port |
| `backend.protocol` | int | 1 = HTTPS, 0 = HTTP |
| `customize_headers` | array | e.g. `[{"name":"Upgrade","value":"$http_upgrade"}]` for websockets |

**Response:** `{ "success": true }`. A new `UUID` appears in `list`.

> ⚠️ `entry` MUST be a JSON string. Passing the object as normal query params → `{"error":{"code":4151}}` (missing/blank `entry`).

---

## SYNO.Core.AppPortal  (Login Portal → Applications)

Per-DSM-app portal settings (alias / customized port / redirect). `version` up to 2.

- `method=list` → `{ "portal": [ { "id": "SYNO.SDS.App.FileStation3.Instance", "display_name": "File Station", "enable_redirect": false } ] }`. Only apps with a portal configured appear.
- `method=set` → requires an app payload; observed error codes: `114` (missing param), `4101` (app not portal-eligible — e.g. **Synology Photos** cannot be given a customized domain this way; use Reverse Proxy instead).

### SYNO.Core.AppPortal.Config
- `method=get`/`set` with `id=<app>` → only exposes `{ "show_titlebar": bool }`. **Not** the domain/port setter (common misconception).

---

## Error codes seen

| Code | Meaning |
|------|---------|
| 103 | Method does not exist |
| 114 | Required parameter missing |
| 119 | Session/permission error (SID invalid or insufficient) |
| 4101 | App not eligible / not found for portal op |
| 4151 | ReverseProxy `entry` missing or not a JSON string |

---

## Serving Synology Photos on a custom hostname (worked example)

Synology Photos is **not** portal-eligible via `AppPortal` (`4101`) and has no Foto-specific portal API. Route it with a Reverse Proxy entry (`frontend: your host` → `backend: the Photos upstream`). Point your external/front proxy's `Host` at the DSM reverse-proxy listener. Backend `localhost:5001` reaches DSM (login) — set the backend to the actual Photos upstream to land on the app.

---

## Root cause: why reverse-proxying Synology Photos shows the DSM login (verified 2026-07-26)

Empirically scanned a DSM 7.x NAS (DSM moved to **5800/5801**; 80/443 serve the app portal):

| URL | Result |
|-----|--------|
| `https://NAS:5801/` | DSM **login** page |
| `https://NAS:5801/photo/` | **404** |
| `https://NAS:5801/?launchApp=SYNO.Foto.AppInstance` | 200, launches Photos (after DSM login) |
| `http(s)://NAS:80|443/photo/` | **200 — but a redirect shell** |

The `/photo/` page on 80/443 is **not the app** — it's a bootstrap that hardcodes the DSM port:
```html
<input id="https" value="5801"><input id="prefer_https" value="true">
<script> var protocol="https:"; var port=5801;
  var URL=protocol+"//"+location.hostname+":"+port+... </script>
```
So the browser is **JS-redirected to `:5801`**. Any reverse proxy that forwards Synology Photos without handling this lands on DSM (login), because the app forces the client back to the DSM port. `backend: localhost:5001` (or 5801) → DSM login / 502.

### The correct fix
DSM **Control Panel → Login Portal → Applications → Synology Photos → Customized Port (or Customized Domain)**. DSM then serves Photos **cleanly on that port/domain without the :5801 redirect**; reverse-proxy your host → that port.

### API status (unsolved via API alone)
- `SYNO.Core.AppPortal.set` is the setter, but every param combo tried (`app`/`apps`/`portal` + `customize_https_port` etc.) returns **`114` (missing param)** or **`4101`** — the exact required param name is **not in any public catalog** and Synology Photos is **not** in `AppPortal.list` (only apps with a portal appear). `AppPortal.Config` only exposes `show_titlebar`.
- **To capture the exact payload:** set the customized port in the DSM UI with browser DevTools open and read the `SYNO.Core.AppPortal set` request. (Blocked here: needs the interactive display.)
- `ReverseProxy.create` works (documented above) but only helps once the app is served on a clean port.
