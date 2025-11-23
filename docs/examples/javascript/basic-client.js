#!/usr/bin/env node
/**
 * Basic Node.js client for Synology ActiveBackup for Business API
 *
 * Usage:
 *   node basic-client.js
 *
 * Requirements:
 *   npm install axios
 */

const axios = require('axios');
const https = require('https');

class ActiveBackupClient {
    /**
     * Initialize the client
     *
     * @param {string} host - NAS hostname or IP address
     * @param {string} username - Admin username
     * @param {string} password - Admin password
     * @param {boolean} useHttps - Use HTTPS instead of HTTP (default: false)
     */
    constructor(host, username, password, useHttps = false) {
        this.host = host;
        this.username = username;
        this.password = password;
        const protocol = useHttps ? 'https' : 'http';
        const port = useHttps ? 5001 : 5000;
        this.baseUrl = `${protocol}://${host}:${port}/webapi`;
        this.sid = null;

        // Create axios instance with SSL verification disabled for self-signed certs
        this.axios = axios.create({
            httpsAgent: new https.Agent({
                rejectUnauthorized: false
            })
        });
    }

    /**
     * Login and obtain session ID
     *
     * @returns {Promise<boolean>} True if login successful
     */
    async login() {
        try {
            const response = await this.axios.post(`${this.baseUrl}/auth.cgi`, null, {
                params: {
                    api: 'SYNO.API.Auth',
                    version: '6',
                    method: 'login',
                    account: this.username,
                    passwd: this.password,
                    session: 'ActiveBackup',
                    format: 'sid'
                }
            });

            const data = response.data;
            if (data.success) {
                this.sid = data.data.sid;
                console.log('✅ Logged in successfully');
                return true;
            } else {
                const error = data.error || {};
                console.error(`❌ Login failed: Error ${error.code}`);
                return false;
            }
        } catch (error) {
            console.error('❌ Login error:', error.message);
            return false;
        }
    }

    /**
     * Logout and invalidate session
     *
     * @returns {Promise<boolean>} True if logout successful
     */
    async logout() {
        if (!this.sid) {
            return true;
        }

        try {
            const response = await this.axios.post(`${this.baseUrl}/auth.cgi`, null, {
                params: {
                    api: 'SYNO.API.Auth',
                    version: '6',
                    method: 'logout',
                    session: 'ActiveBackup',
                    _sid: this.sid
                }
            });

            if (response.data.success) {
                console.log('✅ Logged out successfully');
                this.sid = null;
                return true;
            }
            return false;
        } catch (error) {
            console.error('❌ Logout error:', error.message);
            return false;
        }
    }

    /**
     * Call an API method
     *
     * @param {string} api - API name (e.g., "SYNO.ActiveBackup.Device")
     * @param {string} method - Method name (e.g., "list")
     * @param {string} version - API version (default: "1")
     * @param {Object} params - Additional parameters
     * @returns {Promise<Object>} API response
     */
    async callApi(api, method, version = '1', params = {}) {
        if (!this.sid) {
            throw new Error('Not logged in. Call login() first.');
        }

        try {
            const response = await this.axios.get(`${this.baseUrl}/entry.cgi`, {
                params: {
                    api,
                    version,
                    method,
                    _sid: this.sid,
                    ...params
                }
            });

            return response.data;
        } catch (error) {
            console.error('❌ API call error:', error.message);
            throw error;
        }
    }

    /**
     * Get backup overview
     */
    async getOverview() {
        return this.callApi('SYNO.ActiveBackup.Overview', 'get');
    }

    /**
     * List all backup devices
     */
    async listDevices() {
        return this.callApi('SYNO.ActiveBackup.Device', 'list');
    }

    /**
     * List all backup tasks
     */
    async listTasks() {
        return this.callApi('SYNO.ActiveBackup.Task', 'list');
    }

    /**
     * Get storage information
     */
    async getStorageInfo() {
        return this.callApi('SYNO.ActiveBackup.Storage', 'get');
    }
}

/**
 * Example usage
 */
async function main() {
    // Configuration
    const NAS_HOST = '192.168.1.100';
    const USERNAME = 'admin';
    const PASSWORD = 'your_password';

    // Create client
    const client = new ActiveBackupClient(NAS_HOST, USERNAME, PASSWORD);

    try {
        // Login
        if (!await client.login()) {
            return;
        }

        // Get overview
        console.log('\n📊 Backup Overview:');
        const overview = await client.getOverview();
        if (overview.success) {
            console.log(JSON.stringify(overview.data, null, 2));
        }

        // List devices
        console.log('\n💻 Backup Devices:');
        const devices = await client.listDevices();
        if (devices.success) {
            const deviceList = devices.data.devices || [];
            console.log(`Total devices: ${deviceList.length}`);
            deviceList.slice(0, 5).forEach(device => {
                console.log(`  - ${device.name || 'Unknown'}`);
            });
        }

        // List tasks
        console.log('\n📋 Backup Tasks:');
        const tasks = await client.listTasks();
        if (tasks.success) {
            const taskList = tasks.data.tasks || [];
            console.log(`Total tasks: ${taskList.length}`);
            taskList.slice(0, 5).forEach(task => {
                console.log(`  - ${task.name || 'Unknown'}`);
            });
        }

        // Get storage info
        console.log('\n💾 Storage Information:');
        const storage = await client.getStorageInfo();
        if (storage.success) {
            console.log(JSON.stringify(storage.data, null, 2));
        }

    } catch (error) {
        console.error('Error:', error.message);
    } finally {
        // Always logout
        await client.logout();
    }
}

// Run if executed directly
if (require.main === module) {
    main().catch(console.error);
}

// Export for use as module
module.exports = ActiveBackupClient;

