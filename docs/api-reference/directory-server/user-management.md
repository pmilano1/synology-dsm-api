# Directory Server - User Management

**Category:** Identity Management

[← Back to Directory Server](README.md)

---

**Endpoint:** `/webapi/entry.cgi`

---

## SYNO.DirectoryServer.User

#### Method: `Create`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.DirectoryServer.User`
- `version` (required): `1`
- `method` (required): `Create`
- `logon_name` (required): User logon name
- `password` (required): User password
- `first_name` (optional): First name
- `last_name` (optional): Last name
- `email` (optional): Email address
- `ou` (optional): Organizational Unit DN
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "dn": "CN=John Doe,OU=Users,DC=example,DC=com"
  }
}
```

---

#### Method: `ResetPassword`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.DirectoryServer.User`
- `version` (required): `1`
- `method` (required): `ResetPassword`
- `username` (required): Username
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "new_password": "TempPass123!"
  }
}
```

**Notes:**
- Generates random temporary password
- User must change password on next login
- Requires administrator privileges

---

#### Method: `ChangePassword`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.DirectoryServer.User`
- `version` (required): `1`
- `method` (required): `ChangePassword`
- `user_dn` (required): User Distinguished Name
- `password` (required): New password
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true
}
```

---

#### Method: `Modify`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.DirectoryServer.User`
- `version` (required): `1`
- `method` (required): `Modify`
- `user_dn` (required): User Distinguished Name
- `first_name` (optional): New first name
- `last_name` (optional): New last name
- `email` (optional): New email address
- `description` (optional): User description
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
- `api` (required): `SYNO.DirectoryServer.User`
- `version` (required): `1`
- `method` (required): `Delete`
- `dn` (required): User Distinguished Name
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true
}
```

**Notes:**
- Permanently deletes user from directory
- Cannot be undone
- User's files and permissions remain until manually removed
- Requires administrator privileges

