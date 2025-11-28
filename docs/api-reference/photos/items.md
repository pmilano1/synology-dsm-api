# Photos - Items

**Category:** Media Management

[← Back to Photos](README.md)

---

**Endpoint:** `/photo/webapi/entry.cgi`

---

## SYNO.Foto.Browse.Item

#### Method: `list`

**HTTP Method:** GET

**Auth Level:** 1 (Authentication required)

**Description:** List all items (photos and videos) in folders in Personal Space.

**Parameters:**
- `api` (required): `SYNO.Foto.Browse.Item`
- `version` (required): `1`
- `method` (required): `list`
- `offset` (required): Number of items to skip before beginning to return results (default: 0)
- `limit` (required): Number of items requested. 0 lists all items (default: 0)
- `folder_id` (optional): ID of folder to list items from
- `sort_by` (optional): Field to sort on (only works when `folder_id` is given)
  - `filename`: File name
  - `filesize`: File size
  - `takentime`: Time of taking image
  - `item_type`: Type of the item
- `sort_direction` (optional): Sort order (only works when `folder_id` is given)
  - `asc`: Sort ascending
  - `desc`: Sort descending (default)
- `type` (optional): Type of data to filter
  - `photo`: Photos only
  - `video`: Videos only
  - `live`: iPhone live photos only
- `passphrase` (optional): Passphrase for a shared album (e.g., `xXHXZxIov`). Only items of this album will be listed.
- `additional` (optional): Get additional information about items (JSON array format)
  - `thumbnail`: Available thumbnail sizes (`sm`, `m`, `xl`)
  - `resolution`: Returns `height` and `width` of original photo
  - `orientation`: Orientation of file (integer value)
  - `video_convert`: Video conversion status
  - `video_meta`: Video metadata
  - `provider_user_id`: Provider user ID
  - `exif`: EXIF data (`aperture`, `camera`, `exposure_time`, `focal_length`, `iso`, `lens`)
  - `tag`: Returns tag objects with `id` and `name`
  - `description`: EXIF description
  - `gps`: GPS coordinates (`latitude`, `longitude`)
  - `geocoding_id`: Geocoding ID for internal database
  - `address`: Address calculated from GPS coordinates
  - `person`: Person objects for tagged people

**Example Request:**
```
https://<IP_ADDRESS>/photo/webapi/entry.cgi?api=SYNO.Foto.Browse.Item&version=1&method=list&offset=0&limit=100&folder_id=1989&additional=["thumbnail","resolution","orientation","exif","tag","description","gps","address","person"]
```

**Response:**
```json
{
  "data": {
    "list": [
      {
        "filename": "IMG_20210723_201314.JPG",
        "filesize": 13078975,
        "folder_id": 1989,
        "id": 80716,
        "indexed_time": 1633867030761,
        "owner_user_id": 2,
        "time": 1627071194,
        "type": "photo",
        "additional": {
          "orientation": 1,
          "orientation_original": 1,
          "resolution": {
            "height": 4000,
            "width": 6000
          },
          "thumbnail": {
            "cache_key": "80716_1633859830",
            "m": "ready",
            "preview": "broken",
            "sm": "ready",
            "unit_id": 80716,
            "xl": "ready"
          },
          "exif": {
            "aperture": "f/1.8",
            "camera": "Google Pixel 5",
            "exposure_time": "1/120",
            "focal_length": "4.44mm",
            "iso": 100,
            "lens": "Google Pixel 5 back camera"
          },
          "gps": {
            "latitude": 37.7749,
            "longitude": -122.4194
          },
          "address": {
            "city": "San Francisco",
            "country": "United States",
            "state": "California"
          }
        }
      }
    ]
  },
  "success": true
}
```

**Response Fields:**

| Field | Type | Description |
|-------|------|-------------|
| `filename` | String | Name of file |
| `filesize` | Integer | Size of file in bytes |
| `folder_id` | Integer | ID of parent folder |
| `id` | Integer | Unique ID of file |
| `indexed_time` | Integer | Linux timestamp (milliseconds) of when file was indexed |
| `live_type` | String | Type for iPhone live photos (e.g., "photo") |
| `owner_user_id` | Integer | User ID of owner |
| `time` | Integer | Linux timestamp (seconds) of file creation |
| `type` | String | Type of item: `photo`, `video`, or `live` |

**Additional Fields (when requested):**

| Field | Type | Description |
|-------|------|-------------|
| `orientation` | Integer | Current orientation |
| `orientation_original` | Integer | Original orientation |
| `resolution` | Object | Height and width of original photo |
| `thumbnail` | Object | Thumbnail data with cache_key, preview, sm, m, xl sizes |
| `exif` | Object | EXIF data (aperture, camera, exposure_time, focal_length, iso, lens) |
| `tag` | Array | Tag objects with id and name |
| `description` | String | EXIF description |
| `gps` | Object | GPS coordinates (latitude, longitude) |
| `geocoding_id` | Integer | Internal geocoding database ID |
| `address` | Object | Address components (city, country, state, etc.) |
| `person` | Array | Person objects for tagged people |

---

[← Back to Photos](README.md)

