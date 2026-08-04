# Core · Hardware APIs (probed)

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

## SYNO.Core.Hardware.BeepControl

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Hardware.BeepControl`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "enc_module_fail": "boolean",
    "eunit_redundant_power_fail": "boolean",
    "fan_fail": "boolean",
    "poweroff_beep": "boolean",
    "poweron_beep": "boolean",
    "redundant_power_fail": "boolean",
    "reset_beep": "boolean",
    "sas_link_fail": "boolean",
    "support_fan_fail": "boolean",
    "support_poweroff_beep": "boolean",
    "support_poweron_beep": "boolean",
    "support_redundant_power_fail": "boolean",
    "support_reset_beep": "boolean",
    "support_volume_or_cache_crash": "boolean",
    "volume_or_cache_crash": "boolean"
  }
}
```

## SYNO.Core.Hardware.FanSpeed

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Hardware.FanSpeed`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "all_disk_temp_fail": "string",
    "cool_fan": "string",
    "dual_fan_speed": "string",
    "fan_support_adjust_by_ext_nic": "string",
    "fan_type": "integer"
  }
}
```

## SYNO.Core.Hardware.Hibernation

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Hardware.Hibernation`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "auto_poweroff_enable": "boolean",
    "enable_log": "boolean",
    "eunit_deep_sleep": "integer",
    "eunit_dsleep_blacklist": "string",
    "hibernation_blacklist": "string",
    "ignore_netbios_broadcast": "boolean",
    "internal_hd_idletime": "integer",
    "sata_deep_sleep": "integer",
    "sata_dsleep_blacklist": "string",
    "support_esata": "string",
    "support_eunit_deep_sleep": "boolean",
    "support_eunit_switch_mode": "boolean",
    "usb_idletime": "integer"
  }
}
```

## SYNO.Core.Hardware.LCM

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Hardware.LCM`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {}
}
```

## SYNO.Core.Hardware.Led.Brightness

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Hardware.Led.Brightness`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "led_brightness": "integer",
    "schedule": "string"
  }
}
```

## SYNO.Core.Hardware.MemoryLayout

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Hardware.MemoryLayout`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {}
}
```

## SYNO.Core.Hardware.OOBManagement

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Hardware.OOBManagement`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

Confirmed present: DSM returned error 3794 rather than 103, so the method exists. What it additionally requires was not determined.
The exact signature was not determined; it is listed here so it is known to exist.

**Response:**

```json
{
  "success": false,
  "error": {
    "code": 3794
  }
}
```

## SYNO.Core.Hardware.PowerRecovery

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Hardware.PowerRecovery`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "internal_lan_num": "integer",
    "rc_power_config": "boolean",
    "wol": [
      {
        "enable": "boolean",
        "idx": "integer"
      }
    ],
    "wol1": "boolean",
    "wol2": "boolean"
  }
}
```

## SYNO.Core.Hardware.SpectreMeltdown

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Hardware.SpectreMeltdown`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "enable_spectre_meltdown_mitigation": "boolean"
  }
}
```

## SYNO.Core.Hardware.VideoTranscoding

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Hardware.VideoTranscoding`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {}
}
```

## SYNO.Core.Hardware.ZRAM

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Hardware.ZRAM`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "enable_zram": "boolean"
  }
}
```
