# Photos - Folders

**Category:** Media Management

[← Back to Photos](README.md)

---

**Endpoint:** `/webapi/entry.cgi`

---

## SYNO.Foto.Browse.Folder

#### Method: `list`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.Foto.Browse.Folder`
- `version` (required): `1`
- `method` (required): `list`
- `folder_id` (required): Parent folder ID (0 for root)
- `_sid` (required): Session ID
- `offset` (optional): Starting index (default: 0)
- `limit` (optional): Max results (default: 1000)
- `additional` (optional): Additional fields (comma-separated): `thumbnail`, `sharing_info`

**Response:**
```json
{
  "success": true,
  "data": {
    "list": [
      {
        "id": 123,
        "name": "Vacation 2024",
        "owner_user_id": 1,
        "parent": 0,
        "passphrase": "",
        "shared": false,
        "sort_by": "takentime",
        "sort_direction": "desc"
      }
    ]
  }
}
```

---

#### Method: `get`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.Foto.Browse.Folder`
- `version` (required): `1`
- `method` (required): `get`
- `id` (required): Folder ID
- `_sid` (required): Session ID
- `additional` (optional): Additional fields

**Response:**
```json
{
  "success": true,
  "data": {
    "folder": {
      "id": 123,
      "name": "Vacation 2024",
      "owner_user_id": 1,
      "parent": 0
    }
  }
}
```

---

#### Method: `count`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.Foto.Browse.Folder`
- `version` (required): `1`
- `method` (required): `count`
- `folder_id` (required): Parent folder ID
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "count": 15
  }
}
```

---

## SYNO.FotoTeam.Browse.Folder

#### Method: `list`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.FotoTeam.Browse.Folder`
- `version` (required): `1`
- `method` (required): `list`
- `folder_id` (required): Parent folder ID (0 for root)
- `_sid` (required): Session ID
- `offset` (optional): Starting index (default: 0)
- `limit` (optional): Max results (default: 2000)
- `additional` (optional): Additional fields

**Response:**
```json
{
  "success": true,
  "data": {
    "list": [
      {
        "id": 456,
        "name": "Company Events",
        "owner_user_id": 1,
        "parent": 0,
        "shared": true
      }
    ]
  }
}
```

**Notes:**
- Team Space folders are shared across team members
- Requires appropriate team permissions

