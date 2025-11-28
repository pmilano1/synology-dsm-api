# Photos - Albums

**Category:** Media Management

[← Back to Photos](README.md)

---

**Endpoint:** `/webapi/entry.cgi`

---

## SYNO.Foto.Browse.Album

#### Method: `list`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.Foto.Browse.Album`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID
- `offset` (optional): Starting index (default: 0)
- `limit` (optional): Max results (default: 100)
- `sort_by` (optional): Sort field (`album_name`, `create_time`)
- `sort_direction` (optional): `asc` or `desc`

**Response:**
```json
{
  "success": true,
  "data": {
    "list": [
      {
        "id": "album_123",
        "name": "Best Photos 2024",
        "create_time": 1732752000,
        "item_count": 50,
        "shared": false,
        "type": "normal"
      }
    ]
  }
}
```

---

#### Method: `get`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.Foto.Browse.Album`
- `version` (required): `1`
- `method` (required): `get`
- `id` (required): Album ID
- `_sid` (required): Session ID
- `additional` (optional): Additional fields: `sharing_info`, `thumbnail`

**Response:**
```json
{
  "success": true,
  "data": {
    "album": {
      "id": "album_123",
      "name": "Best Photos 2024",
      "create_time": 1732752000,
      "item_count": 50,
      "condition": []
    }
  }
}
```

---

#### Method: `create`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Foto.Browse.Album`
- `version` (required): `1`
- `method` (required): `create`
- `name` (required): Album name
- `_sid` (required): Session ID
- `condition` (optional): Album condition (JSON array)

**Response:**
```json
{
  "success": true,
  "data": {
    "id": "album_124"
  }
}
```

---

#### Method: `delete`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Foto.Browse.Album`
- `version` (required): `1`
- `method` (required): `delete`
- `id` (required): Album ID (comma-separated for multiple)
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true
}
```

---

## SYNO.Foto.Browse.Item

#### Method: `list`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.Foto.Browse.Item`
- `version` (required): `1`
- `method` (required): `list`
- `folder_id` (optional): Folder ID
- `album_id` (optional): Album ID
- `_sid` (required): Session ID
- `offset` (optional): Starting index (default: 0)
- `limit` (optional): Max results (default: 100)
- `sort_by` (optional): Sort field (`filename`, `takentime`, `filesize`)
- `sort_direction` (optional): `asc` or `desc`
- `type` (optional): Item type (`photo`, `video`)
- `additional` (optional): Additional fields: `thumbnail`, `resolution`, `orientation`, `video_convert`, `video_meta`

**Response:**
```json
{
  "success": true,
  "data": {
    "list": [
      {
        "id": 12345,
        "filename": "IMG_0001.jpg",
        "filesize": 2097152,
        "folder_id": 123,
        "indexed_time": 1732752000,
        "owner_user_id": 1,
        "time": 1732752000,
        "type": "photo",
        "additional": {
          "thumbnail": {
            "cache_key": "12345_1732752000",
            "m": "ready",
            "xl": "ready"
          },
          "resolution": {
            "width": 4032,
            "height": 3024
          }
        }
      }
    ]
  }
}
```

---

## SYNO.Foto.Sharing.Passphrase

#### Method: `create`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Foto.Sharing.Passphrase`
- `version` (required): `1`
- `method` (required): `create`
- `id` (required): Album or folder ID
- `_sid` (required): Session ID
- `enabled` (optional): Enable sharing (default: true)
- `permission` (optional): Permission level
- `expiration` (optional): Expiration timestamp (0 = never)

**Response:**
```json
{
  "success": true,
  "data": {
    "passphrase": "abc123xyz",
    "sharing_link": "https://photos.example.com/mo/sharing/abc123xyz"
  }
}
```

