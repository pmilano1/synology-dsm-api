# cURL Examples

Command-line examples using cURL for quick testing and scripting.

## Prerequisites

- `curl` installed
- `jq` installed (optional, for pretty JSON output)
- Network access to your Synology NAS

## Basic Usage

### 1. Login and Save Session ID

```bash
# Login and extract session ID
SID=$(curl -s -X POST "http://192.168.1.100:5000/webapi/auth.cgi" \
  -d "api=SYNO.API.Auth" \
  -d "version=6" \
  -d "method=login" \
  -d "account=admin" \
  -d "passwd=YOUR_PASSWORD" \
  -d "session=ActiveBackup" \
  -d "format=sid" \
  | jq -r '.data.sid')

echo "Session ID: $SID"
```

### 2. Get Backup Overview

```bash
curl -s "http://192.168.1.100:5000/webapi/entry.cgi" \
  -d "api=SYNO.ActiveBackup.Overview" \
  -d "version=1" \
  -d "method=get" \
  -d "_sid=$SID" \
  | jq '.'
```

### 3. List All Devices

```bash
curl -s "http://192.168.1.100:5000/webapi/entry.cgi" \
  -d "api=SYNO.ActiveBackup.Device" \
  -d "version=1" \
  -d "method=list" \
  -d "_sid=$SID" \
  | jq '.data.devices[] | {name, device_id, status}'
```

### 4. List All Tasks

```bash
curl -s "http://192.168.1.100:5000/webapi/entry.cgi" \
  -d "api=SYNO.ActiveBackup.Task" \
  -d "version=1" \
  -d "method=list" \
  -d "_sid=$SID" \
  | jq '.data.tasks[] | {name, task_id, status}'
```

### 5. Get Storage Information

```bash
curl -s "http://192.168.1.100:5000/webapi/entry.cgi" \
  -d "api=SYNO.ActiveBackup.Storage" \
  -d "version=1" \
  -d "method=get" \
  -d "_sid=$SID" \
  | jq '.'
```

### 6. Logout

```bash
curl -s -X POST "http://192.168.1.100:5000/webapi/auth.cgi" \
  -d "api=SYNO.API.Auth" \
  -d "version=6" \
  -d "method=logout" \
  -d "session=ActiveBackup" \
  -d "_sid=$SID" \
  | jq '.'
```

## Complete Script

Save this as `backup-status.sh`:

```bash
#!/bin/bash

# Configuration
NAS_IP="192.168.1.100"
USERNAME="admin"
PASSWORD="YOUR_PASSWORD"

# Login
echo "Logging in..."
SID=$(curl -s -X POST "http://$NAS_IP:5000/webapi/auth.cgi" \
  -d "api=SYNO.API.Auth" \
  -d "version=6" \
  -d "method=login" \
  -d "account=$USERNAME" \
  -d "passwd=$PASSWORD" \
  -d "session=ActiveBackup" \
  -d "format=sid" \
  | jq -r '.data.sid')

if [ -z "$SID" ] || [ "$SID" == "null" ]; then
    echo "Login failed!"
    exit 1
fi

echo "Logged in successfully"

# Get overview
echo -e "\n=== Backup Overview ==="
curl -s "http://$NAS_IP:5000/webapi/entry.cgi" \
  -d "api=SYNO.ActiveBackup.Overview" \
  -d "version=1" \
  -d "method=get" \
  -d "_sid=$SID" \
  | jq '.data'

# List devices
echo -e "\n=== Backup Devices ==="
curl -s "http://$NAS_IP:5000/webapi/entry.cgi" \
  -d "api=SYNO.ActiveBackup.Device" \
  -d "version=1" \
  -d "method=list" \
  -d "_sid=$SID" \
  | jq '.data.devices[] | {name, status}'

# List tasks
echo -e "\n=== Backup Tasks ==="
curl -s "http://$NAS_IP:5000/webapi/entry.cgi" \
  -d "api=SYNO.ActiveBackup.Task" \
  -d "version=1" \
  -d "method=list" \
  -d "_sid=$SID" \
  | jq '.data.tasks[] | {name, status}'

# Logout
echo -e "\nLogging out..."
curl -s -X POST "http://$NAS_IP:5000/webapi/auth.cgi" \
  -d "api=SYNO.API.Auth" \
  -d "version=6" \
  -d "method=logout" \
  -d "session=ActiveBackup" \
  -d "_sid=$SID" \
  | jq '.'

echo "Done!"
```

Make it executable:
```bash
chmod +x backup-status.sh
./backup-status.sh
```

## Advanced Examples

### Trigger Backup for Specific Task

```bash
curl -s "http://192.168.1.100:5000/webapi/entry.cgi" \
  -d "api=SYNO.ActiveBackup.Task" \
  -d "version=1" \
  -d "method=backup" \
  -d "task_ids=[\"123\"]" \
  -d "_sid=$SID" \
  | jq '.'
```

### Get Backup Versions for Device

```bash
curl -s "http://192.168.1.100:5000/webapi/entry.cgi" \
  -d "api=SYNO.ActiveBackup.Device" \
  -d "version=1" \
  -d "method=list_restorable_version" \
  -d "device_id=123" \
  -d "_sid=$SID" \
  | jq '.'
```

### Get Logs

```bash
curl -s "http://192.168.1.100:5000/webapi/entry.cgi" \
  -d "api=SYNO.ActiveBackup.Log" \
  -d "version=1" \
  -d "method=list_log" \
  -d "_sid=$SID" \
  | jq '.'
```

## Tips

### Pretty Print JSON

Always pipe to `jq` for readable output:
```bash
curl ... | jq '.'
```

### Extract Specific Fields

```bash
curl ... | jq '.data.devices[] | .name'
```

### Save Response to File

```bash
curl ... > response.json
```

### Debug Mode

Add `-v` for verbose output:
```bash
curl -v "http://..." ...
```

### Use HTTPS

For production, use HTTPS (port 5001):
```bash
curl -k "https://192.168.1.100:5001/webapi/..." ...
```

Note: `-k` disables certificate verification (use with caution)

## Next Steps

- **[Python Examples](../python/)** - More complex automation
- **[JavaScript Examples](../javascript/)** - Web integration
- **[API Reference](../../api-reference/README.md)** - Complete API docs

