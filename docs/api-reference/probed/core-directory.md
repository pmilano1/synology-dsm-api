# Core · Directory APIs (probed)

**Category:** System Management

[← Back to Probed APIs](README.md)

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

## SYNO.Core.Directory.Azure.SSO

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Directory.Azure.SSO`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "azure_client_id": "string",
    "azure_client_secret": "string",
    "azure_redirect_uri": "string",
    "azure_tenant_id": "string"
  }
}
```

## SYNO.Core.Directory.Domain

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1–3

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Directory.Domain`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

Additional parameters, from open-source client implementations rather than
from this probe (`synology-api/synology_api/core_sys_info.py:1681`):
- `get` (required)

**Response:**

```json
{
  "success": true,
  "data": {
    "enable_domain": "boolean"
  }
}
```

## SYNO.Core.Directory.Domain.Conf

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1–3

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Directory.Domain.Conf`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "buildDatabaseWithMembership": "boolean",
    "direct_connect_trust": "boolean",
    "disable_domain_admins": "boolean",
    "domain_nested_group": "integer",
    "enable_rpc_enum_usergroup": "boolean",
    "enable_sync_time": "boolean",
    "encrypt_ad_ldap": "string"
  }
}
```

## SYNO.Core.Directory.Domain.Schedule

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Directory.Domain.Schedule`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "date_type": "integer"
  }
}
```

## SYNO.Core.Directory.Domain.Trust

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Directory.Domain.Trust`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

Confirmed present: DSM returned error 2624 rather than 103, so the method exists. What it additionally requires was not determined.
The exact signature was not determined; it is listed here so it is known to exist.

**Response:**

```json
{
  "success": false,
  "error": {
    "code": 2624
  }
}
```

#### Method: `list`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Directory.Domain.Trust`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID from `SYNO.API.Auth`

Confirmed present: DSM returned error 2624 rather than 103, so the method exists. What it additionally requires was not determined.
The exact signature was not determined; it is listed here so it is known to exist.

**Response:**

```json
{
  "success": false,
  "error": {
    "code": 2624
  }
}
```

## SYNO.Core.Directory.LDAP

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1–2

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Directory.LDAP`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "base_dn": "string",
    "enable_cifs": "boolean",
    "enable_cifs_kerberos": "boolean",
    "enable_cifs_pam": "boolean",
    "enable_client": "boolean",
    "enable_client_certificate": "boolean",
    "enable_idmap": "boolean",
    "encryption": "string",
    "error": "integer",
    "host": "string",
    "is_syno_server": "boolean",
    "ldap_schema": "string",
    "nested_group_level": "integer",
    "no_nested_group": "boolean",
    "profile": "string",
    "server_support_samba_schema": "boolean",
    "tls_reqcert": "boolean",
    "update_min": "integer"
  }
}
```

## SYNO.Core.Directory.LDAP.BaseDN

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1–2

#### Method: `list`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Directory.LDAP.BaseDN`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID from `SYNO.API.Auth`

Confirmed present: DSM returned error 2701 rather than 103, so the method exists. What it additionally requires was not determined.
The exact signature was not determined; it is listed here so it is known to exist.

**Response:**

```json
{
  "success": false,
  "error": {
    "code": 2701
  }
}
```

## SYNO.Core.Directory.LDAP.Profile

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1–2

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Directory.LDAP.Profile`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

Confirmed present: DSM returned error 2701 rather than 103, so the method exists. What it additionally requires was not determined.
The exact signature was not determined; it is listed here so it is known to exist.

**Response:**

```json
{
  "success": false,
  "error": {
    "code": 2701
  }
}
```

#### Method: `list`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Directory.LDAP.Profile`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "profiles": "array<string>"
  }
}
```

## SYNO.Core.Directory.OIDC.SSO

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Directory.OIDC.SSO`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "oidc_allow_local_user": "boolean",
    "oidc_authorization_endpoint": "string",
    "oidc_client_id": "string",
    "oidc_client_secret": "string",
    "oidc_name": "string",
    "oidc_redirect_uri": "string",
    "oidc_scope": "string",
    "oidc_token_endpoint": "string",
    "oidc_user_claim": "string",
    "oidc_wellknown": "string"
  }
}
```

## SYNO.Core.Directory.SSO

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1–2

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Directory.SSO`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "appid": "string",
    "enable_sso": "boolean",
    "host": "string",
    "pingpong": "null",
    "sso_default_login": "boolean"
  }
}
```

## SYNO.Core.Directory.SSO.CAS

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Directory.SSO.CAS`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "cas_allow_local_user": "boolean",
    "cas_auth_url": "string",
    "cas_name": "string",
    "cas_service_ids": "string",
    "cas_validate_url": "string",
    "sso_cas_enable": "string"
  }
}
```

## SYNO.Core.Directory.SSO.IWA

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Directory.SSO.IWA`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "enable_http_negotiate": "boolean"
  }
}
```

## SYNO.Core.Directory.SSO.Profile

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Directory.SSO.Profile`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "sso_enable": "boolean",
    "sso_profile": "string"
  }
}
```

#### Method: `list`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Directory.SSO.Profile`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "profiles": "array<string>"
  }
}
```

## SYNO.Core.Directory.SSO.SAML

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Directory.SSO.SAML`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "saml_allow_local_user": "boolean",
    "saml_cert_detail": "string",
    "saml_idp_entity_id": "string",
    "saml_idp_signin_url": "string",
    "saml_name": "string",
    "saml_response_signature": "string",
    "saml_system_date": "string",
    "saml_valid_date": "string",
    "sso_saml_enable": "string"
  }
}
```

## SYNO.Core.Directory.SSO.Setting

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Directory.SSO.Setting`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "sso_default_login": "boolean"
  }
}
```

## SYNO.Core.Directory.WebSphere.SSO

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Directory.WebSphere.SSO`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "websphere_client_id": "string",
    "websphere_client_secret": "string",
    "websphere_oidc_host": "string",
    "websphere_oidc_provider": "string",
    "websphere_redirect_uri": "string"
  }
}
```
