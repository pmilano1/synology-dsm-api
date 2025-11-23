# JavaScript/Node.js Examples

Node.js examples for integrating with the Synology ActiveBackup for Business API.

## Prerequisites

- **Node.js** 14+ installed
- **npm** or **yarn** package manager
- Network access to your Synology NAS

## Installation

Install required dependencies:

```bash
npm install axios
# or
yarn add axios
```

## Quick Start

### 1. Basic Client Usage

The `basic-client.js` provides a complete client class for interacting with the API.

```javascript
const ActiveBackupClient = require('./basic-client');

async function example() {
    const client = new ActiveBackupClient(
        '192.168.1.100',  // NAS IP
        'admin',          // Username
        'your_password'   // Password
    );

    try {
        // Login
        await client.login();

        // Get backup overview
        const overview = await client.getOverview();
        console.log(overview.data);

        // List devices
        const devices = await client.listDevices();
        console.log(devices.data.devices);

        // Logout
        await client.logout();
    } catch (error) {
        console.error('Error:', error.message);
    }
}

example();
```

### 2. Run the Example

```bash
# Edit the configuration in basic-client.js first
node basic-client.js
```

## API Client Class

### Constructor

```javascript
const client = new ActiveBackupClient(host, username, password, useHttps);
```

**Parameters:**
- `host` (string) - NAS hostname or IP address
- `username` (string) - Admin username
- `password` (string) - Admin password
- `useHttps` (boolean) - Use HTTPS instead of HTTP (default: false)

### Methods

#### Authentication

```javascript
// Login and get session ID
await client.login();

// Logout and invalidate session
await client.logout();
```

#### API Calls

```javascript
// Generic API call
await client.callApi(api, method, version, params);

// Get backup overview
await client.getOverview();

// List all devices
await client.listDevices();

// List all tasks
await client.listTasks();

// Get storage information
await client.getStorageInfo();
```

## Advanced Examples

### Custom API Call

```javascript
const client = new ActiveBackupClient('192.168.1.100', 'admin', 'password');

await client.login();

// Call any API method
const result = await client.callApi(
    'SYNO.ActiveBackup.Device',  // API name
    'list_restorable_version',   // Method
    '1',                          // Version
    { device_id: '123' }          // Parameters
);

console.log(result);
await client.logout();
```

### Error Handling

```javascript
const client = new ActiveBackupClient('192.168.1.100', 'admin', 'password');

try {
    if (!await client.login()) {
        throw new Error('Login failed');
    }

    const overview = await client.getOverview();

    if (!overview.success) {
        const error = overview.error || {};
        throw new Error(`API error ${error.code}: ${error.message}`);
    }

    console.log('Success:', overview.data);

} catch (error) {
    console.error('Error:', error.message);
} finally {
    await client.logout();
}
```

### Monitoring Script

```javascript
const ActiveBackupClient = require('./basic-client');

async function checkBackupStatus() {
    const client = new ActiveBackupClient(
        process.env.NAS_HOST || '192.168.1.100',
        process.env.NAS_USER || 'admin',
        process.env.NAS_PASS || 'password'
    );

    try {
        await client.login();

        // Get overview
        const overview = await client.getOverview();
        const stats = overview.data;

        console.log('=== Backup Status ===');
        console.log(`Total Devices: ${stats.total_devices || 0}`);
        console.log(`Active Tasks: ${stats.active_tasks || 0}`);
        console.log(`Failed Tasks: ${stats.failed_tasks || 0}`);

        // Check for failed tasks
        if (stats.failed_tasks > 0) {
            console.warn('⚠️  Warning: Failed tasks detected!');

            // Get task details
            const tasks = await client.listTasks();
            const failedTasks = tasks.data.tasks.filter(t => t.status === 'failed');

            failedTasks.forEach(task => {
                console.error(`  - ${task.name}: ${task.error_message}`);
            });
        } else {
            console.log('✅ All backups healthy');
        }

        await client.logout();

    } catch (error) {
        console.error('❌ Error checking backup status:', error.message);
        process.exit(1);
    }
}

// Run every hour
setInterval(checkBackupStatus, 60 * 60 * 1000);
checkBackupStatus(); // Run immediately
```

## Environment Variables

For production use, store credentials in environment variables:

```bash
# .env file
NAS_HOST=192.168.1.100
NAS_USER=admin
NAS_PASS=your_password
NAS_USE_HTTPS=false
```

