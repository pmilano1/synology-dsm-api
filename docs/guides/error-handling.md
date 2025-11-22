# Error Handling Guide

Complete guide to handling errors in the ActiveBackup API.

## Error Response Format

All errors follow this format:

```json
{
  "error": {
    "code": 120,
    "errors": {
      "name": "device_id"
    }
  },
  "success": false
}
```

## Authentication Errors (400-499)

### 400 - Invalid Credentials

**Cause:** Wrong username or password

**Solution:**
```python
try:
    client.login()
except AuthenticationError as e:
    if e.code == 400:
        print("Invalid credentials. Please check username and password.")
```

### 401 - Account Disabled

**Cause:** User account is disabled in DSM

**Solution:** Enable the account in DSM Control Panel → User

### 402 - Permission Denied

**Cause:** Account doesn't have admin privileges

**Solution:** Grant admin privileges or use an admin account

### 403 - 2FA Required

**Cause:** Two-factor authentication is enabled

**Solution:** Disable 2FA for API access or provide OTP code

### 404 - Account Not Found

**Cause:** Username doesn't exist

**Solution:** Verify the username exists in DSM

## API Errors (100-199)

### 102 - Method Not Found

**Cause:** Invalid API or method name

**Example:**
```json
{
  "error": {
    "code": 102
  },
  "success": false
}
```

**Solution:**
- Verify API name is correct
- Check method name spelling
- Ensure API version is supported

### 103 - Permission Denied

**Cause:** Insufficient permissions for this operation

**Solution:**
- Use an admin account
- Check user has ActiveBackup permissions

### 117 - Invalid Operation

**Cause:** Operation not allowed in current state

**Example:** Trying to backup a device that's already backing up

**Solution:**
- Check resource state before operation
- Wait for current operation to complete

### 120 - Missing Required Parameter

**Cause:** Required parameter not provided

**Example:**
```json
{
  "error": {
    "code": 120,
    "errors": {
      "name": "device_id"
    }
  },
  "success": false
}
```

**Solution:**
```python
response = client.call_api("SYNO.ActiveBackup.Device", "get")
if not response.get("success"):
    error = response.get("error", {})
    if error.get("code") == 120:
        missing_param = error.get("errors", {}).get("name")
        print(f"Missing required parameter: {missing_param}")
```

## Parameter Errors (1000-1099)

### 1001 - Invalid Parameter Value

**Cause:** Parameter value is invalid

**Example:** Invalid device_id

**Solution:**
- Verify parameter value exists
- Check parameter format
- Ensure value is correct type

### 1009 - Invalid Parameter Format

**Cause:** Parameter format is incorrect

**Example:** JSON string expected but plain string provided

**Solution:**
```python
import json

# Wrong
response = client.call_api("SYNO.ActiveBackup.Task", "create", 
                          schedule="daily")

# Correct
response = client.call_api("SYNO.ActiveBackup.Task", "create",
                          schedule=json.dumps({"type": "daily"}))
```

### 1010 - Parameter Out of Range

**Cause:** Numeric parameter outside valid range

**Example:** `limit` parameter too large

**Solution:**
- Check parameter constraints
- Use reasonable values (e.g., limit ≤ 1000)

## Session Errors

### Session Expired

**Cause:** Session ID expired (30 min inactivity)

**Solution:**
```python
class ActiveBackupClient:
    def call_api_with_retry(self, api, method, **params):
        """Auto-retry with re-authentication"""
        response = self.call_api(api, method, **params)
        
        if not response.get("success"):
            error = response.get("error", {})
            # Check if session expired (implementation specific)
            if self._is_session_expired(error):
                self.login()
                response = self.call_api(api, method, **params)
        
        return response
```

## Network Errors

### Connection Refused

**Cause:** Cannot connect to NAS

**Solution:**
```python
import requests
from requests.exceptions import ConnectionError

try:
    response = requests.get(url, timeout=10)
except ConnectionError:
    print("Cannot connect to NAS. Check IP address and network.")
except requests.exceptions.Timeout:
    print("Request timed out. NAS may be slow or unreachable.")
```

### SSL Certificate Errors

**Cause:** Self-signed certificate

**Solution:**
```python
# Disable SSL verification (not recommended for production)
response = requests.get(url, verify=False)

# Or provide certificate
response = requests.get(url, verify='/path/to/cert.pem')
```

## Best Practices

### 1. Always Check Success

```python
response = client.call_api("SYNO.ActiveBackup.Device", "list")

if response.get("success"):
    # Process data
    data = response.get("data")
else:
    # Handle error
    error = response.get("error", {})
    handle_error(error)
```

### 2. Implement Retry Logic

```python
def call_with_retry(func, max_retries=3, delay=1):
    """Retry failed API calls"""
    for attempt in range(max_retries):
        try:
            response = func()
            if response.get("success"):
                return response
            
            error = response.get("error", {})
            if error.get("code") in [102, 103, 120]:
                # Don't retry client errors
                return response
            
            # Retry server errors
            time.sleep(delay * (attempt + 1))
        except Exception as e:
            if attempt == max_retries - 1:
                raise
            time.sleep(delay * (attempt + 1))
    
    return response
```

### 3. Log Errors

```python
import logging

logger = logging.getLogger(__name__)

def call_api_with_logging(client, api, method, **params):
    """Call API with error logging"""
    try:
        response = client.call_api(api, method, **params)
        
        if not response.get("success"):
            error = response.get("error", {})
            logger.error(f"API error: {api}.{method} - Code {error.get('code')}")
        
        return response
    except Exception as e:
        logger.exception(f"Exception calling {api}.{method}")
        raise
```

### 4. Graceful Degradation

```python
def get_backup_status(client):
    """Get backup status with fallback"""
    try:
        response = client.call_api("SYNO.ActiveBackup.Overview", "get")
        if response.get("success"):
            return response["data"]
    except Exception:
        pass
    
    # Fallback to basic info
    return {"status": "unknown", "devices": 0}
```

## Error Code Reference

| Code | Description | Retry? | Solution |
|------|-------------|--------|----------|
| 102 | Method not found | No | Check API/method name |
| 103 | Permission denied | No | Use admin account |
| 117 | Invalid operation | Maybe | Check resource state |
| 120 | Missing parameter | No | Add required parameter |
| 400 | Invalid credentials | No | Check username/password |
| 401 | Account disabled | No | Enable account |
| 402 | Permission denied | No | Grant permissions |
| 1001 | Invalid value | No | Check parameter value |
| 1009 | Invalid format | No | Check parameter format |
| 1010 | Out of range | No | Use valid range |

## Next Steps

- **[Common Patterns](../getting-started/common-patterns.md)** - Learn common patterns
- **[API Reference](../api-reference/README.md)** - Complete API documentation
- **[Examples](../examples/)** - See working examples

