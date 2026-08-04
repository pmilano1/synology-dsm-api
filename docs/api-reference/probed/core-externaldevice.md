# Core · ExternalDevice APIs (probed)

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

## SYNO.Core.ExternalDevice.Bluetooth

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1–2

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.ExternalDevice.Bluetooth`
- `version` (required): `2`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

Confirmed present: DSM returned error 111 rather than 103, so the method exists. What it additionally requires was not determined.
The exact signature was not determined; it is listed here so it is known to exist.

**Response:**

```json
{
  "success": false,
  "error": {
    "code": 111
  }
}
```

#### Method: `list`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.ExternalDevice.Bluetooth`
- `version` (required): `2`
- `method` (required): `list`
- `_sid` (required): Session ID from `SYNO.API.Auth`

Confirmed present: DSM returned error 111 rather than 103, so the method exists. What it additionally requires was not determined.
The exact signature was not determined; it is listed here so it is known to exist.

**Response:**

```json
{
  "success": false,
  "error": {
    "code": 111
  }
}
```

## SYNO.Core.ExternalDevice.Bluetooth.Settings

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.ExternalDevice.Bluetooth.Settings`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

Confirmed present: DSM returned error 111 rather than 103, so the method exists. What it additionally requires was not determined.
The exact signature was not determined; it is listed here so it is known to exist.

**Response:**

```json
{
  "success": false,
  "error": {
    "code": 111
  }
}
```

## SYNO.Core.ExternalDevice.DefaultPermission

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.ExternalDevice.DefaultPermission`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

Confirmed present: DSM returned error 403 rather than 103, so the method exists. What it additionally requires was not determined.
The exact signature was not determined; it is listed here so it is known to exist.

**Response:**

```json
{
  "success": false,
  "error": {
    "code": 403
  }
}
```

## SYNO.Core.ExternalDevice.Printer

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `list`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.ExternalDevice.Printer`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "printers": "array<empty>"
  }
}
```

## SYNO.Core.ExternalDevice.Printer.BonjourSharing

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.ExternalDevice.Printer.BonjourSharing`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "enable_bonjour_support": "boolean"
  }
}
```

## SYNO.Core.ExternalDevice.Printer.Driver

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `list`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.ExternalDevice.Printer.Driver`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "Apollo": "array<array<string>>",
    "Apple": "array<array<string>>",
    "Brother": "array<array<string>>",
    "Canon": "array<array<string>>",
    "Citizen": "array<array<string>>",
    "Compaq": "array<array<string>>",
    "DEC": "array<array<string>>",
    "DNP": "array<array<string>>",
    "Epson": "array<array<string>>",
    "Fujifilm": "array<array<string>>",
    "Fujitsu": "array<array<string>>",
    "Generic": "array<array<string>>",
    "Gestetner": "array<array<string>>",
    "HP": "array<array<string>>",
    "IBM": "array<array<string>>",
    "Infotec": "array<array<string>>",
    "Kodak": "array<array<string>>",
    "Kyocera": "array<array<string>>",
    "Lanier": "array<array<string>>",
    "Lexmark": "array<array<string>>",
    "Minolta": "array<array<string>>",
    "Mitsubishi": "array<array<string>>",
    "NEC": "array<array<string>>",
    "NRG": "array<array<string>>",
    "Oki": "array<array<string>>",
    "Olivetti": "array<array<string>>",
    "Olympus": "array<array<string>>",
    "PCPI": "array<array<string>>",
    "Panasonic": "array<array<string>>",
    "Raven": "array<array<string>>",
    "Ricoh": "array<array<string>>",
    "Samsung": "array<array<string>>",
    "Savin": "array<array<string>>",
    "Seiko": "array<array<string>>",
    "Sharp": "array<array<string>>",
    "Shinko": "array<array<string>>",
    "Sinfonia": "array<array<string>>",
    "Sony": "array<array<string>>",
    "Star": "array<array<string>>",
    "Tally": "array<array<string>>",
    "Tektronix": "array<array<string>>",
    "Xerox": "array<array<string>>"
  }
}
```

## SYNO.Core.ExternalDevice.Printer.Network

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.ExternalDevice.Printer.Network`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

Confirmed present: DSM returned error 3600 rather than 103, so the method exists. What it additionally requires was not determined.
The exact signature was not determined; it is listed here so it is known to exist.

**Response:**

```json
{
  "success": false,
  "error": {
    "code": 3600
  }
}
```

## SYNO.Core.ExternalDevice.Printer.Network.Host

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.ExternalDevice.Printer.Network.Host`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

Confirmed present: DSM returned error 3600 rather than 103, so the method exists. What it additionally requires was not determined.
The exact signature was not determined; it is listed here so it is known to exist.

**Response:**

```json
{
  "success": false,
  "error": {
    "code": 3600
  }
}
```

## SYNO.Core.ExternalDevice.Printer.OAuth

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.ExternalDevice.Printer.OAuth`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "OAuth": "boolean",
    "account": "string"
  }
}
```

## SYNO.Core.ExternalDevice.Printer.USB

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.ExternalDevice.Printer.USB`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

Confirmed present: DSM returned error 3600 rather than 103, so the method exists. What it additionally requires was not determined.
The exact signature was not determined; it is listed here so it is known to exist.

**Response:**

```json
{
  "success": false,
  "error": {
    "code": 3600
  }
}
```

## SYNO.Core.ExternalDevice.Storage.EUnit

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `list`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.ExternalDevice.Storage.EUnit`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "devices": "array<empty>"
  }
}
```

## SYNO.Core.ExternalDevice.Storage.Setting

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.ExternalDevice.Storage.Setting`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "delalloc": "boolean",
    "forbid_usb": "boolean",
    "needReboot": "boolean",
    "non_admin_eject": "boolean",
    "setting": "boolean",
    "support_exfat_mkfs": "string"
  }
}
```

## SYNO.Core.ExternalDevice.Storage.USB

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `list`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.ExternalDevice.Storage.USB`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "devices": "array<empty>"
  }
}
```

## SYNO.Core.ExternalDevice.Storage.eSATA

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `list`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.ExternalDevice.Storage.eSATA`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "devices": "array<empty>"
  }
}
```

## SYNO.Core.ExternalDevice.UPS

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.ExternalDevice.UPS`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "ACL_enable": "boolean",
    "ACL_list": "array<empty>",
    "charge": "integer",
    "delay_time": "integer",
    "enable": "boolean",
    "manufacture": "string",
    "mode": "string",
    "model": "string",
    "net_server_ip": "string",
    "runtime": "integer",
    "shutdown_device": "boolean",
    "snmp_auth": "boolean",
    "snmp_auth_key": "boolean",
    "snmp_auth_type": "string",
    "snmp_community": "string",
    "snmp_mib": "string",
    "snmp_privacy": "boolean",
    "snmp_privacy_key": "boolean",
    "snmp_privacy_type": "string",
    "snmp_server_ip": "string",
    "snmp_user": "string",
    "snmp_version": "string",
    "status": "string",
    "usb_ups_connect": "boolean"
  }
}
```
