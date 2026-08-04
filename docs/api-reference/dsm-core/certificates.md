# DSM Core - Certificates

**Category:** System Management

See also: [SSL certificate workflow](../../guides/ssl-certificate-workflow.md) — how these calls fit together, and which order avoids taking DSM offline mid-change.

[← Back to DSM Core](README.md)

---

**Endpoint:** `/webapi/entry.cgi`

---

## SYNO.Core.Certificate

#### Method: `list`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.Core.Certificate`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "certificates": [
      {
        "id": "cert_1",
        "desc": "Default certificate",
        "issuer": {
          "common_name": "Synology Inc. CA",
          "country": "TW",
          "organization": "Synology Inc."
        },
        "subject": {
          "common_name": "synology.me",
          "sub_alt_name": ["*.synology.me", "synology.me"]
        },
        "user_deletable": false,
        "renewable": true,
        "is_default": true,
        "valid_from": "Nov 1 00:00:00 2024 GMT",
        "valid_till": "Nov 1 23:59:59 2025 GMT"
      }
    ]
  }
}
```

---

#### Method: `get`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.Core.Certificate`
- `version` (required): `1`
- `method` (required): `get`
- `id` (required): Certificate ID
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "certificate": {
      "id": "cert_1",
      "desc": "Default certificate",
      "issuer": {
        "common_name": "Synology Inc. CA"
      },
      "subject": {
        "common_name": "synology.me"
      }
    }
  }
}
```

---

## SYNO.Core.Certificate.CRT

#### Method: `import`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Certificate.CRT`
- `version` (required): `1`
- `method` (required): `import`
- `_sid` (required): Session ID
- `key` (required): Private key file (multipart/form-data)
- `cert` (required): Certificate file (multipart/form-data)
- `inter_cert` (optional): Intermediate certificate file
- `desc` (optional): Certificate description
- `as_default` (optional): Set as default certificate (default: false)

**Response:**
```json
{
  "success": true,
  "data": {
    "id": "cert_2"
  }
}
```

---

#### Method: `export`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.Core.Certificate.CRT`
- `version` (required): `1`
- `method` (required): `export`
- `id` (required): Certificate ID
- `_sid` (required): Session ID

**Response:**
```
Binary ZIP archive containing the certificate files (no JSON envelope on success).
```

---

## SYNO.Core.Certificate.LetsEncrypt

#### Method: `create`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Certificate.LetsEncrypt`
- `version` (required): `1`
- `method` (required): `create`
- `_sid` (required): Session ID
- `domain_list` (required): Domain names (comma-separated)
- `email` (required): Email address for Let's Encrypt
- `as_default` (optional): Set as default certificate (default: false)

**Response:**
```json
{
  "success": true,
  "data": {
    "task_id": "letsencrypt_task_123"
  }
}
```

---

