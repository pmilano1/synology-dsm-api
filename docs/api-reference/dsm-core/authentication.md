# DSM Core - Authentication

**Category:** System Management

[← Back to DSM Core](README.md)

---

**Endpoint:** `/webapi/auth.cgi`

---

## SYNO.API.Auth

#### Method: `login`

**HTTP Method:** GET/POST

**Parameters:**
- `api` (required): `SYNO.API.Auth`
- `version` (required): `7`
- `method` (required): `login`
- `account` (required): Username
- `passwd` (required): Password
- `session` (required): Session name (e.g., `FileStation`, `DownloadStation`, `DSM`)
- `format` (optional): Response format (`cookie` or `sid`, default: `cookie`)
- `otp_code` (optional): 2FA code (if enabled)
- `device_name` (optional): Device name for trusted device
- `device_id` (optional): Device ID for trusted device

**Response:**
```json
{
  "success": true,
  "data": {
    "did": "device_id_12345",
    "sid": "SESSION_ID_STRING",
    "is_portal_port": false,
    "synotoken": "SYNOTOKEN_STRING"
  }
}
```

**Response Fields:**

| Field | Type | Description |
|-------|------|-------------|
| `sid` | string | Session ID for API calls |
| `did` | string | Device ID |
| `synotoken` | string | CSRF token |
| `is_portal_port` | boolean | Using portal port |

---

#### Method: `logout`

**HTTP Method:** GET/POST

**Parameters:**
- `api` (required): `SYNO.API.Auth`
- `version` (required): `7`
- `method` (required): `logout`
- `session` (required): Session name
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true
}
```

---

## SYNO.API.Info

#### Method: `query`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.API.Info`
- `version` (required): `1`
- `method` (required): `query`
- `query` (required): API names (comma-separated or `all`)

**Response:**
```json
{
  "success": true,
  "data": {
    "SYNO.API.Auth": {
      "path": "auth.cgi",
      "minVersion": 1,
      "maxVersion": 7
    },
    "SYNO.FileStation.Info": {
      "path": "entry.cgi",
      "minVersion": 1,
      "maxVersion": 2
    }
  }
}
```

**Notes:**
- Use `query=all` to get all available APIs
- Returns API paths and supported versions
- Useful for discovering available APIs

---

## SYNO.Core.Desktop.SessionData

#### Method: `getjs`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.Core.Desktop.SessionData`
- `version` (required): `1`
- `method` (required): `getjs`
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "SynoToken": "SYNOTOKEN_STRING",
    "isAdmin": true,
    "user": "admin"
  }
}
```

---

## Examples

### Login Example

```bash
curl -X POST "http://192.168.1.100:5000/webapi/auth.cgi" \
  -d "api=SYNO.API.Auth" \
  -d "version=7" \
  -d "method=login" \
  -d "account=admin" \
  -d "passwd=YOUR_PASSWORD" \
  -d "session=FileStation" \
  -d "format=sid"
```

### Login with 2FA

```bash
curl -X POST "http://192.168.1.100:5000/webapi/auth.cgi" \
  -d "api=SYNO.API.Auth" \
  -d "version=7" \
  -d "method=login" \
  -d "account=admin" \
  -d "passwd=YOUR_PASSWORD" \
  -d "otp_code=123456" \
  -d "session=FileStation" \
  -d "format=sid"
```

### Logout Example

```bash
curl "http://192.168.1.100:5000/webapi/auth.cgi" \
  -d "api=SYNO.API.Auth" \
  -d "version=7" \
  -d "method=logout" \
  -d "session=FileStation" \
  -d "_sid=YOUR_SESSION_ID"
```


---

## SYNO.API.Encryption

Some privileged write APIs (e.g. [`SYNO.Core.Share` `create`/`set`](shares.md), password changes) reject **plaintext** params with **error 403** — the sensitive params must be encrypted with a per-request RSA/AES envelope obtained from this API. The DSM web UI does this transparently (`encryption: [...]` on the API call). (Local `synowebapi --exec` as SYSTEM_ADMIN does **not** need it.)

#### Method: `getinfo`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.API.Encryption`
- `version` (required): `1`
- `method` (required): `getinfo`

**Response:**
```json
{
  "success": true,
  "data": {
    "cipherkey": "__cIpHeRtExT",
    "ciphertoken": "__cIpHeRtOkEn",
    "public_key": "<base64 DER RSA public key>",
    "server_time": 1784819806
  }
}
```

**Building the encrypted request** (verified on DSM 7.4):

1. `getinfo` → `public_key`, `cipherkey` (`__cIpHeRtExT`), `ciphertoken` (`__cIpHeRtOkEn`), `server_time`.
2. Generate a random `passphrase`.
3. **AES**-encrypt the target request as an OpenSSL-compatible blob: form the params (including `<ciphertoken>=<server_time>`), URL-encode them, then AES-256-CBC with `passphrase` using OpenSSL `EVP_BytesToKey` (MD5) key/IV derivation and the `Salted__`+salt header; base64 the result.
4. **RSA**-encrypt the `passphrase` with `public_key` (PKCS#1 v1.5); base64 the result.
5. POST to `entry.cgi` a single field: `<cipherkey> = {"rsa":"<b64 rsa>","aes":"<b64 aes>"}`.

The server decrypts, then processes the inner params normally. Include `_sid` (and `SynoToken` for CSRF) among the encrypted params for authenticated calls.
