# Quick Start Guide

Get started with the Synology ActiveBackup for Business API in 5 minutes.

## Prerequisites

- Synology NAS with ActiveBackup for Business installed
- Admin account credentials
- Network access to your NAS

## Step 1: Authenticate

All API calls require authentication. First, obtain a session ID:

### Using cURL

```bash
curl -X POST "http://YOUR_NAS_IP:5000/webapi/auth.cgi" \
  -d "api=SYNO.API.Auth" \
  -d "version=6" \
  -d "method=login" \
  -d "account=admin" \
  -d "passwd=YOUR_PASSWORD" \
  -d "session=ActiveBackup" \
  -d "format=sid"
```

### Using Python

```python
import requests

response = requests.post(
    "http://YOUR_NAS_IP:5000/webapi/auth.cgi",
    data={
        "api": "SYNO.API.Auth",
        "version": "6",
        "method": "login",
        "account": "admin",
        "passwd": "YOUR_PASSWORD",
        "session": "ActiveBackup",
        "format": "sid"
    }
)

data = response.json()
sid = data["data"]["sid"]
print(f"Session ID: {sid}")
```

### Using JavaScript (Node.js)

```javascript
const axios = require('axios');

async function login() {
    const response = await axios.post(
        'http://YOUR_NAS_IP:5000/webapi/auth.cgi',
        new URLSearchParams({
            api: 'SYNO.API.Auth',
            version: '6',
            method: 'login',
            account: 'admin',
            passwd: 'YOUR_PASSWORD',
            session: 'ActiveBackup',
            format: 'sid'
        })
    );
    
    const sid = response.data.data.sid;
    console.log(`Session ID: ${sid}`);
    return sid;
}
```

### Response

```json
{
  "data": {
    "sid": "AbCdEfGhIjKlMnOpQrStUvWxYz123456"
  },
  "success": true
}
```

Save the `sid` value - you'll need it for all subsequent API calls.

## Step 2: Make Your First API Call

Let's get an overview of your backup system:

### Using cURL

```bash
curl "http://YOUR_NAS_IP:5000/webapi/entry.cgi" \
  -d "api=SYNO.ActiveBackup.Overview" \
  -d "version=1" \
  -d "method=get" \
  -d "_sid=YOUR_SESSION_ID"
```

### Using Python

```python
response = requests.get(
    "http://YOUR_NAS_IP:5000/webapi/entry.cgi",
    params={
        "api": "SYNO.ActiveBackup.Overview",
        "version": "1",
        "method": "get",
        "_sid": sid
    }
)

overview = response.json()
print(overview)
```

### Using JavaScript

```javascript
const response = await axios.get(
    'http://YOUR_NAS_IP:5000/webapi/entry.cgi',
    {
        params: {
            api: 'SYNO.ActiveBackup.Overview',
            version: '1',
            method: 'get',
            _sid: sid
        }
    }
);

console.log(response.data);
```

### Response

```json
{
  "data": {
    "backup_size": 1234567890,
    "device_count": 5,
    "task_count": 10,
    "last_backup": 1700000000
  },
  "success": true
}
```

## Step 3: List Backup Devices

Get a list of all devices being backed up:

```bash
curl "http://YOUR_NAS_IP:5000/webapi/entry.cgi" \
  -d "api=SYNO.ActiveBackup.Device" \
  -d "version=1" \
  -d "method=list" \
  -d "_sid=YOUR_SESSION_ID"
```

## Step 4: List Backup Tasks

Get all backup tasks:

```bash
curl "http://YOUR_NAS_IP:5000/webapi/entry.cgi" \
  -d "api=SYNO.ActiveBackup.Task" \
  -d "version=1" \
  -d "method=list" \
  -d "_sid=YOUR_SESSION_ID"
```

## Common Patterns

### GET vs POST

- Most `list` and `get` methods work with GET requests
- `create`, `update`, `delete` methods typically require POST
- When in doubt, POST works for everything

### Required Parameters

All API calls require:
- `api` - The API name (e.g., `SYNO.ActiveBackup.Device`)
- `version` - API version (usually `1`)
- `method` - The method name (e.g., `list`)
- `_sid` - Your session ID from login

### Error Handling

Always check the `success` field in responses:

```python
response = requests.get(url, params=params)
data = response.json()

if data.get("success"):
    # Success
    result = data.get("data")
else:
    # Error
    error = data.get("error")
    print(f"Error {error['code']}: {error}")
```

## Next Steps

- **[Authentication Guide](authentication.md)** - Learn about session management
- **[Common Patterns](common-patterns.md)** - Common API usage patterns
- **[API Reference](../api-reference/README.md)** - Complete API documentation
- **[Examples](../examples/)** - More code examples

## Troubleshooting

### Connection Refused
- Verify your NAS IP address
- Ensure port 5000 is accessible
- Check firewall settings

### Authentication Failed
- Verify username and password
- Ensure account has admin privileges
- Check if account is enabled

### Invalid Session
- Session IDs expire after inactivity
- Re-authenticate to get a new session ID
- Store session ID securely

## Need Help?

- Check the [Error Handling Guide](../guides/error-handling.md)
- See [Common Patterns](common-patterns.md)
- Review [API Reference](../api-reference/README.md)

