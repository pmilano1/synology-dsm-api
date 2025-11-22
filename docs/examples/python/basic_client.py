#!/usr/bin/env python3
"""
Basic Python client for Synology ActiveBackup for Business API

Usage:
    python basic_client.py
"""

import requests
import json
from typing import Dict, Any, Optional


class ActiveBackupClient:
    """Client for Synology ActiveBackup for Business API"""
    
    def __init__(self, host: str, username: str, password: str, use_https: bool = False):
        """
        Initialize the client
        
        Args:
            host: NAS hostname or IP address
            username: Admin username
            password: Admin password
            use_https: Use HTTPS instead of HTTP (default: False)
        """
        self.host = host
        self.username = username
        self.password = password
        protocol = "https" if use_https else "http"
        port = 5001 if use_https else 5000
        self.base_url = f"{protocol}://{host}:{port}/webapi"
        self.sid: Optional[str] = None
        
    def login(self) -> bool:
        """
        Login and obtain session ID
        
        Returns:
            True if login successful, False otherwise
        """
        response = requests.post(
            f"{self.base_url}/auth.cgi",
            data={
                "api": "SYNO.API.Auth",
                "version": "6",
                "method": "login",
                "account": self.username,
                "passwd": self.password,
                "session": "ActiveBackup",
                "format": "sid"
            },
            verify=False  # Disable SSL verification for self-signed certs
        )
        
        data = response.json()
        if data.get("success"):
            self.sid = data["data"]["sid"]
            print(f"✅ Logged in successfully")
            return True
        else:
            error = data.get("error", {})
            print(f"❌ Login failed: Error {error.get('code')}")
            return False
    
    def logout(self) -> bool:
        """
        Logout and invalidate session
        
        Returns:
            True if logout successful, False otherwise
        """
        if not self.sid:
            return True
            
        response = requests.post(
            f"{self.base_url}/auth.cgi",
            data={
                "api": "SYNO.API.Auth",
                "version": "6",
                "method": "logout",
                "session": "ActiveBackup",
                "_sid": self.sid
            },
            verify=False
        )
        
        data = response.json()
        if data.get("success"):
            print(f"✅ Logged out successfully")
            self.sid = None
            return True
        return False
    
    def call_api(self, api: str, method: str, version: str = "1", **params) -> Dict[str, Any]:
        """
        Call an API method
        
        Args:
            api: API name (e.g., "SYNO.ActiveBackup.Device")
            method: Method name (e.g., "list")
            version: API version (default: "1")
            **params: Additional parameters
            
        Returns:
            API response as dictionary
        """
        if not self.sid:
            raise Exception("Not logged in. Call login() first.")
        
        params.update({
            "api": api,
            "version": version,
            "method": method,
            "_sid": self.sid
        })
        
        response = requests.get(
            f"{self.base_url}/entry.cgi",
            params=params,
            verify=False
        )
        
        return response.json()
    
    def get_overview(self) -> Dict[str, Any]:
        """Get backup overview"""
        return self.call_api("SYNO.ActiveBackup.Overview", "get")
    
    def list_devices(self) -> Dict[str, Any]:
        """List all backup devices"""
        return self.call_api("SYNO.ActiveBackup.Device", "list")
    
    def list_tasks(self) -> Dict[str, Any]:
        """List all backup tasks"""
        return self.call_api("SYNO.ActiveBackup.Task", "list")
    
    def get_storage_info(self) -> Dict[str, Any]:
        """Get storage information"""
        return self.call_api("SYNO.ActiveBackup.Storage", "get")


def main():
    """Example usage"""
    
    # Configuration
    NAS_HOST = "192.168.1.100"
    USERNAME = "admin"
    PASSWORD = "your_password"
    
    # Create client
    client = ActiveBackupClient(NAS_HOST, USERNAME, PASSWORD)
    
    try:
        # Login
        if not client.login():
            return
        
        # Get overview
        print("\n📊 Backup Overview:")
        overview = client.get_overview()
        if overview.get("success"):
            print(json.dumps(overview["data"], indent=2))
        
        # List devices
        print("\n💻 Backup Devices:")
        devices = client.list_devices()
        if devices.get("success"):
            device_list = devices["data"].get("devices", [])
            print(f"Total devices: {len(device_list)}")
            for device in device_list[:5]:  # Show first 5
                print(f"  - {device.get('name', 'Unknown')}")
        
        # List tasks
        print("\n📋 Backup Tasks:")
        tasks = client.list_tasks()
        if tasks.get("success"):
            task_list = tasks["data"].get("tasks", [])
            print(f"Total tasks: {len(task_list)}")
            for task in task_list[:5]:  # Show first 5
                print(f"  - {task.get('name', 'Unknown')}")
        
    finally:
        # Always logout
        client.logout()


if __name__ == "__main__":
    main()

