# DSM Core - Certificates

**Category:** System Management

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
- Returns a ZIP file containing certificate files

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

