# SYNO.ActiveBackup.Share

**Category:** System

[← Back to API Reference](../README.md)

---


**Endpoint:** `entry.cgi`
**Versions:** 1-2


#### Method: `check_file`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Share`
- `version` (required): `1`
- `method` (required): `check_file`
- `_sid` (required): Session ID from login

**Response:**
```json
{
  "data": {
    "error_files": []
  },
  "success": true
}
```


#### Method: `create_fs_dir`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Share`
- `version` (required): `1`
- `method` (required): `create_fs_dir`
- `paths` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `paths`
- Error code 120 when parameter missing


#### Method: `list`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Share`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID from login

**Response:**
```json
{
  "data": {
    "default_share": "ActiveBackupforBusiness",
    "shares": [
      {
        "acl_permission": true,
        "available": true,
        "compress": false,
        "cow": false,
        "delegated": false,
        "free_space": 10401845899264,
        "name": "ActiveBackupforBusiness",
        "not_support_new_vesion": false,
        "path": "/volume1/ActiveBackupforBusiness",
        "readonly": false,
        "relinkable": false,
        "share_type": "",
        "storage_automount": true,
        "storage_compress_algorithm": 0,
        "storage_encrypt_algorithm": 0,
        "storage_id": 1,
        "storage_mounted": true,
        "type": "btrfs",
        "volume_no_space": false
      }
    ]
  },
  "success": true
}
```


#### Method: `list_encrypted`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Share`
- `version` (required): `1`
- `method` (required): `list_encrypted`
- `_sid` (required): Session ID from login

**Response:**
```json
{
  "data": {
    "shares": []
  },
  "success": true
}
```


#### Method: `list_file`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Share`
- `version` (required): `1`
- `method` (required): `list_file`
- `root_path` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `root_path`
- Error code 120 when parameter missing


#### Method: `list_storage`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Share`
- `version` (required): `1`
- `method` (required): `list_storage`
- `_sid` (required): Session ID from login

**Response:**
```json
{
  "data": {
    "storages": [
      {
        "automount_iv": "",
        "automount_location": "",
        "backup_tasks": [],
        "compacting": false,
        "compacting_percentage": 0,
        "compressed_size": 0,
        "dedup_size": 9121643806720,
        "delete_tasks": [],
        "delete_versions": [],
        "device_count": 4,
        "device_info": {
          "agentless_count": 0,
          "agentless_size": 0,
          "dsm_count": 0,
          "dsm_size": 0,
          "pc_count": 4,
          "pc_size": 20039709263360,
          "server_count": 0,
          "server_size": 0,
          "vm_count": 0,
          "vm_size": 0
        },
        "fs_name": "btrfs",
        "fs_type": 3,
        "mounted": true,
        "relink_state": {
          "alive": false,
          "error": {
            "code": 0
          },
          "owner": true,
          "state": 0
        },
        "repo_dir": "@ActiveBackup",
        "share_name": "ActiveBackupforBusiness",
        "share_type": "",
        "storage_compress_algorithm": 0,
        "storage_encrypt_algorithm": 0,
        "storage_id": 1,
        "vol_name": "Volume 1",
        "volume_path": "/volume1"
      }
    ]
  },
  "success": true
}
```

**Notes:**
- May take longer to respond


#### Method: `list_volume`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Share`
- `version` (required): `1`
- `method` (required): `list_volume`
- `_sid` (required): Session ID from login

**Response:**
```json
{
  "data": {
    "volumes": [
      {
        "total_bytes": "23030223990784",
        "used_bytes": "12628378091520",
        "volume_path": "/volume1"
      }
    ]
  },
  "success": true
}
```

**Notes:**
- May take longer to respond


#### Method: `relink`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Share`
- `version` (required): `1`
- `method` (required): `relink`
- `share_name` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `share_name`
- Error code 120 when parameter missing


#### Method: `remove`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Share`
- `version` (required): `1`
- `method` (required): `remove`
- `is_remove_data` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `is_remove_data`
- Error code 120 when parameter missing


---
