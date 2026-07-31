# DSM Core - Terminal

**Category:** System Management

[← Back to DSM Core](README.md)

---

**Endpoint:** `/webapi/entry.cgi`

Controls the SSH and Telnet services, and the cipher/KEX/MAC suites SSH offers.

Useful diagnostically: when key-based SSH fails, this API distinguishes "the service is
off" from "the service is on and the key is being refused". Note that a rejected key is
often not about the key at all — if [User Home](users.md#syno-core-user-home) is
disabled there is no `/var/services/homes/<user>`, so there is nowhere for
`~/.ssh/authorized_keys` to live and public-key auth cannot work for **any** account.
The giveaway is `Could not chdir to home directory` on an otherwise successful password
login.

---

## SYNO.Core.Terminal

#### Method: `get`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.Core.Terminal`
- `version` (required): `3`
- `method` (required): `get`
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "enable_ssh": true,
    "enable_telnet": false,
    "forbid_console": false,
    "ssh_port": 22,
    "ssh_cipher": [
      {
        "name": "aes256-ctr",
        "in_use": true,
        "security_level": 2,
        "hardware_support": false
      }
    ],
    "ssh_kex": [
      { "name": "curve25519-sha256", "in_use": true, "security_level": 2 }
    ],
    "ssh_mac": [
      { "name": "hmac-sha2-512-etm@openssh.com", "in_use": true, "security_level": 2 }
    ]
  }
}
```

**Notes:**
- `enable_ssh` and `ssh_port` are the fields that answer "is SSH reachable" — check them
  before assuming a connection problem is a key problem.
- `ssh_cipher` / `ssh_kex` / `ssh_mac` are arrays of objects, each with `in_use` and a
  `security_level` (`0` weak, `1` medium, `2` strong). DSM ships several
  `security_level: 0` algorithms enabled by default (`3des-cbc`, `hmac-md5`,
  `diffie-hellman-group1-sha1`), so an audit that only checks `enable_ssh` will miss
  them.
- `maxVersion` is **3** on DSM 7.x; this is the only `*Terminal*` API the platform
  exposes.
