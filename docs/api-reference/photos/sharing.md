# Photos - Sharing

**Category:** Media Management

[← Back to Photos](README.md)

---

**Endpoint:** `/photo/webapi/entry.cgi`

---

## SYNO.Foto.PublicSharing

#### Method: `get_ui_string`

**HTTP Method:** GET

**Auth Level:** 0 (No authentication needed)

**Description:** Get all text strings for user interface (UI) in Synology Photos. This endpoint returns localized strings used throughout the Photos application interface.

**Parameters:**
- `api` (required): `SYNO.Foto.PublicSharing`
- `version` (required): `1`
- `method` (required): `get_ui_string`

**Example Request:**
```
https://<IP_ADDRESS>/photo/webapi/entry.cgi?api=SYNO.Foto.PublicSharing&version=1&method=get_ui_string
```

**Response:**

The response contains a comprehensive object with UI strings organized by category. Below is a sample of the structure:

```json
{
  "success": true,
  "data": {
    "action": {
      "about": "About",
      "add": "Add",
      "add_photos": "Add Photos",
      "add_tag": "Add tags",
      "add_to_album": "Add to album",
      "add_to_favorite": "Add to favorites",
      "apply": "Save effects",
      "back": "Back",
      "browse": "Browse",
      "cancel": "Cancel",
      "create_album": "Create Album",
      "delete": "Delete",
      "download": "Download",
      "edit_permission": "Set share permissions",
      "share": "Share",
      "upload": "Upload Photos"
    },
    "app": {
      "album": "Albums",
      "all": "All",
      "favorite": "Favorites",
      "folder_view": "Folder View",
      "for_you": "For You",
      "moments_library": "My Photo Library",
      "person": "People",
      "personal_space": "Personal Space",
      "photo": "Photos",
      "shared": "Shared",
      "shared_space": "Shared Space",
      "sharing": "Sharing",
      "team_library": "Shared Photo Library",
      "timeline": "Timeline",
      "timeline_view": "Timeline View",
      "video": "Videos"
    },
    "permission": {
      "add_remove": "Add/Remove",
      "add_remove_hint": "View, download, add, and remove files",
      "download": "Download",
      "download_hint": "View, download, and copy files",
      "manage": "Manage",
      "manage_hint": "View, download, copy, upload, move, edit, delete files, and create folders",
      "privacy_private": "Private - Only invitees can access",
      "privacy_public_download": "Public - Anyone with the link can download",
      "privacy_public_upload": "Public - Anyone with the link can upload",
      "privacy_public_view": "Public - Anyone with the link can view",
      "upload": "Upload",
      "upload_hint": "View, download, copy, upload files, and create folders",
      "view": "View",
      "view_hint": "View files"
    },
    "sharing": {
      "album_link": "Album Link",
      "album_link_desc": "Share albums with others via link",
      "copy_link": "Copy Link",
      "create_link": "Create Link",
      "disable_link": "Disable Link",
      "enable_link": "Enable Link",
      "link_copied": "Link copied",
      "link_settings": "Link Settings",
      "password_protected": "Password Protected",
      "set_expiration": "Set Expiration",
      "share_album": "Share Album",
      "share_folder": "Share Folder",
      "share_link": "Share Link",
      "share_settings": "Share Settings",
      "shared_by_me": "Shared by Me",
      "shared_with_me": "Shared with Me"
    },
    "error": {
      "album_not_exist": "The album does not exist.",
      "album_permission_denied": "You do not have permission to access this album.",
      "file_permission_denied": "You do not have the permission to access Synology Photos.",
      "nopermission": "You are not authorized to use this service.",
      "timeout": "Connection expired. Please login again.",
      "unknown": "Unable to perform this operation because the network connection is unstable or the system is busy."
    }
  }
}
```

**Response Categories:**

The UI strings are organized into the following main categories:

| Category | Description |
|----------|-------------|
| `action` | Action buttons and commands (add, delete, download, share, etc.) |
| `app` | Application-level labels (albums, folders, timeline, etc.) |
| `permission` | Permission levels and descriptions |
| `sharing` | Sharing-related strings and settings |
| `error` | Error messages |
| `filter` | Filter options and descriptions |
| `search` | Search-related strings |
| `setting` | Settings page strings |
| `lightbox` | Photo viewer strings |
| `datetime` | Date and time formatting |
| `common` | Common UI elements |

**Use Cases:**

1. **Localization**: Get all UI strings for building custom interfaces
2. **Error Handling**: Reference error messages for user feedback
3. **Permission Display**: Show permission levels and descriptions
4. **Sharing UI**: Build custom sharing interfaces with proper labels

**Notes:**

- This endpoint does not require authentication
- The response contains over 1000 UI strings
- Strings are returned in the server's configured language
- Useful for building custom clients or integrations that need to match Synology Photos UI

---

## Additional Sharing Methods

The Synology Photos API includes additional sharing methods that may be documented in future updates:

- **Share Link Management**: Create, update, and delete share links for albums and folders
- **Permission Management**: Set and modify sharing permissions for users and groups
- **Public Sharing**: Configure public access settings for albums and folders
- **Share Link Settings**: Configure password protection, expiration dates, and access levels

For more information on these methods, refer to the official Synology DSM API documentation or explore the API using browser developer tools while using Synology Photos.

---

[← Back to Photos](README.md)

