# Common Patterns

Learn common patterns and best practices for using the ActiveBackup API.

## API Call Patterns

### List Resources

Most APIs have a `list` method that returns all resources:

```python
# List all devices
response = client.call_api("SYNO.ActiveBackup.Device", "list")

# List all tasks
response = client.call_api("SYNO.ActiveBackup.Task", "list")

# List all backup versions
response = client.call_api("SYNO.ActiveBackup.Version", "list", task_id="123")
```

**Pattern:**
- Method name: `list`
- Usually works without parameters
- Returns array of resources
- May support pagination with `limit` and `offset`

### Get Single Resource

Get details of a specific resource:

```python
# Get device details
response = client.call_api("SYNO.ActiveBackup.Device", "get", device_id="123")

# Get task details
response = client.call_api("SYNO.ActiveBackup.Task", "get", task_id="456")
```

**Pattern:**
- Method name: `get`
- Requires resource ID parameter
- Returns single resource object

### Create Resource

Create a new resource:

```python
# Create a new task
response = client.call_api(
    "SYNO.ActiveBackup.Task",
    "create",
    name="My Backup Task",
    device_id="123",
    schedule=json.dumps({"type": "daily", "hour": 2})
)
```

**Pattern:**
- Method name: `create`
- Requires resource data as parameters
- Returns created resource with ID

### Update Resource

Update an existing resource:

```python
# Update task settings
response = client.call_api(
    "SYNO.ActiveBackup.Task",
    "update",
    task_id="456",
    name="Updated Task Name"
)
```

**Pattern:**
- Method name: `update` or `set`
- Requires resource ID
- Requires fields to update
- Returns updated resource

### Delete Resource

Delete a resource:

```python
# Delete a task
response = client.call_api(
    "SYNO.ActiveBackup.Task",
    "remove",
    task_ids=json.dumps(["456"])
)
```

**Pattern:**
- Method name: `remove` or `delete`
- Requires resource ID(s)
- May accept array of IDs for bulk deletion
- Returns success status

## Response Handling

### Success Response

```python
response = client.call_api("SYNO.ActiveBackup.Device", "list")

if response.get("success"):
    data = response.get("data")
    # Process data
else:
    error = response.get("error")
    print(f"Error: {error}")
```

### Error Response

```python
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

**Common error codes:**
- `102` - Method not found
- `103` - Permission denied
- `120` - Missing required parameter
- `1001` - Invalid parameter value

## Pagination

For large result sets, use pagination:

```python
def get_all_devices(client):
    """Get all devices with pagination"""
    all_devices = []
    offset = 0
    limit = 100
    
    while True:
        response = client.call_api(
            "SYNO.ActiveBackup.Device",
            "list",
            limit=limit,
            offset=offset
        )
        
        if not response.get("success"):
            break
        
        devices = response["data"].get("devices", [])
        if not devices:
            break
        
        all_devices.extend(devices)
        offset += limit
    
    return all_devices
```

## Filtering and Sorting

Some APIs support filtering and sorting:

```python
# Filter devices by type
response = client.call_api(
    "SYNO.ActiveBackup.Device",
    "list",
    filter=json.dumps({"type": "pc"}),
    sort_by="name",
    sort_direction="ASC"
)
```

## Batch Operations

Many delete/update operations support batch processing:

```python
# Delete multiple tasks at once
response = client.call_api(
    "SYNO.ActiveBackup.Task",
    "remove",
    task_ids=json.dumps(["123", "456", "789"])
)

# Backup multiple tasks
response = client.call_api(
    "SYNO.ActiveBackup.Task",
    "backup",
    task_ids=json.dumps(["123", "456"])
)
```

## JSON Parameters

Complex parameters must be JSON-encoded:

```python
import json

# Schedule configuration
schedule = {
    "type": "daily",
    "hour": 2,
    "minute": 0,
    "days": [1, 2, 3, 4, 5]  # Monday-Friday
}

response = client.call_api(
    "SYNO.ActiveBackup.Task",
    "create",
    schedule=json.dumps(schedule)
)
```

## Session Management

### Reuse Sessions

```python
class ActiveBackupClient:
    def __init__(self, host, username, password):
        self.sid = None
        self.login(username, password)
    
    def call_api(self, api, method, **params):
        if not self.sid:
            raise Exception("Not logged in")
        # Use self.sid for all calls
```

### Handle Expiration

```python
def call_api_with_retry(self, api, method, **params):
    """Call API with automatic re-authentication"""
    try:
        return self.call_api(api, method, **params)
    except SessionExpiredError:
        self.login()
        return self.call_api(api, method, **params)
```

## Error Handling

### Graceful Degradation

```python
def get_device_info(client, device_id):
    """Get device info with fallback"""
    try:
        response = client.call_api(
            "SYNO.ActiveBackup.Device",
            "get",
            device_id=device_id
        )
        
        if response.get("success"):
            return response["data"]
        else:
            error = response.get("error", {})
            if error.get("code") == 120:
                # Missing parameter
                return None
            raise Exception(f"API error: {error}")
    except Exception as e:
        print(f"Error getting device info: {e}")
        return None
```

## Rate Limiting

Be respectful of the API:

```python
import time

def batch_process_with_delay(items, process_func, delay=0.1):
    """Process items with delay between calls"""
    results = []
    for item in items:
        result = process_func(item)
        results.append(result)
        time.sleep(delay)  # Avoid overwhelming the API
    return results
```

## Next Steps

- **[API Reference](../api-reference/README.md)** - Complete API documentation
- **[Examples](../examples/)** - More code examples
- **[Error Handling Guide](../guides/error-handling.md)** - Handle errors gracefully

