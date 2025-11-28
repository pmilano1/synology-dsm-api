# Directory Server - Group Management

**Category:** Identity Management

[← Back to Directory Server](README.md)

---

**Endpoint:** `/webapi/entry.cgi`

---

## SYNO.DirectoryServer.Group

#### Method: `Create`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.DirectoryServer.Group`
- `version` (required): `1`
- `method` (required): `Create`
- `name` (required): Group name
- `description` (optional): Group description
- `ou` (optional): Organizational Unit DN
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "dn": "CN=Developers,OU=Groups,DC=example,DC=com"
  }
}
```

---

#### Method: `AddMember`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.DirectoryServer.Group`
- `version` (required): `1`
- `method` (required): `AddMember`
- `user_dn` (required): User Distinguished Name
- `group_dn` (required): Group Distinguished Name
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true
}
```

**Notes:**
- Adds user as member of group
- User must exist in directory
- Group must exist in directory

---

#### Method: `RemoveMember`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.DirectoryServer.Group`
- `version` (required): `1`
- `method` (required): `RemoveMember`
- `user_dn` (required): User Distinguished Name
- `group_dn` (required): Group Distinguished Name
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true
}
```

---

#### Method: `Delete`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.DirectoryServer.Group`
- `version` (required): `1`
- `method` (required): `Delete`
- `dn` (required): Group Distinguished Name
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true
}
```

**Notes:**
- Permanently deletes group from directory
- Cannot be undone
- Group members are not deleted
- Group permissions remain until manually removed
- Requires administrator privileges

