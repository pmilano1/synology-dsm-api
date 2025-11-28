# Virtual Machine Manager - Images

**Category:** Virtualization

[← Back to Virtual Machine Manager](README.md)

---

**Endpoint:** `/webapi/entry.cgi`

---

## SYNO.Virtualization.Image

#### Method: `List`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.Virtualization.Image`
- `version` (required): `1`
- `method` (required): `List`
- `offset` (optional): Starting index (default: 0)
- `limit` (optional): Max results (default: 100)
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "images": [
      {
        "image_id": "img-1",
        "image_name": "ubuntu-22.04-server.iso",
        "size": 1073741824,
        "type": "iso",
        "create_time": 1732788000
      }
    ],
    "total": 1
  }
}
```

**Response Fields:**

| Field | Type | Description |
|-------|------|-------------|
| `image_id` | string | Image ID |
| `image_name` | string | Image filename |
| `size` | integer | Image size (bytes) |
| `type` | string | Image type (`iso`, `vdisk`) |
| `create_time` | integer | Creation timestamp (Unix time) |

---

#### Method: `Create`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Virtualization.Image`
- `version` (required): `1`
- `method` (required): `Create`
- `auto_clean_task` (optional): Auto-clean task after completion (default: true)
- `guest_id` (optional): Source VM ID (for VM-to-image)
- `image_name` (required): Image filename
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true,
  "data": {
    "task_id": "task_126",
    "image_id": "img-2"
  }
}
```

**Notes:**
- Create image from existing VM using `guest_id`
- Image creation is asynchronous (use task_id to monitor)
- Images stored in designated image folder

---

#### Method: `Delete`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Virtualization.Image`
- `version` (required): `1`
- `method` (required): `Delete`
- `image_id` (optional): Image ID
- `image_name` (optional): Image filename
- `_sid` (required): Session ID

**Response:**
```json
{
  "success": true
}
```

**Notes:**
- Use either `image_id` or `image_name` parameter
- Cannot delete images in use by VMs
- ISO images can be uploaded via File Station

