# SSL certificate workflow

How a certificate gets onto a Synology NAS and in front of a service, end to end,
using the Web API rather than the UI.

Verified against **DSM 7.3.2** on 2026-08-04 by intercepting the calls DSM's own
Control Panel issues, and cross-checked against
[acme.sh's `deploy/synology_dsm.sh`](https://github.com/acmesh-official/acme.sh/blob/master/deploy/synology_dsm.sh),
which performs the same operations.

## The shape of it

DSM separates two things the UI presents together:

1. **A certificate exists** in the appliance's store, with an id.
2. **A service uses it** — a separate mapping from service to certificate id.

Importing does not put a certificate in front of anything. Assigning does. Almost
every surprise in this area comes from conflating them.

## Authentication

Every call below needs a `SynoToken` as well as a session id. A session cookie alone
is not enough, and the failure does not say so — see
[certificates.md](../api-reference/dsm-core/certificates.md) for the error codes and
how they mislead.

```
POST /webapi/entry.cgi?api=…&_sid=<sid>
X-SYNO-TOKEN: <token>
```

Both come from `SYNO.API.Auth` (version 6 or 7, negotiated).

## 1. Read what exists

```
POST api=SYNO.Core.Certificate.CRT&method=list&version=1
```

Returns the certificates with their ids, descriptions, expiry and which is default.

**This is also the service enumeration.** There is no separate "list services" call —
`SYNO.Core.Certificate.Service` exposes only `set`, and asking it for `get` returns
error 103. Instead each certificate carries a `services` array of the services bound
to it, so the union across all certificates is every assignable service:

```json
{ "id": "rHYpUM", "desc": "", "is_default": true,
  "services": [
    { "display_name": "DSM Desktop Service", "service": "default",
      "subscriber": "system", "owner": "root", "isPkg": false,
      "multiple_cert": true, "user_setable": true,
      "display_name_i18n": "common:web_desktop" },
    { "display_name": "FTPS", "service": "ftpd",
      "subscriber": "smbftpd", "owner": "root", "isPkg": false }
  ] }
```

Fields beyond the four needed by `Service.set`:

| Field | Meaning |
|---|---|
| `display_name_i18n` | Translation key; absent on some services |
| `multiple_cert` | Service can hold more than one certificate |
| `user_setable` | Whether the UI lets it be reassigned — respect it |

A service whose `subscriber` is `ReverseProxy` is a DSM reverse-proxy vhost, and its
`service` is a UUID rather than a name. Those are assignable like any other.

**Capture the current mapping before changing anything.** It is what a rollback
needs, and it cannot be reconstructed afterwards from the certificate list alone —
because once reassigned, the old binding is simply gone.

## 2. Import

Two API names are in circulation for `import` — `SYNO.Core.Certificate` and
`SYNO.Core.Certificate.CRT`. Both are documented; see the note in certificates.md
about why neither has been deleted.

```
POST api=SYNO.Core.Certificate&method=import&version=1
  key=<private key>          (multipart)
  cert=<certificate>         (multipart)
  inter_cert=<chain>         (multipart, optional)
  id=<existing id | "">      empty creates new; an id REPLACES in place
  desc=<description>
  as_default=<bool>
```

Two decisions here matter more than the rest.

### Prefer replacing in place

Passing an existing `id` replaces that certificate and **keeps its service
assignments**. For a renewal that is almost always what is wanted: one call, no
reassignment, no window where the new certificate exists but nothing uses it.

Creating a new certificate instead means step 3, and step 3 restarts services.

### Avoid `as_default=true` on import

It reassigns services in the same call that uploads the bytes, including whatever is
serving the connection making the request. Splitting the upload from the assignment
makes the upload non-destructive: if anything is wrong — wrong chain, wrong key,
mismatched pair — the appliance is still serving exactly what it was before, and
nothing needs undoing.

The response may contain `"restart_httpd": true`. Expect the connection to drop; do
not treat that as failure.

## 3. Assign (only if you created a new certificate)

```
POST api=SYNO.Core.Certificate.Service&method=set&version=1
  settings=[{"service":{…},"old_id":"<current>","id":"<new>"}]
```

The `service` value is a descriptor object, not a name — copy it verbatim from the
listing. `old_id` is required: DSM uses it to detect a concurrent change rather than
silently overwriting someone else's assignment, so read it immediately beforehand.

**This restarts the affected services.** Assigning to `System default` restarts the
DSM web interface, which drops the connection issuing the call. Sequence accordingly
and do not wait on a response that will not arrive.

## 4. Verify

Re-read the mapping and confirm the service now points at the new id, and that the
certificate's expiry is what was uploaded. A successful HTTP response only means DSM
accepted the request.

## Rollback

An import does not delete the previous certificate — it stays in the store with its
own id. So rollback is step 3 again with the ids swapped, using the mapping captured
in step 1. That is the reason to capture it rather than assume it can be
reconstructed.

The exception is a replace-in-place import (`id` set), which overwrites the
certificate itself. There is no rollback for that beyond re-importing the previous
certificate, so keep the old one.

## Things that are not this

- **`SYNO.Core.Certificate.LetsEncrypt.create` / `renew`** — DSM issuing its own
  certificate. Useful standalone, but it makes the appliance a second, independent
  issuer. If a certificate is already being issued elsewhere, importing it is the way
  to have one issuance path rather than two.
- **Advanced → Reset Certificate** — resets to the Synology default and, per DSM's own
  warning, *deletes every other certificate on the NAS*. Not a rollback mechanism.
- **`SYNO.Core.Certificate.CSR`** — backs the Advanced tab's "Create certificate
  signing request". Present on DSM 7.3.2 (v1) and not documented here; its methods
  were not probed.
- **`SYNO.Core.Certificate.LetsEncrypt.Account`** and
  **`SYNO.Core.Certificate.Tencent`** — also present and undocumented.
- **A reverse proxy in front of DSM** — if TLS terminates at a proxy, DSM's own
  certificate is only ever seen on the internal leg, and none of this is needed for
  browser-facing trust. It still matters for API clients that talk to DSM directly,
  which otherwise have to disable certificate verification.
