# SYNO.ActiveBackup.Task

**Category:** Core

[← Back to API Reference](../README.md)

---


**Endpoint:** `entry.cgi`
**Versions:** 1-2


#### Method: `backup`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Task`
- `version` (required): `1`
- `method` (required): `backup`
- `task_ids` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `task_ids`
- Error code 120 when parameter missing


#### Method: `cancel`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Task`
- `version` (required): `1`
- `method` (required): `cancel`
- `task_ids` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `task_ids`
- Error code 120 when parameter missing


#### Method: `cancel_waiting_backup`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Task`
- `version` (required): `1`
- `method` (required): `cancel_waiting_backup`
- `_sid` (required): Session ID from login

**Response:**
```json
{
  "success": true
}
```

**Notes:**
- Does not use socket connection


#### Method: `create_agent`


#### Method: `create_agentless`


#### Method: `create_vm`


#### Method: `create_vm_check`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Task`
- `version` (required): `1`
- `method` (required): `create_vm_check`
- `_sid` (required): Session ID from login

**Response:**
```json
{
  "data": {
    "aem_check_list": [],
    "check_list": []
  },
  "success": true
}
```


#### Method: `get_default_task_name`

**HTTP Method:** GET or POST

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Task`
- `version` (required): `1`
- `method` (required): `get_default_task_name`
- `backup_type` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `backup_type`
- Error code 120 when parameter missing


#### Method: `list`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Task`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID from login

**Response:**
```json
{
  "data": {
    "has_devices": false,
    "has_dsm_agent": false,
    "has_hyperv_inventories": false,
    "has_linux_agent": false,
    "has_mac_agent": false,
    "has_vmware_inventories": false,
    "has_windows_agent": false,
    "tasks": [
      {
        "agentless_backup_path": "",
        "agentless_backup_policy": 0,
        "agentless_enable_block_transfer": false,
        "agentless_enable_dedup": false,
        "agentless_enable_windows_vss": false,
        "allow_manual_backup": true,
        "backup_cache_content": {
          "cached_enabled": false
        },
        "backup_external": true,
        "backup_type": 2,
        "bandwidth": 0,
        "bandwidth_content": {
          "backup_bandwidth_base": 0,
          "backup_bandwidth_number": 0,
          "enable": false
        },
        "cbt_enable_mode": 1,
        "connection_timeout": 0,
        "custom_volume": [
          "C:"
        ],
        "custom_volume_alias": null,
        "datastore_reserved_percentage": 0,
        "deactivate_by_plan": false,
        "dedup_api_restore": false,
        "dedup_path": "",
        "device_count": 1,
        "devices": [
          {
            "agent_token": "REDACTED",
            "agentless_auth_policy": 0,
            "auto_discovery": false,
            "backup_type": 2,
            "create_time": 1594735305,
            "device_id": 1,
            "device_uuid": "37E1E2FE-B040-0F76-E903-40B0760FE904",
            "dsm_model": "",
            "dsm_unique": "",
            "host_ip": "192.168.X.X",
            "host_name": "HOSTNAME",
            "host_port": 0,
            "hypervisor_id": "",
            "inventory_id": 0,
            "kernel_version": "",
            "login_password": "REDACTED",
            "login_time": 1594735318,
            "login_user": "peterm",
            "login_user_id": 1027,
            "mssql_password": "REDACTED",
            "mssql_user": "",
            "oracle_password": "REDACTED",
            "oracle_user": "",
            "os_name": "Windows 11(64-bit)",
            "platform_type": 1,
            "time_zone": -18000,
            "vm_moid_path": ""
          }
        ],
        "enable_app_aware_bkp": false,
        "enable_compress_transfer": true,
        "enable_datastore_aware": false,
        "enable_dedup": true,
        "enable_encrypt_transfer": true,
        "enable_notify": false,
        "enable_shutdown_after_complete": false,
        "enable_verification": false,
        "enable_wake_up": false,
        "enable_windows_working_state": false,
        "max_concurrent_devices": 0,
        "next_trigger_time": 1763884800,
        "pre_post_script_setting": {
          "post_script_path": "",
          "pre_script_path": "",
          "script_exec_mode": 0
        },
        "repo_dir": "@ActiveBackup",
        "retention_policy": {
          "gfs_days": "7",
          "gfs_months": "12",
          "gfs_weeks": "4",
          "gfs_years": "36",
          "keep_all": false,
          "keep_versions": 7
        },
        "sched_content": {
          "backup_window": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111",
          "enable_backup_window": false,
          "is_continuous_paused": false,
          "repeat_hour": 0,
          "repeat_type": "Weekly",
          "run_hour": 3,
          "run_min": 0,
          "run_weekday": [
            0
          ],
          "schedule_setting_type": 1,
          "start_day": 0,
          "start_month": 0,
          "start_year": 0
        },
        "sched_id": 0,
        "sched_modify_time": 1654599934,
        "sched_uuid": "",
        "share_compressed": false,
        "share_name": "ActiveBackupforBusiness",
        "source_type": 3,
        "src_target_dir": "",
        "storage_compress_algorithm": 0,
        "storage_encrypt_algorithm": 0,
        "storage_id": 1,
        "target_dir": "PC-PETERM-PC-peterm-Default",
        "task_id": 1,
        "task_name": "peterm-Default",
        "unikey": "75711daf-8ee1-4bcb-bd84-2b04e9983f6d",
        "verification_policy": 120,
        "view_type": "",
        "vm_folder": null,
        "workload_uuid": ""
      }
    ],
    "total": 5
  },
  "success": true
}
```

