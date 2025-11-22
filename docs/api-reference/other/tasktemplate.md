# SYNO.ActiveBackup.TaskTemplate

**Category:** Other

[← Back to API Reference](../README.md)

---


**Endpoint:** `entry.cgi`
**Versions:** 1-2


#### Method: `create`


#### Method: `list`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.TaskTemplate`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID from login

**Response:**
```json
{
  "data": {
    "success": true,
    "template_list": [
      {
        "available": true,
        "backup_cache_content": {
          "cached_enabled": false
        },
        "backup_external": true,
        "backup_type": 2,
        "bandwidth": 0,
        "bandwidth_content": {
          "enable": false
        },
        "compress": false,
        "custom_volume": null,
        "enable_app_aware_bkp": false,
        "enable_compress_transfer": true,
        "enable_encrypt_transfer": true,
        "enable_notify": false,
        "enable_shutdown_after_complete": false,
        "enable_verification": false,
        "enable_wake_up": false,
        "enable_windows_working_state": false,
        "groups": [
          101
        ],
        "groups_name": [
          "administrators"
        ],
        "instant_backup": false,
        "is_default": true,
        "plan_uuid": "",
        "platform_type": 1,
        "pre_post_script_setting": null,
        "priority_order": 1,
        "relinkable": false,
        "retention_policy": {
          "gfs_days": 0,
          "gfs_months": 0,
          "gfs_weeks": 0,
          "gfs_years": 0,
          "keep_all": true,
          "keep_days": 0,
          "keep_versions": 0
        },
        "sched_content": {
          "repeat_type": "Weekly",
          "run_hour": 3,
          "run_min": 0,
          "run_weekday": [
            1
          ],
          "schedule_setting_type": 1
        },
        "share_name": "ActiveBackupforBusiness",
        "source_type": 1,
        "storage_compress_algorithm": 0,
        "storage_encrypt_algorithm": 0,
        "target_errorcode": 0,
        "target_id": 0,
        "target_name": "*",
        "target_type": 2,
        "template_id": 1,
        "template_name": "Default",
        "template_uuid": "",
        "unavailable_groups_count": 0,
        "unavailable_users_count": 0,
        "users": [
          1024
        ],
        "users_name": [
          "admin"
        ],
        "verification_policy": 120
      }
    ],
    "total": 5
  },
  "success": true
}
```


#### Method: `remove`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.TaskTemplate`
- `version` (required): `1`
- `method` (required): `remove`
- `template_ids` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `template_ids`
- Error code 120 when parameter missing


#### Method: `set`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.TaskTemplate`
- `version` (required): `1`
- `method` (required): `set`
- `_sid` (required): Session ID from login

**Response:**
```json
{
  "success": true
}
```


#### Method: `set_priority`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.TaskTemplate`
- `version` (required): `1`
- `method` (required): `set_priority`
- `_sid` (required): Session ID from login

**Response:**
```json
{
  "success": true
}
```


#### Method: `translate_target_id`


---
