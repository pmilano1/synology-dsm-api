# FileStation - Sharing APIs

[← Back to FileStation](README.md)

---

## SYNO.FileStation.Sharing - Get Link Info

Get information about a specific shared link.

**API:** `SYNO.FileStation.Sharing`  
**Version:** 3  
**Method:** `getinfo`

### Request Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | String | Yes | Shared link ID |

### Request

```http
GET /webapi/entry.cgi?api=SYNO.FileStation.Sharing&version=3&method=getinfo&id=SHARE_LINK_ID&_sid={sid}
```

### Response

```json
{
  "success": true,
  "data": {
    "links": [
      {
        "id": "SHARE_LINK_ID",
        "url": "https://nas.example.com/sharing/SHARE_LINK_ID",
        "link_owner": "admin",
        "path": "/docker/document.pdf",
        "date_expired": 0,
        "date_available": 0,
        "status": "valid",
        "has_password": false,
        "expire_times": 0,
        "access_time": 5,
        "isFolder": false
      }
    ]
  }
}
```

---

## SYNO.FileStation.Sharing - List Links

List all shared links created by the current user.

**API:** `SYNO.FileStation.Sharing`  
**Version:** 3  
**Method:** `list`

### Request Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `offset` | Integer | No | Starting index (default: 0) |
| `limit` | Integer | No | Max results (default: 0 = all) |
| `sort_by` | String | No | Sort field: `name`, `user`, `access_time`, `mtime`, `expire_time`, `status` |
| `sort_direction` | String | No | `asc` or `desc` (default: `asc`) |
| `force_clean` | Boolean | No | Clean invalid links before listing (default: false) |

### Request

```http
GET /webapi/entry.cgi?api=SYNO.FileStation.Sharing&version=3&method=list&_sid={sid}
```

### Response

```json
{
  "success": true,
  "data": {
    "total": 3,
    "offset": 0,
    "links": [
      {
        "id": "LINK_001",
        "url": "https://nas.example.com/sharing/LINK_001",
        "link_owner": "admin",
        "path": "/docker/README.md",
        "date_expired": 0,
        "date_available": 0,
        "status": "valid",
        "has_password": false,
        "expire_times": 0,
        "access_time": 12,
        "isFolder": false
      },
      {
        "id": "LINK_002",
        "url": "https://nas.example.com/sharing/LINK_002",
        "link_owner": "admin",
        "path": "/photos/vacation",
        "date_expired": 1735689600,
        "status": "valid",
        "has_password": true,
        "isFolder": true
      }
    ]
  }
}
```

---

## SYNO.FileStation.Sharing - Create Link

Create a new shared link for a file or folder.

**API:** `SYNO.FileStation.Sharing`  
**Version:** 3  
**Method:** `create`

### Request Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `path` | String | Yes | File or folder path to share |
| `password` | String | No | Password protection for the link |
| `date_expired` | Integer/String | No | Expiration date (Unix timestamp or `0` for never) |
| `date_available` | Integer/String | No | Available from date (Unix timestamp or `0` for immediate) |
| `expire_times` | Integer | No | Max number of accesses (0 = unlimited) |

### Request

```http
POST /webapi/entry.cgi
Content-Type: application/x-www-form-urlencoded

api=SYNO.FileStation.Sharing&version=3&method=create&path=/docker/document.pdf&_sid={sid}
```

### Request (With Password and Expiration)

```http
POST /webapi/entry.cgi
Content-Type: application/x-www-form-urlencoded

api=SYNO.FileStation.Sharing&version=3&method=create&path=/docker/document.pdf&password=SecurePass123&date_expired=1735689600&expire_times=10&_sid={sid}
```

### Response

```json
{
  "success": true,
  "data": {
    "links": [
      {
        "id": "NEW_LINK_ID",
        "url": "https://nas.example.com/sharing/NEW_LINK_ID",
        "link_owner": "admin",
        "path": "/docker/document.pdf",
        "date_expired": 1735689600,
        "date_available": 0,
        "status": "valid",
        "has_password": true,
        "expire_times": 10,
        "access_time": 0,
        "isFolder": false
      }
    ]
  }
}
```

---

## SYNO.FileStation.Sharing - Delete Link

Delete one or more shared links.

**API:** `SYNO.FileStation.Sharing`  
**Version:** 3  
**Method:** `delete`

### Request Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | String | Yes | Shared link ID (comma-separated for multiple) |

### Request (Single Link)

```http
POST /webapi/entry.cgi
Content-Type: application/x-www-form-urlencoded

api=SYNO.FileStation.Sharing&version=3&method=delete&id=LINK_ID&_sid={sid}
```

### Request (Multiple Links)

```http
POST /webapi/entry.cgi
Content-Type: application/x-www-form-urlencoded

api=SYNO.FileStation.Sharing&version=3&method=delete&id=LINK_001,LINK_002,LINK_003&_sid={sid}
```

### Response

```json
{
  "success": true
}
```

---

## SYNO.FileStation.Sharing - Clear Invalid Links

Remove all invalid or expired shared links.

**API:** `SYNO.FileStation.Sharing`  
**Version:** 3  
**Method:** `clear_invalid`

### Request

```http
POST /webapi/entry.cgi
Content-Type: application/x-www-form-urlencoded

api=SYNO.FileStation.Sharing&version=3&method=clear_invalid&_sid={sid}
```

### Response

```json
{
  "success": true
}
```

---

## SYNO.FileStation.Sharing - Edit Link

Edit an existing shared link's properties.

**API:** `SYNO.FileStation.Sharing`  
**Version:** 3  
**Method:** `edit`

### Request Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | String | Yes | Shared link ID |
| `password` | String | No | New password (empty string to remove) |
| `date_expired` | Integer/String | No | New expiration date (Unix timestamp or `0` for never) |
| `date_available` | Integer/String | No | New available from date |
| `expire_times` | Integer | No | New max accesses (0 = unlimited) |

### Request

```http
POST /webapi/entry.cgi
Content-Type: application/x-www-form-urlencoded

api=SYNO.FileStation.Sharing&version=3&method=edit&id=LINK_ID&password=NewPassword&date_expired=1767225600&_sid={sid}
```

### Response

```json
{
  "success": true,
  "data": {
    "links": [
      {
        "id": "LINK_ID",
        "url": "https://nas.example.com/sharing/LINK_ID",
        "link_owner": "admin",
        "path": "/docker/document.pdf",
        "date_expired": 1767225600,
        "has_password": true
      }
    ]
  }
}
```

