# Core · FileServ APIs (probed)

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

## SYNO.Core.FileServ.FTP

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1–3

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.FileServ.FTP`
- `version` (required): `3`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "custom_port": "string",
    "custom_port_range": "boolean",
    "enable_ascii": "boolean",
    "enable_fips": "boolean",
    "enable_flow_ctrl": "boolean",
    "enable_ftp": "boolean",
    "enable_ftps": "boolean",
    "enable_fxp": "boolean",
    "ext_ip": "string",
    "max_conn_per_ip": "integer",
    "maxdownloadrate": "integer",
    "maxuploadrate": "integer",
    "modify_time_std": "string",
    "portnum": "integer",
    "timeout": "integer",
    "use_ext_ip": "boolean",
    "utf8_mode": "integer"
  }
}
```

## SYNO.Core.FileServ.FTP.SFTP

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.FileServ.FTP.SFTP`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "enable": "boolean",
    "portnum": "integer"
  }
}
```

## SYNO.Core.FileServ.FTP.Security

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.FileServ.FTP.Security`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "anonymous": "boolean",
    "anonymous_chroot": "boolean",
    "anonymous_chroot_share": "string",
    "enable_umask": "boolean",
    "user_chroot": "boolean"
  }
}
```

## SYNO.Core.FileServ.NFS.AdvancedSetting

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.FileServ.NFS.AdvancedSetting`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "custom_port_enable": "integer",
    "nfs_v4_domain": "string",
    "nlm_port": "integer",
    "read_size": "integer",
    "statd_port": "integer",
    "unix_pri_enable": "boolean",
    "write_size": "integer"
  }
}
```

## SYNO.Core.FileServ.NFS.IDMap

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `list`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.FileServ.NFS.IDMap`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "idmap": "array<empty>",
    "total": "integer"
  }
}
```

## SYNO.Core.FileServ.NFS.Kerberos

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.FileServ.NFS.Kerberos`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "kerberos_principal": "string",
    "kerberos_support": "boolean"
  }
}
```

#### Method: `list`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.FileServ.NFS.Kerberos`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "keytab": "array<empty>"
  }
}
```

## SYNO.Core.FileServ.ReflinkCopy

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.FileServ.ReflinkCopy`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "reflink_copy_enable": "boolean"
  }
}
```

## SYNO.Core.FileServ.Rsync.Account

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `list`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.FileServ.Rsync.Account`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "account_list": "array<empty>"
  }
}
```

## SYNO.Core.FileServ.SMB.ConfBackup

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.FileServ.SMB.ConfBackup`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "db_items": [
      {
        "option": "string",
        "value": "integer"
      }
    ]
  }
}
```

## SYNO.Core.FileServ.SMB.MSDFS

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.FileServ.SMB.MSDFS`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "max_rules": "integer",
    "rules": "array<empty>"
  }
}
```

## SYNO.Core.FileServ.ServiceDiscovery

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.FileServ.ServiceDiscovery`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "enable_afp_time_machine": "boolean",
    "enable_smb_time_machine": "boolean",
    "time_machine_disable_shares": "array<empty>",
    "time_machine_shares": "array<empty>"
  }
}
```

## SYNO.Core.FileServ.ServiceDiscovery.WSTransfer

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.FileServ.ServiceDiscovery.WSTransfer`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "enable_wstransfer": "boolean"
  }
}
```