```javascript
require('dotenv').config();

const client = new ActiveBackupClient(
    process.env.NAS_HOST,
    process.env.NAS_USER,
    process.env.NAS_PASS,
    process.env.NAS_USE_HTTPS === 'true'
);
```

Install dotenv:
```bash
npm install dotenv
```

## TypeScript Support

For TypeScript projects, create type definitions:

```typescript
// types.d.ts
declare module 'basic-client' {
    export default class ActiveBackupClient {
        constructor(host: string, username: string, password: string, useHttps?: boolean);
        login(): Promise<boolean>;
        logout(): Promise<boolean>;
        callApi(api: string, method: string, version?: string, params?: object): Promise<any>;
        getOverview(): Promise<any>;
        listDevices(): Promise<any>;
        listTasks(): Promise<any>;
        getStorageInfo(): Promise<any>;
    }
}
```

## Common Use Cases

### 1. Backup Status Dashboard

```javascript
async function getBackupDashboard() {
    const client = new ActiveBackupClient('192.168.1.100', 'admin', 'password');
    await client.login();

    const [overview, devices, tasks, storage] = await Promise.all([
        client.getOverview(),
        client.listDevices(),
        client.listTasks(),
        client.getStorageInfo()
    ]);

    await client.logout();

    return {
        overview: overview.data,
        devices: devices.data.devices,
        tasks: tasks.data.tasks,
        storage: storage.data
    };
}
```

### 2. Trigger Backup for Specific Device

```javascript
async function triggerBackup(deviceId) {
    const client = new ActiveBackupClient('192.168.1.100', 'admin', 'password');
    await client.login();

    const result = await client.callApi(
        'SYNO.ActiveBackup.Task',
        'backup',
        '1',
        { device_ids: JSON.stringify([deviceId]) }
    );

    await client.logout();
    return result;
}
```

### 3. Get Backup History

```javascript
async function getBackupHistory(deviceId) {
    const client = new ActiveBackupClient('192.168.1.100', 'admin', 'password');
    await client.login();

    const result = await client.callApi(
        'SYNO.ActiveBackup.Device',
        'list_restorable_version',
        '1',
        { device_id: deviceId }
    );

    await client.logout();
    return result.data.versions;
}
```

## Tips

### 1. Connection Pooling

For high-frequency API calls, reuse the client instance:

```javascript
class BackupService {
    constructor() {
        this.client = new ActiveBackupClient('192.168.1.100', 'admin', 'password');
        this.isLoggedIn = false;
    }

    async ensureLoggedIn() {
        if (!this.isLoggedIn) {
            this.isLoggedIn = await this.client.login();
        }
    }

    async getOverview() {
        await this.ensureLoggedIn();
        return this.client.getOverview();
    }
}
```

### 2. Retry Logic

```javascript
async function callApiWithRetry(client, api, method, maxRetries = 3) {
    for (let i = 0; i < maxRetries; i++) {
        try {
            return await client.callApi(api, method);
        } catch (error) {
            if (i === maxRetries - 1) throw error;
            await new Promise(resolve => setTimeout(resolve, 1000 * (i + 1)));
        }
    }
}
```

### 3. Rate Limiting

```javascript
const pLimit = require('p-limit');
const limit = pLimit(5); // Max 5 concurrent requests

const devices = await client.listDevices();
const deviceDetails = await Promise.all(
    devices.data.devices.map(device =>
        limit(() => client.callApi('SYNO.ActiveBackup.Device', 'get', '1', { device_id: device.id }))
    )
);
```

## Next Steps

- **[Python Examples](../python/)** - Python implementation
- **[cURL Examples](../curl/)** - Command-line examples
- **[API Reference](../../api-reference/README.md)** - Complete API documentation
- **[Best Practices](../../guides/best-practices.md)** - API best practices

} catch (error) {
    console.error('Error:', error.message);
} finally {
    await client.logout();
}
```

### Using with Express.js

```javascript
const express = require('express');
const ActiveBackupClient = require('./basic-client');

const app = express();

app.get('/api/backup/overview', async (req, res) => {
    const client = new ActiveBackupClient(
        process.env.NAS_HOST,
        process.env.NAS_USER,
        process.env.NAS_PASS
    );

    try {
        await client.login();
        const overview = await client.getOverview();
        await client.logout();

        if (overview.success) {
            res.json(overview.data);
        } else {
            res.status(500).json({ error: overview.error });
        }
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

app.listen(3000, () => {
    console.log('Server running on port 3000');
});
```