**Notes:**
- May take longer to respond


#### Method: `list_vm_check`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Task`
- `version` (required): `1`
- `method` (required): `list_vm_check`
- `_sid` (required): Session ID from login

**Response:**
```json
{
  "data": [],
  "success": true
}
```


#### Method: `list_with_device`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Task`
- `version` (required): `1`
- `method` (required): `list_with_device`
- `_sid` (required): Session ID from login

**Response:**
```json
{
  "data": {
    "cms_info": {
      "is_managed": false,
      "leader_address": "",
      "local_address": "synology01",
      "unfiltered_task_size": 5
    },
    "has_hyperv_inventories": false,
    "has_vmware_inventories": false,
    "tasks": [
      {
        "agentless_backup_path": "",
        "agentless_backup_policy": 0,
        "agentless_enable_block_transfer": false,
        "agentless_enable_dedup": false,
        "agentless_enable_windows_vss": false,
        "backup_cache_content": {
          "cached_enabled": false
        },
        "backup_external": true,
        "backup_type": 2,
        "bandwidth": 0,
        "bandwidth_content": {
          "backup_bandwidth_base": 0,
          "backup_bandwidth_number": 0,
          "enable": false
        },
        "cbt_enable_mode": 1,
        "connection_timeout": 0,
        "custom_volume": [
          "C:"
        ],
        "custom_volume_alias": null,
        "datastore_reserved_percentage": 0,
        "deactivate_by_plan": false,
        "dedup_api_restore": false,
        "dedup_path": "",
        "device_info": {
          "agent_token": "REDACTED",
          "agentless_auth_policy": 0,
          "auto_discovery": false,
          "backup_type": 2,
          "create_time": 1594735305,
          "device_id": 1,
          "device_uuid": "37E1E2FE-B040-0F76-E903-40B0760FE904",
          "dsm_model": "",
          "dsm_unique": "",
          "host_ip": "192.168.X.X",
          "host_name": "HOSTNAME",
          "host_port": 0,
          "hypervisor_id": "",
          "inventory_id": 0,
          "kernel_version": "",
          "login_password": "REDACTED",
          "login_time": 1594735318,
          "login_user": "peterm",
          "login_user_id": 1027,
          "mssql_password": "REDACTED",
          "mssql_user": "",
          "oracle_password": "REDACTED",
          "oracle_user": "",
          "os_name": "Windows 11(64-bit)",
          "time_zone": -18000,
          "vm_moid_path": ""
        },
        "enable_app_aware_bkp": false,
        "enable_compress_transfer": true,
        "enable_datastore_aware": false,
        "enable_dedup": true,
        "enable_encrypt_transfer": true,
        "enable_notify": false,
        "enable_shutdown_after_complete": false,
        "enable_verification": false,
        "enable_wake_up": false,
        "enable_windows_working_state": false,
        "last_result": {
          "activity_uuid": "a62f9539-dbbc-4813-b293-c338f40f73df",
          "backup_type": 2,
          "detail_path": "",
          "error_count": 0,
          "job_action": 1,
          "none_count": 0,
          "result_id": 7544,
          "status": 2,
          "success_count": 0,
          "task_config": {
            "device_list": [
              {
                "device_id": 1,
                "host_name": "HOSTNAME"
              }
            ]
          },
          "task_id": 1,
          "task_name": "peterm-Default",
          "time_end": 1762848525,
          "time_start": 1762848003,
          "transfered_bytes": 4754168380,
          "warning_count": 0
        },
        "max_concurrent_devices": 0,
        "pre_post_script_setting": {
          "post_script_path": "",
          "pre_script_path": "",
          "script_exec_mode": 0
        },
        "repo_dir": "@ActiveBackup",
        "retention_policy": {
          "gfs_days": "7",
          "gfs_months": "12",
          "gfs_weeks": "4",
          "gfs_years": "36",
          "keep_all": false,
          "keep_versions": 7
        },
        "sched_content": {
          "backup_window": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111",
          "enable_backup_window": false,
          "is_continuous_paused": false,
          "repeat_hour": 0,
          "repeat_type": "Weekly",
          "run_hour": 3,
          "run_min": 0,
          "run_weekday": [
            0
          ],
          "schedule_setting_type": 1,
          "start_day": 0,
          "start_month": 0,
          "start_year": 0
        },
        "sched_id": 0,
        "sched_modify_time": 1654599934,
        "sched_uuid": "",
        "share_name": "ActiveBackupforBusiness",
        "source_type": 3,
        "src_target_dir": "",
        "storage_id": 1,
        "target_dir": "PC-PETERM-PC-peterm-Default",
        "task_id": 1,
        "task_name": "peterm-Default",
        "unikey": "75711daf-8ee1-4bcb-bd84-2b04e9983f6d",
        "unique_id": "1-1",
        "verification_policy": 120,
        "view_type": "",
        "workload_uuid": ""
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
- `api` (required): `SYNO.ActiveBackup.Task`
- `version` (required): `1`
- `method` (required): `remove`
- `task_ids` (required): Required parameter
- `_sid` (required): Session ID from login

**Notes:**
- Requires parameter: `task_ids`
- Error code 120 when parameter missing


#### Method: `set`


#### Method: `vm_check_cancel`

**HTTP Method:** GET

**Parameters:**
- `api` (required): `SYNO.ActiveBackup.Task`
- `version` (required): `1`
- `method` (required): `vm_check_cancel`
- `_sid` (required): Session ID from login

**Response:**
```json
{
  "success": true
}
```


---