#### Method: `renew`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Certificate.LetsEncrypt`
- `version` (required): `1`
- `method` (required): `renew`
- `id` (required): Certificate ID
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "task_id": "letsencrypt_renew_123"
  }
}
```

---

## SYNO.Core.Certificate.Service

#### Method: `get`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.Core.Certificate.Service`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "services": [
      {
        "display_name": "DSM Desktop Service",
        "owner": "root",
        "service": "default",
        "subscriber": "system",
        "user_setable": true,
        "cert_id": "cert_1"
      }
    ]
  }
}
```

**Notes:**
- Shows which services use which certificates
- Allows mapping certificates to specific services


---

> **`get` does not exist on DSM 7.3.2.** Calling it returns `{"error":{"code":103}}`
> even with a valid `SynoToken`, so anything built against it fails in a way that
> looks like an authentication problem. It is not documented as a method here for
> that reason.
>
> The service list comes from `SYNO.Core.Certificate.CRT.list` instead: each
> certificate carries a `services` array, and the union across certificates is every
> assignable service. See the
> [SSL certificate workflow](../../guides/ssl-certificate-workflow.md).

#### Method: `set`

Assigns certificates to services. **This is the only way to change which certificate a
service presents**, short of `as_default` on import — which reassigns everything at
once and is a much larger blast radius.

Not in Synology's published documentation. Captured from DSM 7.3.2's own UI
(Control Panel → Security → Certificate → Settings → Configure) on 2026-08-04 by
intercepting the request the dialog issues, and cross-checked against acme.sh's
`deploy/synology_dsm.sh`, which uses the same call.

**HTTP Method:** POST

**Parameters:**

- `api` (required): `SYNO.Core.Certificate.Service`
- `version` (required): `1`
- `method` (required): `set`
- `settings` (required): JSON array, one object per service being reassigned

Each element of `settings`:

| Field | Meaning |
|---|---|
| `service` | Service descriptor object, copied verbatim from the listing (see below) |
| `old_id` | The certificate id the service currently uses |
| `id` | The certificate id it should use |

The `service` object is not a name — it is the full descriptor DSM identifies a
service by:

| Field | Example | Notes |
|---|---|---|
| `display_name` | `FTPS` | What the UI shows |
| `service` | `ftpd` | The internal service key |
| `subscriber` | `smbftpd` | Owning subsystem |
| `owner` | `root` | |
| `isPkg` | `false` | `true` for package-provided services |

**Example** (verbatim capture, ids redacted):

```
api=SYNO.Core.Certificate.Service&method=set&version=1&settings=[
  {"service":{"display_name":"FTPS","isPkg":false,"owner":"root",
              "service":"ftpd","subscriber":"smbftpd"},
   "old_id":"rHYpUM","id":"CrRATM"}
]
```

**Response:**

Not observed. The capture that produced this documentation deliberately BLOCKED the
request rather than let it reach the appliance, so no response body was returned —
the DSM dialog sat on "Processing. Please wait..." indefinitely, which is what a
blocked write looks like from the UI side.

By analogy with other `SYNO.Core` setters the success shape is expected to be:

```json
{ "success": true }
```

Marked unverified rather than presented as fact. Confirming it requires performing a
real certificate reassignment, which restarts the affected services.

**`old_id` is required and is not decorative.** DSM uses it to detect a concurrent
change; supplying a stale value is how it avoids silently overwriting an assignment
someone else made. Read the current value immediately before writing.

**The UI asks for confirmation before sending this.** Reassigning a certificate
restarts the affected services — for `System default` that includes the DSM web
interface itself, which will drop the connection issuing the request. Sequence the
call so nothing depends on the response arriving.

---

## Authentication — required for every call on this page

All certificate calls need a **`SynoToken`** in addition to the session id. Without
it DSM answers with an error rather than a permission message, which makes a
missing token look like a wrong API name:

| Symptom | Actual cause |
|---|---|
| `{"error":{"code":103},"success":false}` | usually a missing/invalid `SynoToken`, not a nonexistent method |
| `{"error":{"code":119},"success":false}` | session id or token rejected |

Both were reproduced on DSM 7.3.2 by calling `SYNO.Core.Certificate.Service` and
`SYNO.Core.Certificate.CRT` from an authenticated browser session **without** the
token — the session cookie alone is not enough.

Obtain both from `SYNO.API.Auth` (version 6 or 7, negotiated) and pass:

- header `X-SYNO-TOKEN: <token>`
- query parameter `_sid=<sid>`

acme.sh's `deploy/synology_dsm.sh` is a working reference implementation.

## Note on `import`: two API names

This page documents `import` under `SYNO.Core.Certificate.CRT`. acme.sh calls it on
**`SYNO.Core.Certificate`** instead:

```
POST /webapi/entry.cgi?api=SYNO.Core.Certificate&method=import&version=1&SynoToken=…&_sid=…
```

with multipart fields `key`, `cert`, `inter_cert`, `id`, `desc`, `as_default`.

Two differences worth knowing beyond the API name:

- **`id`** — empty string creates a new certificate; passing an existing id REPLACES
  that certificate in place, preserving its service assignments. That is usually
  what a renewal wants, and it avoids needing `Service.set` at all.
- The response may include **`"restart_httpd": true`**, indicating DSM restarted its
  web server — so the caller should expect the connection to drop.

Which name is correct on which DSM version has not been established here. Both are
recorded rather than one being deleted, because picking the wrong one produces error
103, which reads as "method does not exist" and sends you looking for the wrong
problem.

## UI operations without captured APIs

Control Panel → Security → Certificate → Settings → **Advanced** offers two actions
whose API calls are NOT documented here, because triggering them on a live appliance
was not acceptable:

- **Create certificate signing request (CSR)** — generates a CSR to submit to a CA.
- **Reset Certificate** — resets to the default Synology certificate and, in DSM's
  own words, *"all the other certificates will be deleted from your Synology NAS"*.
  Destructive; do not probe casually.
