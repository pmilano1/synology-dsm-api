# Core-other APIs (probed)

**Category:** DSM Services

[← Back to Probed APIs](README.md)

---

These APIs were confirmed against a live DSM 7.4 appliance by probing every
read-shaped method (`list`, `get`, `info`, `status`, `query`, `enum`) at the version the
appliance itself advertises. An entry appears here only because DSM answered for it.

Response blocks are **shapes, not captures** — key names and value *types*, derived on the
appliance so no real hostname, account, share, serial or key ever left it. Where a method
exists but needs arguments, that is stated with the error code rather than guessed at.

Write-shaped methods were not probed: DSM validates `version` *before* `method`, so a
no-argument call to an unknown write method executes it. Those need a disposable appliance.

---

## SYNO.Core.ActionPriv

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.ActionPriv`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

Confirmed present: DSM returned error 2 rather than 103, so the method exists. What it additionally requires was not determined.
The exact signature was not determined; it is listed here so it is known to exist.

**Response:**

```json
{
  "success": false,
  "error": {
    "code": 2
  }
}
```

## SYNO.Core.ActionPriv.Role

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `list`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.ActionPriv.Role`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "roles": [
      {
        "desc": "string",
        "priv_id": "string",
        "title": "string"
      }
    ]
  }
}
```

## SYNO.Core.AppNotify

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.AppNotify`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "SYNO.SDS.AdminCenter.Application": {
      "customized": "boolean",
      "fn": {
        "SYNO.SDS.AdminCenter.Update_Reset.Main": "object"
      },
      "lastView": "integer",
      "time": "integer",
      "unread": "integer"
    },
    "SYNO.SDS.PkgManApp.Instance": {
      "customized": "boolean",
      "fn": {
        "generalFn": "object"
      },
      "lastView": "integer",
      "time": "integer",
      "unread": "integer"
    },
    "SYNO.SDS.SecurityScan.Instance": {
      "customized": "boolean",
      "fn": {
        "generalFn": "object"
      },
      "lastView": "integer",
      "time": "integer",
      "unread": "integer"
    }
  }
}
```

## SYNO.Core.AppPortal.AccessControl

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `list`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.AppPortal.AccessControl`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "entries": "array<empty>"
  }
}
```

## SYNO.Core.BackgroundTask

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.BackgroundTask`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "task_conf_time": {
      "nsec": "integer",
      "sec": "integer"
    },
    "task_data_time": {
      "nsec": "integer",
      "sec": "integer"
    },
    "task_groups": {
      "shared_folder": {
        "belong_tray": "string",
        "custom_tray_tooltip": "string",
        "enable_tray_tooltip": "boolean",
        "functions": "object",
        "i18n": "string",
        "icon_class": "string",
        "icon_path": "string",
        "is_tray": "boolean",
        "read_only_config": "boolean",
        "tray_groups": "array<empty>",
        "tray_icon_class": "string"
      },
      "storage_manager": {
        "belong_tray": "string",
        "custom_tray_tooltip": "string",
        "enable_tray_tooltip": "boolean",
        "functions": "object",
        "i18n": "string",
        "icon_class": "string",
        "icon_path": "string",
        "is_tray": "boolean",
        "read_only_config": "boolean",
        "tray_groups": "array<empty>",
        "tray_icon_class": "string"
      },
      "synoindex": {
        "belong_tray": "string",
        "custom_tray_tooltip": "string",
        "enable_tray_tooltip": "boolean",
        "functions": "object",
        "i18n": "string",
        "icon_class": "string",
        "icon_path": "string",
        "is_tray": "boolean",
        "read_only_config": "boolean",
        "tray_groups": "array<empty>",
        "tray_icon_class": "string"
      }
    }
  }
}
```

## SYNO.Core.CurrentConnection

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.CurrentConnection`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "items": [
      {
        "can_be_kicked": "boolean",
        "descr": "string",
        "did": "string",
        "first_login_time": "string",
        "from": "string",
        "is_amfa": "boolean",
        "is_current_connected": "boolean",
        "is_otp_trusted": "boolean",
        "location": "string",
        "pid": "integer",
        "protocol": "string",
        "time": "string",
        "type": "string",
        "user_agent": "string",
        "user_can_be_disabled": "boolean",
        "who": "string"
      }
    ],
    "systime": "string",
    "total": "integer"
  }
}
```

#### Method: `list`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.CurrentConnection`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "items": [
      {
        "can_be_kicked": "boolean",
        "descr": "string",
        "did": "string",
        "first_login_time": "string",
        "from": "string",
        "is_amfa": "boolean",
        "is_current_connected": "boolean",
        "is_otp_trusted": "boolean",
        "location": "string",
        "pid": "integer",
        "protocol": "string",
        "time": "string",
        "type": "string",
        "user_agent": "string",
        "user_can_be_disabled": "boolean",
        "who": "string"
      }
    ],
    "systime": "string",
    "total": "integer"
  }
}
```

## SYNO.Core.DSMNotify.MailContent

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

## SYNO.Core.DSMNotify.Strings

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.DSMNotify.Strings`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {}
}
```

## SYNO.Core.Desktop.Initdata

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Desktop.Initdata`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "ActionPrivilege": "array<empty>",
    "AppPrivilege": {
      "SYNO.ALLOW.ALL.APPLICATIONS": "boolean"
    },
    "CSSFiles": "array<string>",
    "GroupSettings": "null",
    "JSConfig": {
      "webman/3rdparty/AIConsole/dist/bundle.iife.js": {
        "SYNO.SDS.App.AI.Instance": "object"
      },
      "webman/3rdparty/AIConsole/dist/noop.js": {
        "SYNO.SDS.AI.Strings": "object"
      },
      "webman/3rdparty/ActiveBackup-GSuite/ActiveBackup-GSuite-activebackup-library-js.js": {
        "SYNO.SDS.ActiveBackupGSuiteLib.PkgVersion": "object",
        "SYNO.SDS.ActiveBackupGSuiteLib.Portal.AboutWindow": "object",
        "SYNO.SDS.ActiveBackupGSuiteLib.Portal.AppWindow": "object",
        "SYNO.SDS.ActiveBackupGSuiteLib.Portal.Component.AlertWindow": "object",
        "SYNO.SDS.ActiveBackupGSuiteLib.Portal.Component.Button": "object",
        "SYNO.SDS.ActiveBackupGSuiteLib.Portal.Component.Checkbox": "object",
        "SYNO.SDS.ActiveBackupGSuiteLib.Portal.Component.ComboBox": "object",
        "SYNO.SDS.ActiveBackupGSuiteLib.Portal.Component.ConfirmWindow": "object",
        "SYNO.SDS.ActiveBackupGSuiteLib.Portal.Component.DateField": "object",
        "SYNO.SDS.ActiveBackupGSuiteLib.Portal.Component.DropdownMenuButton": "object",
        "SYNO.SDS.ActiveBackupGSuiteLib.Portal.Component.FormComboBox": "object",
        "SYNO.SDS.ActiveBackupGSuiteLib.Portal.Component.FormDisplayField": "object",
        "SYNO.SDS.ActiveBackupGSuiteLib.Portal.Component.FormPanel": "object",
        "SYNO.SDS.ActiveBackupGSuiteLib.Portal.Component.GridPanel": "object",
        "SYNO.SDS.ActiveBackupGSuiteLib.Portal.Component.Menu": "object",
        "SYNO.SDS.ActiveBackupGSuiteLib.Portal.Component.MessageBoxV5": "object",
        "SYNO.SDS.ActiveBackupGSuiteLib.Portal.Component.ModalWindow": "object",
        "SYNO.SDS.ActiveBackupGSuiteLib.Portal.Component.PagingSet": "object",
        "SYNO.SDS.ActiveBackupGSuiteLib.Portal.Component.PagingToolbar": "object",
        "SYNO.SDS.ActiveBackupGSuiteLib.Portal.Component.Radio": "object",
        "SYNO.SDS.ActiveBackupGSuiteLib.Portal.Component.SplitButton": "object",
        "SYNO.SDS.ActiveBackupGSuiteLib.Portal.Component.TextField": "object",
        "SYNO.SDS.ActiveBackupGSuiteLib.Portal.Component.TextFilter": "object",
        "SYNO.SDS.ActiveBackupGSuiteLib.Portal.EmptyMask": "object",
        "SYNO.SDS.ActiveBackupGSuiteLib.Portal.Explore.HistoryManager": "object",
        "SYNO.SDS.ActiveBackupGSuiteLib.Portal.Explore.PathButton": "object",
        "SYNO.SDS.ActiveBackupGSuiteLib.Portal.Explorer.DriveTreePanel": "object",
        "SYNO.SDS.ActiveBackupGSuiteLib.Portal.Explorer.PathBar": "object",
        "SYNO.SDS.ActiveBackupGSuiteLib.Portal.Explorer.TimeIndicator": "object",
        "SYNO.SDS.ActiveBackupGSuiteLib.Portal.Explorer.Timeline": "object",
        "SYNO.SDS.ActiveBackupGSuiteLib.Portal.Explorer.TreePanel": "object",
        "SYNO.SDS.ActiveBackupGSuiteLib.Portal.MailPreview.Attachments": "object",
        "SYNO.SDS.ActiveBackupGSuiteLib.Portal.MailPreview.Body": "object",
        "SYNO.SDS.ActiveBackupGSuiteLib.Portal.MailPreview.SentTime": "object",
        "SYNO.SDS.ActiveBackupGSuiteLib.Portal.MailPreview.Window": "object",
        "SYNO.SDS.ActiveBackupGSuiteLib.Portal.RestoreStatusWindow": "object",
        "SYNO.SDS.ActiveBackupGSuiteLib.Portal.ServiceButton": "object",
        "SYNO.SDS.ActiveBackupGSuiteLib.Utils": "object",
        "SYNO.SDS.ActiveBackupGSuiteLib.component.QuickTip": "object",
        "SYNO.SDS.ActiveBackupGSuiteLib.component.QuickTips": "object",
        "SYNO.SDS.ActiveBackupGSuiteLib.core.App": "object",
        "SYNO.SDS.ActiveBackupGSuiteLib.core.Controller": "object",
        "SYNO.SDS.ActiveBackupGSuiteLib.core.Model": "object",
        "SYNO.SDS.ActiveBackupGSuiteLib.core.Widget": "object",
        "SYNO.SDS.ActiveBackupGSuiteLib.data.JsonStore": "object"
      },
      "webman/3rdparty/ActiveBackup-GSuite/ActiveBackup-GSuite-app.js": {
        "SYNO.SDS.ActiveBackupGSuite.Controller.ActivitiesPanel": "object",
        "SYNO.SDS.ActiveBackupGSuite.Controller.BasicUpdateServiceKeyWindow": "object",
        "SYNO.SDS.ActiveBackupGSuite.Controller.CreateWizard.AccountSetting.AccountManagementPanel": "object",
        "SYNO.SDS.ActiveBackupGSuite.Controller.CreateWizard.AccountSetting.MainWindow": "object",
        "SYNO.SDS.ActiveBackupGSuite.Controller.CreateWizard.AccountSetting.TeamDriveManagementPanel": "object",
        "SYNO.SDS.ActiveBackupGSuite.Controller.CreateWizard.AuthorizationPanel": "object",
        "SYNO.SDS.ActiveBackupGSuite.Controller.CreateWizard.AutoDiscoveryPanel": "object",
        "SYNO.SDS.ActiveBackupGSuite.Controller.CreateWizard.MainWindow": "object",
        "SYNO.SDS.ActiveBackupGSuite.Controller.CreateWizard.SelectTaskPanel": "object",
        "SYNO.SDS.ActiveBackupGSuite.Controller.CreateWizard.SummaryPanel": "object",
        "SYNO.SDS.ActiveBackupGSuite.Controller.CreateWizard.TaskSettingsPanel": "object",
        "SYNO.SDS.ActiveBackupGSuite.Controller.CreateWizard.VersionControlPanel": "object",
        "SYNO.SDS.ActiveBackupGSuite.Controller.CurrentActivities": "object",
        "SYNO.SDS.ActiveBackupGSuite.Controller.DetailInfoWindow.UserStatusPanel": "object",
        "SYNO.SDS.ActiveBackupGSuite.Controller.LastBackupStatus": "object",
        "SYNO.SDS.ActiveBackupGSuite.Controller.LastEventLog": "object",
        "SYNO.SDS.ActiveBackupGSuite.Controller.LogDetailWindow.LogGridnPanel": "object",
        "SYNO.SDS.ActiveBackupGSuite.Controller.LogDetailWindow.MainWindow": "object",
        "SYNO.SDS.ActiveBackupGSuite.Controller.LogDetailWindow.RestoreTaskInformationPanel": "object",
        "SYNO.SDS.ActiveBackupGSuite.Controller.LogDetailWindow.TaskInformationPanel": "object",
        "SYNO.SDS.ActiveBackupGSuite.Controller.LogPanel": "object",
        "SYNO.SDS.ActiveBackupGSuite.Controller.MainWindow": "object",
        "SYNO.SDS.ActiveBackupGSuite.Controller.OverViewHistogramPanel": "object",
        "SYNO.SDS.ActiveBackupGSuite.Controller.OverViewInformation": "object",
        "SYNO.SDS.ActiveBackupGSuite.Controller.OverViewLegendPanel": "object",
        "SYNO.SDS.ActiveBackupGSuite.Controller.OverViewPanel": "object",
        "SYNO.SDS.ActiveBackupGSuite.Controller.OverViewStatisticPanel": "object",
        "SYNO.SDS.ActiveBackupGSuite.Controller.ReauthWindow": "object",
        "SYNO.SDS.ActiveBackupGSuite.Controller.RestoreWindow.MainWindow": "object",
        "SYNO.SDS.ActiveBackupGSuite.Controller.RestoreWindow.RestoreInformationPanel": "object",
        "SYNO.SDS.ActiveBackupGSuite.Controller.ServiceDetailWindow.AllLogPanel": "object",
        "SYNO.SDS.ActiveBackupGSuite.Controller.ServiceDetailWindow.CalendarLogPanel": "object",
        "SYNO.SDS.ActiveBackupGSuite.Controller.ServiceDetailWindow.ContactLogPanel": "object",
        "SYNO.SDS.ActiveBackupGSuite.Controller.ServiceDetailWindow.FileLogPanel": "object",
        "SYNO.SDS.ActiveBackupGSuite.Controller.ServiceDetailWindow.LogPanel": "object",
        "SYNO.SDS.ActiveBackupGSuite.Controller.ServiceDetailWindow.MailLogPanel": "object",
        "SYNO.SDS.ActiveBackupGSuite.Controller.ServiceDetailWindow.MainWindow": "object",
        "SYNO.SDS.ActiveBackupGSuite.Controller.ServiceDetailWindow.UserStatusPanel": "object",
        "SYNO.SDS.ActiveBackupGSuite.Controller.SettingsTabPanel.AccountManagementPanel": "object",
        "SYNO.SDS.ActiveBackupGSuite.Controller.SettingsTabPanel.MainWindow": "object",
        "SYNO.SDS.ActiveBackupGSuite.Controller.SettingsTabPanel.RotationPanel": "object",
        "SYNO.SDS.ActiveBackupGSuite.Controller.SettingsTabPanel.TaskSettingsPanel": "object",
        "SYNO.SDS.ActiveBackupGSuite.Controller.SettingsTabPanel.TeamDriveManagementPanel": "object",
        "SYNO.SDS.ActiveBackupGSuite.Controller.StorageUsage": "object",
        "SYNO.SDS.ActiveBackupGSuite.Controller.TaskListPanel": "object",
        "SYNO.SDS.ActiveBackupGSuite.Controller.TrendUsage": "object",
        "SYNO.SDS.ActiveBackupGSuite.Controller.UpdateAppSettingWindow": "object",
        "SYNO.SDS.ActiveBackupGSuite.Controller.UpdateServiceKeyWindow": "object",
        "SYNO.SDS.ActiveBackupGSuite.Controller.UserService": "object",
        "SYNO.SDS.ActiveBackupGSuite.Controller.UserUsage": "object",
        "SYNO.SDS.ActiveBackupGSuite.Histogram.BaseChart": "object",
        "SYNO.SDS.ActiveBackupGSuite.Histogram.StageBarChart": "object",
        "SYNO.SDS.ActiveBackupGSuite.Instance": "object",
        "SYNO.SDS.ActiveBackupGSuite.LegendContainer.Legend": "object",
        "SYNO.SDS.ActiveBackupGSuite.Model.AccountManagementGrid": "object",
        "SYNO.SDS.ActiveBackupGSuite.Model.ActivitiesList": "object",
        "SYNO.SDS.ActiveBackupGSuite.Model.AdvancedSearchField": "object",
        "SYNO.SDS.ActiveBackupGSuite.Model.BackupTaskListSlim": "object",
        "SYNO.SDS.ActiveBackupGSuite.Model.CurrentActivitiesContainer": "object",
        "SYNO.SDS.ActiveBackupGSuite.Model.CurrentActivitiesGrid": "object",
        "\u2026": "+88 more keys"
      },
      "webman/3rdparty/ActiveBackup-GSuite/ActiveBackup-GSuite-lib-util.js": {
        "SYNO.SDS.ActiveBackupGSuite.ErrorCode": "object",
        "SYNO.SDS.ActiveBackupGSuite.Utils": "object",
        "SYNO.SDS.ActiveBackupGSuiteLib.CUS": "object"
      },
      "webman/3rdparty/ActiveBackup-GSuite/ActiveBackup-GSuite-portal.js": {
        "SYNO.SDS.ActiveBackupGSuite.Portal.CalendarExplorer": "object",
        "SYNO.SDS.ActiveBackupGSuite.Portal.CalendarRestoreStatusWindow": "object",
        "SYNO.SDS.ActiveBackupGSuite.Portal.ChooseDomainUserWindow": "object",
        "SYNO.SDS.ActiveBackupGSuite.Portal.ChooseUserWindow": "object",
        "SYNO.SDS.ActiveBackupGSuite.Portal.ConfirmRestoreWindow": "object",
        "SYNO.SDS.ActiveBackupGSuite.Portal.ContactExplorer": "object",
        "SYNO.SDS.ActiveBackupGSuite.Portal.ContactPreviewContainer": "object",
        "SYNO.SDS.ActiveBackupGSuite.Portal.ContactRestoreStatusWindow": "object",
        "SYNO.SDS.ActiveBackupGSuite.Portal.ContactSelectionContainer": "object",
        "SYNO.SDS.ActiveBackupGSuite.Portal.ContactViewPanel": "object",
        "SYNO.SDS.ActiveBackupGSuite.Portal.DEBUG": "object",
        "SYNO.SDS.ActiveBackupGSuite.Portal.DriveButton": "object",
        "SYNO.SDS.ActiveBackupGSuite.Portal.DriveConfirmRestoreWindow": "object",
        "SYNO.SDS.ActiveBackupGSuite.Portal.DriveExplorer": "object",
        "SYNO.SDS.ActiveBackupGSuite.Portal.DrivePathBar": "object",
        "SYNO.SDS.ActiveBackupGSuite.Portal.DriveRestoreStatusWindow": "object",
        "SYNO.SDS.ActiveBackupGSuite.Portal.DriveTreePanel": "object",
        "SYNO.SDS.ActiveBackupGSuite.Portal.HeaderBar": "object",
        "SYNO.SDS.ActiveBackupGSuite.Portal.Instance": "object",
        "SYNO.SDS.ActiveBackupGSuite.Portal.ItemListWindow": "object",
        "SYNO.SDS.ActiveBackupGSuite.Portal.ItemRestoreStatusWindow": "object",
        "SYNO.SDS.ActiveBackupGSuite.Portal.MailConfirmRestoreWindow": "object",
        "SYNO.SDS.ActiveBackupGSuite.Portal.MailExplorer": "object",
        "SYNO.SDS.ActiveBackupGSuite.Portal.MailItemListWindow": "object",
        "SYNO.SDS.ActiveBackupGSuite.Portal.MailPreviewWindow": "object",
        "SYNO.SDS.ActiveBackupGSuite.Portal.MailRestoreStatusWindow": "object",
        "SYNO.SDS.ActiveBackupGSuite.Portal.MailSearchPanel": "object",
        "SYNO.SDS.ActiveBackupGSuite.Portal.MainWindow": "object",
        "SYNO.SDS.ActiveBackupGSuite.Portal.RestoreStatusWindow": "object"
      },
      "webman/3rdparty/ActiveBackup-Portal/ActiveBackup-app.js": {
        "SYNO.SDS.ActiveBackupPortal.AboutWindow": "object",
        "SYNO.SDS.ActiveBackupPortal.AgentDestinationTreeLoader": "object",
        "SYNO.SDS.ActiveBackupPortal.Application": "object",
        "SYNO.SDS.ActiveBackupPortal.Comp.FolderTreeLoader": "object",
        "SYNO.SDS.ActiveBackupPortal.Comp.TreeLoader": "object",
        "SYNO.SDS.ActiveBackupPortal.Comp.TreeNodeUI": "object",
        "SYNO.SDS.ActiveBackupPortal.Comp.TreeRootNodeUI": "object",
        "SYNO.SDS.ActiveBackupPortal.Comp.TreeSubNodeUI": "object",
        "SYNO.SDS.ActiveBackupPortal.Controller.ActionBase": "object",
        "SYNO.SDS.ActiveBackupPortal.Controller.Base": "object",
        "SYNO.SDS.ActiveBackupPortal.Controller.Env": "object",
        "SYNO.SDS.ActiveBackupPortal.Controller.Event": "object",
        "SYNO.SDS.ActiveBackupPortal.Controller.FileAction": "object",
        "SYNO.SDS.ActiveBackupPortal.Controller.History": "object",
        "SYNO.SDS.ActiveBackupPortal.Controller.Navigation": "object",
        "SYNO.SDS.ActiveBackupPortal.Controller.TaskAction": "object",
        "SYNO.SDS.ActiveBackupPortal.DecryptDialog": "object",
        "SYNO.SDS.ActiveBackupPortal.DecryptPanel": "object",
        "SYNO.SDS.ActiveBackupPortal.DestinationExplorer": "object",
        "SYNO.SDS.ActiveBackupPortal.DestinationTreeLoader": "object",
        "SYNO.SDS.ActiveBackupPortal.DestinationTreePanel": "object",
        "SYNO.SDS.ActiveBackupPortal.DeviceComboBox": "object",
        "SYNO.SDS.ActiveBackupPortal.DevicePanel": "object",
        "SYNO.SDS.ActiveBackupPortal.EmptyMask": "object",
        "SYNO.SDS.ActiveBackupPortal.Explorer.GridPanel": "object",
        "SYNO.SDS.ActiveBackupPortal.Explorer.MainPanel": "object",
        "SYNO.SDS.ActiveBackupPortal.Explorer.Path": "object",
        "SYNO.SDS.ActiveBackupPortal.Explorer.PathBar": "object",
        "SYNO.SDS.ActiveBackupPortal.Explorer.PathButton": "object",
        "SYNO.SDS.ActiveBackupPortal.Explorer.TopPanel": "object",
        "SYNO.SDS.ActiveBackupPortal.Explorer.TreePanel": "object",
        "SYNO.SDS.ActiveBackupPortal.MainPanel": "object",
        "SYNO.SDS.ActiveBackupPortal.MainWindow": "object",
        "SYNO.SDS.ActiveBackupPortal.RestoreDetail": "object",
        "SYNO.SDS.ActiveBackupPortal.RestoreDetailDialog": "object",
        "SYNO.SDS.ActiveBackupPortal.RestorePanel": "object",
        "SYNO.SDS.ActiveBackupPortal.RestoreTaskDialog": "object",
        "SYNO.SDS.ActiveBackupPortal.Storage.VerificationDialog": "object",
        "SYNO.SDS.ActiveBackupPortal.Storage.VerificationPanel": "object",
        "SYNO.SDS.ActiveBackupPortal.Store.File": "object",
        "SYNO.SDS.ActiveBackupPortal.Store.RestoreTask": "object",
        "SYNO.SDS.ActiveBackupPortal.Store.Task": "object",
        "SYNO.SDS.ActiveBackupPortal.Store.User": "object",
        "SYNO.SDS.ActiveBackupPortal.TaskDialog": "object",
        "SYNO.SDS.ActiveBackupPortal.TaskPanel": "object",
        "SYNO.SDS.ActiveBackupPortal.Timeline": "object",
        "SYNO.SDS.ActiveBackupPortal.TopToolbar": "object",
        "SYNO.SDS.ActiveBackupPortal.UserDialog": "object",
        "SYNO.SDS.ActiveBackupPortal.UserPanel": "object",
        "SYNO.SDS.ActiveBackupPortal.VM.CredentialPanel": "object",
        "SYNO.SDS.ActiveBackupPortal.VM.DestinationLoader": "object",
        "SYNO.SDS.ActiveBackupPortal.VM.DestinationPanel": "object",
        "SYNO.SDS.ActiveBackupPortal.VM.RestoreWizard": "object",
        "SYNO.SDS.ActiveBackupPortal.VersionMenu": "object"
      },
      "webman/3rdparty/ActiveBackup-Portal/ActiveBackup-framework.js": {
        "SYNO.SDS.ActiveBackupPortal.AppInstance": "object",
        "SYNO.SDS.ActiveBackupPortal.AppWindow": "object",
        "SYNO.SDS.ActiveBackupPortal.GridBufferView": "object",
        "SYNO.SDS.ActiveBackupPortal.ModalWindow": "object",
        "SYNO.SDS.ActiveBackupPortal.Store.Base": "object",
        "SYNO.SDS.ActiveBackupPortal.TextFilter": "object",
        "SYNO.SDS.ActiveBackupPortal.Wizard.ModalWindow": "object"
      },
      "webman/3rdparty/ActiveBackup-Portal/ActiveBackup-utils.js": {
        "SYNO.ActiveBackupPortal.Adapter": "object",
        "SYNO.ActiveBackupPortal.GridStatePlugin": "object",
        "SYNO.ActiveBackupPortal.StateGridPanel": "object",
        "SYNO.SDS.ActiveBackupPortal.AppUtils": "object",
        "SYNO.SDS.ActiveBackupPortal.Defines": "object",
        "SYNO.SDS.ActiveBackupPortal.Errors": "object",
        "SYNO.SDS.ActiveBackupPortal.Utils": "object"
      },
      "webman/3rdparty/ActiveBackup-Portal/ActiveBackup-webapi.js": {
        "SYNO.SDS.ActiveBackupPortal.WebAPI.Core": "object",
        "SYNO.SDS.ActiveBackupPortal.WebAPI.Description": "object"
      },
      "webman/3rdparty/ActiveBackup/activebackup.js": {
        "SYNO.ActiveBackup.Activation.OfflineStep": "object",
        "SYNO.ActiveBackup.Activation.WelcomeStep": "object",
        "SYNO.ActiveBackup.Activation.Wizard": "object",
        "SYNO.ActiveBackup.Adapter": "object",
        "SYNO.ActiveBackup.AdminDelegationPanel": "object",
        "SYNO.ActiveBackup.Agent.AddDeviceCertPanel": "object",
        "SYNO.ActiveBackup.Agent.AddDeviceCertWindow": "object",
        "SYNO.ActiveBackup.Agent.AddDevicePanel": "object",
        "SYNO.ActiveBackup.Agent.AddDeviceWizard": "object",
        "SYNO.ActiveBackup.Agent.AdvanceSettingCreateWizardPanel": "object",
        "SYNO.ActiveBackup.Agent.AdvanceSettingPanel": "object",
        "SYNO.ActiveBackup.Agent.BatchEditBox": "object",
        "SYNO.ActiveBackup.Agent.BatchEditBoxWrapper": "object",
        "SYNO.ActiveBackup.Agent.ClientVolumePanel": "object",
        "SYNO.ActiveBackup.Agent.ClientVolumeWindow": "object",
        "SYNO.ActiveBackup.Agent.ConfigureTaskSettingPanel": "object",
        "SYNO.ActiveBackup.Agent.DSMDeviceView": "object",
        "SYNO.ActiveBackup.Agent.DataTransferSettingPanel": "object",
        "SYNO.ActiveBackup.Agent.DeviceSelectGridPanel": "object",
        "SYNO.ActiveBackup.Agent.DeviceSelectPanel": "object",
        "SYNO.ActiveBackup.Agent.DeviceSettingPanel": "object",
        "SYNO.ActiveBackup.Agent.DeviceView": "object",
        "SYNO.ActiveBackup.Agent.GeneralEditPanel": "object",
        "SYNO.ActiveBackup.Agent.LinuxDeviceView": "object",
        "SYNO.ActiveBackup.Agent.MacDeviceView": "object",
        "SYNO.ActiveBackup.Agent.MacRecoveryToolGuideQRCodeDialog": "object",
        "SYNO.ActiveBackup.Agent.RecoveryMediaWindow": "object",
        "SYNO.ActiveBackup.Agent.ScriptPathField": "object",
        "SYNO.ActiveBackup.Agent.ScriptPathSetter": "object",
        "SYNO.ActiveBackup.Agent.ScriptPathTree": "object",
        "SYNO.ActiveBackup.Agent.ScriptSetter": "object",
        "SYNO.ActiveBackup.Agent.SourceTypePanel": "object",
        "SYNO.ActiveBackup.Agent.TaskCreateWizard": "object",
        "SYNO.ActiveBackup.Agent.TaskEditWizard": "object",
        "SYNO.ActiveBackup.Agent.TaskSummaryPanel": "object",
        "SYNO.ActiveBackup.Agent.TaskView": "object",
        "SYNO.ActiveBackup.Agent.WindowsDeviceView": "object",
        "SYNO.ActiveBackup.Agentless.AdvancedSettingPanel": "object",
        "SYNO.ActiveBackup.Agentless.AuthTypeMsgBox": "object",
        "SYNO.ActiveBackup.Agentless.BackupPolicyPanel": "object",
        "SYNO.ActiveBackup.Agentless.DeviceCreateWizard": "object",
        "SYNO.ActiveBackup.Agentless.DeviceEditWizard": "object",
        "SYNO.ActiveBackup.Agentless.DeviceSelectGridPanel": "object",
        "SYNO.ActiveBackup.Agentless.DeviceSelectPanel": "object",
        "SYNO.ActiveBackup.Agentless.DeviceView": "object",
        "SYNO.ActiveBackup.Agentless.Filter.Panel": "object",
        "SYNO.ActiveBackup.Agentless.Filter.TreeNodeUI": "object",
        "SYNO.ActiveBackup.Agentless.Filter.TreePanel": "object",
        "SYNO.ActiveBackup.Agentless.MachineTypePanel": "object",
        "SYNO.ActiveBackup.Agentless.RemoteInfomationPanel": "object",
        "SYNO.ActiveBackup.Agentless.ScheduleLite": "object",
        "SYNO.ActiveBackup.Agentless.ScheduleWizard": "object",
        "SYNO.ActiveBackup.Agentless.SourceSelectPanel": "object",
        "SYNO.ActiveBackup.Agentless.TaskCreateWizard": "object",
        "SYNO.ActiveBackup.Agentless.TaskEdit.GeneralPanel": "object",
        "SYNO.ActiveBackup.Agentless.TaskEditWizard": "object",
        "SYNO.ActiveBackup.Agentless.TaskSettingPanel": "object",
        "SYNO.ActiveBackup.Agentless.TaskSummaryPanel": "object",
        "SYNO.ActiveBackup.Agentless.TaskView": "object",
        "SYNO.ActiveBackup.AppInstance": "object",
        "\u2026": "+209 more keys"
      },
      "webman/3rdparty/ActiveInsight/Bundle.js": {
        "SYNO.SDS.ActiveInsight.FileActivity.TruncateDatabase.BackgroundTask": "object",
        "SYNO.SDS.ActiveInsight.Instance": "object"
      },
      "webman/3rdparty/CloudDownloader/CloudDownloader.js": {
        "SYNO.FileStation.CloudDownloader.Application": "object",
        "SYNO.FileStation.CloudDownloader.Utils": "object",
        "SYNO.FileStation.CloudDownloader.Utils.checkFn": "object",
        "SYNO.FileStation.CloudDownloader.Utils.launchFn": "object",
        "SYNO.FileStation.CloudDownloader.Utils.startDownload": "object",
        "SYNO.FileStation.CloudDownloader.Utils.supportDownloadAsType": "object"
      },
      "webman/3rdparty/ContainerManager/MainVue.js": {
        "SYNO.SDS.ContainerManager.Application": "object",
        "SYNO.SDS.Docker.Modals.Capabilities": "object",
        "SYNO.SDS.Docker.Project.ProjectActionLogDialog": "object",
        "SYNO.SDS.Docker.Project.ProjectBuildDialog": "object",
        "SYNO.SDS.Docker.Project.ProjectCleanDialog": "object",
        "SYNO.SDS.Docker.Project.ProjectRestartDialog": "object",
        "SYNO.SDS.Docker.Project.ProjectStartDialog": "object",
        "SYNO.SDS.Docker.Project.ProjectStopDialog": "object"
      },
      "webman/3rdparty/ContainerManager/docker.js": {
        "SYNO.SDS.Docker.ContainerDetail.HotKeyForm": "object",
        "SYNO.SDS.Docker.ContainerDetail.HotKeys": "object",
        "SYNO.SDS.Docker.ContainerDetail.PanelTerm": "object",
        "SYNO.SDS.Docker.ContainerDetail.Term": "object",
        "SYNO.SDS.Docker.ContainerDetail.TermSocket": "object",
        "SYNO.SDS.Docker.Registry.TagDialog": "object",
        "SYNO.SDS.Docker.Utils.APILoadingDialog": "object",
        "SYNO.SDS.Docker.Utils.AliyunHub": "object",
        "SYNO.SDS.Docker.Utils.DockerHub": "object",
        "SYNO.SDS.Docker.Utils.Helper": "object",
        "SYNO.SDS.Docker.Utils.PreserveStates": "object",
        "SYNO.SDS.Docker.Utils.PromptDialog": "object",
        "SYNO.SDS.Docker.Utils.SearchField": "object",
        "SYNO.SDS.Docker.Utils.Shortcut": "object",
        "SYNO.SDS.Docker.Utils.Socket": "object",
        "SYNO.SDS.Docker.Utils.WelcomeDialog": "object"
      },
      "webman/3rdparty/ContainerManager/docker_no_check.js": {
        "SYNO.SDS.Docker.Term": "object"
      },
      "webman/3rdparty/FileBrowser/ExternViewer.js": {
        "SYNO.SDS.AccessFolder.FBExt": "object",
        "SYNO.SDS.AccessFolder.FBExt.checkFn": "object",
        "SYNO.SDS.AccessFolder.FBExt.launchFn": "object",
        "SYNO.SDS.GoogleDocsViewer.FBExt": "object",
        "SYNO.SDS.GoogleDocsViewer.FBExt.checkFn": "object",
        "SYNO.SDS.GoogleDocsViewer.FBExt.launchFn": "object",
        "SYNO.SDS.GoogleDriveEditor.FBExt": "object",
        "SYNO.SDS.GoogleDriveEditor.FBExt.checkFn": "object",
        "SYNO.SDS.GoogleDriveEditor.FBExt.launchFn": "object",
        "SYNO.SDS.OfficeViewer.FBExt": "object",
        "SYNO.SDS.OfficeViewer.FBExt.checkFn": "object",
        "SYNO.SDS.OfficeViewer.FBExt.launchFn": "object"
      },
      "webman/3rdparty/FileBrowser/FileBrowser.js": {
        "SYNO.FileStation.AdvSearchHistoryPanel": "object",
        "SYNO.FileStation.BandwidthConfig": "object",
        "SYNO.FileStation.BasicAction": "object",
        "SYNO.FileStation.BasicComp": "object",
        "SYNO.FileStation.BasicTabPanel": "object",
        "SYNO.FileStation.BasicTreePanel": "object",
        "SYNO.FileStation.BlobDownloadMgr": "object",
        "SYNO.FileStation.BlobDownloader": "object",
        "SYNO.FileStation.BufferViewFlexcrollPlugin": "object",
        "SYNO.FileStation.BufferViewFlexcrollPluginInstance": "object",
        "SYNO.FileStation.Clipboard": "object",
        "SYNO.FileStation.ColumnView": "object",
        "SYNO.FileStation.CompressAction": "object",
        "SYNO.FileStation.CompressDialog": "object",
        "SYNO.FileStation.CrtFdrDialog": "object",
        "SYNO.FileStation.CtxMenu": "object",
        "SYNO.FileStation.DeleteAction": "object",
        "SYNO.FileStation.DragDropHintDialog": "object",
        "SYNO.FileStation.EditFileRequestDialog": "object",
        "SYNO.FileStation.EditSharingDialog": "object",
        "SYNO.FileStation.ExtractAction": "object",
        "SYNO.FileStation.ExtractDialog": "object",
        "SYNO.FileStation.FavDialog": "object",
        "SYNO.FileStation.FileAction": "object",
        "SYNO.FileStation.FileRequestDialog": "object",
        "SYNO.FileStation.FocusGridPlugin": "object",
        "SYNO.FileStation.FocusGridPluginInstance": "object",
        "SYNO.FileStation.FocusPanelPlugin": "object",
        "SYNO.FileStation.FocusPanelPluginInstance": "object",
        "SYNO.FileStation.GridPanelFlexcrollPlugin": "object",
        "SYNO.FileStation.GridPanelFlexcrollPluginInstance": "object",
        "SYNO.FileStation.Lock.BaseDialog": "object",
        "SYNO.FileStation.Lock.ChangeStateDialog": "object",
        "SYNO.FileStation.Lock.ExtendRetentionDialog": "object",
        "SYNO.FileStation.Lock.LockDialog": "object",
        "SYNO.FileStation.Lock.Period": "object",
        "SYNO.FileStation.Lock.State": "object",
        "SYNO.FileStation.LockAction": "object",
        "SYNO.FileStation.LockConfirmDialog": "object",
        "SYNO.FileStation.MVCPAction": "object",
        "SYNO.FileStation.MVCPAskDialog": "object",
        "SYNO.FileStation.MainPanel": "object",
        "SYNO.FileStation.MixedTreePanel": "object",
        "SYNO.FileStation.MountConfig": "object",
        "SYNO.FileStation.MountISODialog": "object",
        "SYNO.FileStation.MountListDialog": "object",
        "SYNO.FileStation.MountRemoteDialog": "object",
        "SYNO.FileStation.MountRemoteDialog.MountCIFS": "object",
        "SYNO.FileStation.MountRemoteDialog.MountNFS": "object",
        "SYNO.FileStation.PathBar": "object",
        "SYNO.FileStation.ProtocolUserConfigDialog": "object",
        "SYNO.FileStation.RemoteConnection.ServerListDialog": "object",
        "SYNO.FileStation.RemoteConnection.Wizard": "object",
        "SYNO.FileStation.RenameDialog": "object",
        "SYNO.FileStation.SearchFormPanel": "object",
        "SYNO.FileStation.SearchHistoryPanel": "object",
        "SYNO.FileStation.SelTreeDialog": "object",
        "SYNO.FileStation.SelectAllRowSelectionModel": "object",
        "SYNO.FileStation.SettingDialog": "object",
        "SYNO.FileStation.SharingConfig": "object",
        "\u2026": "+23 more keys"
      },
      "webman/3rdparty/FileBrowser/FileBrowserUtil.js": {
        "SYNO.c2share.utils": "object",
        "SYNO.tiershare.utils": "object",
        "SYNO.webfm.utils": "object"
      },
      "webman/3rdparty/FileBrowser/FileProperty.js": {
        "SYNO.FileStation.PropertyDialog": "object"
      },
      "webman/3rdparty/FileBrowser/FileRequest.js": {
        "SYNO.FileStation.SharingUploadGrid.GridPanel": "object",
        "SYNO.FileStation.SharingUploadQueue.GridPanel": "object",
        "SYNO.SDS.App.SharingUpload.Application": "object",
        "SYNO.SDS.App.SharingUpload.MainWindow": "object"
      },
      "webman/3rdparty/FileBrowser/FileSaver.min.js": {
        "FileSaver": "object"
      },
      "webman/3rdparty/FileBrowser/FileTask.js": {
        "SYNO.FileStation.FileTask": "object"
      },
      "webman/3rdparty/FileBrowser/FileUploader.js": {
        "SYNO.FileStation.Action.Uploader": "object",
        "SYNO.FileStation.UploadDialog": "object",
        "SYNO.FileStation.Uploader.HTML5Uploader": "object",
        "SYNO.FileStation.Uploader.Uploader": "object"
      },
      "webman/3rdparty/FileBrowser/FolderSharingBase.js": {
        "SYNO.FileStation.BufferViewFlexcrollPlugin": "object",
        "SYNO.FileStation.BufferViewFlexcrollPluginInstance": "object",
        "SYNO.FileStation.FocusGridPlugin": "object",
        "SYNO.FileStation.FocusGridPluginInstance": "object",
        "SYNO.FileStation.GridPanelFlexcrollPlugin": "object",
        "SYNO.FileStation.GridPanelFlexcrollPluginInstance": "object",
        "SYNO.FileStation.PathBar": "object",
        "SYNO.FileStation.SelectAllRowSelectionModel": "object",
        "SYNO.FileStation.ThumbnailsView": "object",
        "SYNO.webfm.utils": "object"
      },
      "webman/3rdparty/FileBrowser/RecycleBin.js": {
        "SYNO.SDS.RecycleBin.Cleaner.FBExt": "object",
        "SYNO.SDS.RecycleBin.Cleaner.FBExt.checkFn": "object",
        "SYNO.SDS.RecycleBin.Cleaner.FBExt.launchFn": "object",
        "SYNO.SDS.RecycleBin.Restore.FBExt": "object",
        "SYNO.SDS.RecycleBin.Restore.FBExt.checkFn": "object",
        "SYNO.SDS.RecycleBin.Restore.FBExt.launchFn": "object"
      },
      "webman/3rdparty/FileBrowser/jszip.min.js": {
        "JSZip": "object"
      },
      "webman/3rdparty/FileTaskMonitor/MailTaskTray.js": {
        "SYNO.SDS.FileTaskMonitor.MailTaskTray.Panel": "object",
        "SYNO.SDS.FileTaskMonitor.MailTaskTray.TrayItem": "object"
      },
      "webman/3rdparty/FileTaskMonitor/TaskGrid.js": {
        "SYNO.SDS.FileTaskMonitor.MailMonitorGrid": "object"
      },
      "webman/3rdparty/FileTaskMonitor/UploadMonitor.js": {
        "SYNO.SDS.App.FileTaskMonitor": "object",
        "SYNO.SDS.App.FileTaskMonitor.Instance": "object",
        "SYNO.SDS.FileTaskMonitor.DownloadGrid": "object",
        "SYNO.SDS.FileTaskMonitor.DownloadTray.GridPanel": "object",
        "SYNO.SDS.FileTaskMonitor.DownloadTray.TrayItem": "object",
        "SYNO.SDS.FileTaskMonitor.UploadGrid": "object",
        "SYNO.SDS.FileTaskMonitor.UploadTray.GridPanel": "object",
        "SYNO.SDS.FileTaskMonitor.UploadTray.TrayItem": "object",
        "SYNO.SDS.UploadTray.GridPanel": "object"
      },
      "webman/3rdparty/FileTaskMonitor/UploadUtil.js": {
        "SYNO.FileStation.FormUploadAction": "object",
        "SYNO.FileStation.MonitorGrid": "object",
        "SYNO.FileStation.MonitorQueue.GridPanel": "object",
        "SYNO.FileStation.UploadGrid": "object"
      },
      "webman/3rdparty/HybridShare/C2FS.js": {
        "SYNO.SDS.C2FS.App.ConfigLoader": "object",
        "SYNO.SDS.C2FS.App.DownloadForDSMNotification": "object",
        "SYNO.SDS.C2FS.App.LaunchForDSMNotification": "object",
        "SYNO.SDS.C2FS.App.PinDownloadBackgroundTask": "object",
        "SYNO.SDS.C2FS.App.PopUpNotification": "object",
        "SYNO.SDS.C2FS.Application": "object",
        "SYNO.SDS.C2FS.DecryptBucketStep": "object",
        "SYNO.SDS.C2FS.EncryptBucketStep": "object",
        "SYNO.SDS.C2FS.File.LocalStatus": "object",
        "SYNO.SDS.C2FS.FileBrowser._IconWatchStore": "object",
        "SYNO.SDS.C2FS.FileBrowser.canPin": "object",
        "SYNO.SDS.C2FS.FileBrowser.canRetry": "object",
        "SYNO.SDS.C2FS.FileBrowser.canUnpin": "object",
        "SYNO.SDS.C2FS.FileBrowser.clearCacheIconWatches": "object",
        "SYNO.SDS.C2FS.FileBrowser.onPinClicked": "object",
        "SYNO.SDS.C2FS.FileBrowser.onRetryClicked": "object",
        "SYNO.SDS.C2FS.FileBrowser.onUnpinClicked": "object",
        "SYNO.SDS.C2FS.FileBrowser.watchForCacheIcons": "object",
        "SYNO.SDS.C2FS.FileBrowserExtension.Evict": "object",
        "SYNO.SDS.C2FS.FileBrowserExtension.Evict.enableIf": "object",
        "SYNO.SDS.C2FS.FileBrowserExtension.Evict.onClicked": "object",
        "SYNO.SDS.C2FS.FillBasicInfoStep": "object",
        "SYNO.SDS.C2FS.Helper": "object",
        "SYNO.SDS.C2FS.Helper.ErrorMap": "object",
        "SYNO.SDS.C2FS.Helper.GLOBAL_CONF": "object",
        "SYNO.SDS.C2FS.NPM": "object",
        "SYNO.SDS.C2FS.PermissionStep": "object",
        "SYNO.SDS.C2FS.SetC2FSStep": "object",
        "SYNO.SDS.C2FS.Share.AdvancedPermissionForm": "object",
        "SYNO.SDS.C2FS.Share.DefaultPermissionGrid": "object",
        "SYNO.SDS.C2FS.Share.EditDialog": "object",
        "SYNO.SDS.C2FS.Share.FullResync": "object",
        "SYNO.SDS.C2FS.Share.GeneralForm": "object",
        "SYNO.SDS.C2FS.Share.Issue": "object",
        "SYNO.SDS.C2FS.Share.NameTextField": "object",
        "SYNO.SDS.C2FS.Share.PermissionGrid": "object",
        "SYNO.SDS.C2FS.Share.RequiredDisplayField": "object",
        "SYNO.SDS.C2FS.Share.SetupC2FSForm": "object",
        "SYNO.SDS.C2FS.Share.Status": "object",
        "SYNO.SDS.C2FS.Share.Transform.BackgroundTask": "object",
        "SYNO.SDS.C2FS.Share.Transform.CSVExpoter": "object",
        "SYNO.SDS.C2FS.Share.Transform.CheckResultRecorder": "object",
        "SYNO.SDS.C2FS.Share.Transform.EncryptBucketStep": "object",
        "SYNO.SDS.C2FS.Share.Transform.FillBasicInfoStep": "object",
        "SYNO.SDS.C2FS.Share.Transform.HtmlExporter": "object",
        "SYNO.SDS.C2FS.Share.Transform.SummaryDiagram": "object",
        "SYNO.SDS.C2FS.Share.Transform.SummaryDiagramAfterShow": "object",
        "SYNO.SDS.C2FS.Share.Transform.SummaryDiagramOriginShow": "object",
        "SYNO.SDS.C2FS.Share.Transform.SummaryDiagramTitle": "object",
        "SYNO.SDS.C2FS.Share.Transform.SummaryDiagramTransitionShow": "object",
        "SYNO.SDS.C2FS.Share.Transform.SummaryStep": "object",
        "SYNO.SDS.C2FS.Share.Transform.ValidateStep": "object",
        "SYNO.SDS.C2FS.Share.Transform.WelcomeStep": "object",
        "SYNO.SDS.C2FS.Share.Transform.Wizard": "object",
        "SYNO.SDS.C2FS.Share.Utils": "object",
        "SYNO.SDS.C2FS.SummaryStep": "object",
        "SYNO.SDS.C2FS.UtilForDSM": "object",
        "SYNO.SDS.C2FS.Utils.C2WebHandler": "object",
        "SYNO.SDS.C2FS.Utils.FileExpoter": "object",
        "SYNO.SDS.C2FS.Utils.LocalStatusWatch.WatchStoreInterface": "object",
        "\u2026": "+6 more keys"
      },
      "webman/3rdparty/HyperBackup/addon.js": {
        "SYNO.Backup.Addon.Cloud.base.Task.SettingPanel": "object",
        "SYNO.Backup.Addon.Config.addon_list": "object",
        "SYNO.Backup.Addon.Legacy.base.Task.SettingPanel": "object",
        "SYNO.Backup.Addon.Util.getClass": "object",
        "SYNO.Backup.Addon.Util.getFunc": "object",
        "SYNO.Backup.Addon.Util.getID": "object",
        "SYNO.Backup.Addon.Util.getInfo": "object",
        "SYNO.Backup.Addon.Util.getString": "object",
        "SYNO.Backup.Addon.amazon_cloud_drive.Destination.SettingPanel": "object",
        "SYNO.Backup.Addon.amazon_cloud_drive.Destination.getInfo": "object",
        "SYNO.Backup.Addon.amazon_cloud_drive.Restore.DestStep": "object",
        "SYNO.Backup.Addon.amazon_cloud_drive.Task.SettingPanel": "object",
        "SYNO.Backup.Addon.aws_s3.Destination.EditPanel": "object",
        "SYNO.Backup.Addon.aws_s3.Destination.SettingPanel": "object",
        "SYNO.Backup.Addon.aws_s3.Destination.getInfo": "object",
        "SYNO.Backup.Addon.aws_s3.Restore.DestStep": "object",
        "SYNO.Backup.Addon.aws_s3.Task.SettingPanel": "object",
        "SYNO.Backup.Addon.azure_blob.Destination.EditPanel": "object",
        "SYNO.Backup.Addon.azure_blob.Destination.SettingPanel": "object",
        "SYNO.Backup.Addon.azure_blob.Destination.getInfo": "object",
        "SYNO.Backup.Addon.azure_blob.Restore.DestStep": "object",
        "SYNO.Backup.Addon.azure_blob.Task.SettingPanel": "object",
        "SYNO.Backup.Addon.azure_cn_blob.Destination.EditPanel": "object",
        "SYNO.Backup.Addon.azure_cn_blob.Destination.SettingPanel": "object",
        "SYNO.Backup.Addon.azure_cn_blob.Destination.getInfo": "object",
        "SYNO.Backup.Addon.azure_cn_blob.Task.SettingPanel": "object",
        "SYNO.Backup.Addon.base.Destination.EditPanel": "object",
        "SYNO.Backup.Addon.base.Destination.SettingPanel": "object",
        "SYNO.Backup.Addon.base.Destination.getInfo": "object",
        "SYNO.Backup.Addon.base.Restore.DestStep": "object",
        "SYNO.Backup.Addon.base.Task.SettingPanel": "object",
        "SYNO.Backup.Addon.dropbox.Destination.SettingPanel": "object",
        "SYNO.Backup.Addon.dropbox.Destination.getInfo": "object",
        "SYNO.Backup.Addon.dropbox.Restore.DestStep": "object",
        "SYNO.Backup.Addon.dropbox.Task.SettingPanel": "object",
        "SYNO.Backup.Addon.google_drive.Destination.SettingPanel": "object",
        "SYNO.Backup.Addon.google_drive.Destination.getInfo": "object",
        "SYNO.Backup.Addon.google_drive.Restore.DestStep": "object",
        "SYNO.Backup.Addon.google_drive.Task.SettingPanel": "object",
        "SYNO.Backup.Addon.hicloud_s3.Destination.EditPanel": "object",
        "SYNO.Backup.Addon.hicloud_s3.Destination.SettingPanel": "object",
        "SYNO.Backup.Addon.hicloud_s3.Destination.getInfo": "object",
        "SYNO.Backup.Addon.hicloud_s3.Restore.DestStep": "object",
        "SYNO.Backup.Addon.hicloud_s3.Task.SettingPanel": "object",
        "SYNO.Backup.Addon.hidrive.Destination.EditPanel": "object",
        "SYNO.Backup.Addon.hidrive.Destination.SettingPanel": "object",
        "SYNO.Backup.Addon.hidrive.Destination.getInfo": "object",
        "SYNO.Backup.Addon.hidrive.Restore.DestStep": "object",
        "SYNO.Backup.Addon.hidrive.Task.SettingPanel": "object",
        "SYNO.Backup.Addon.hubic.Destination.SettingPanel": "object",
        "SYNO.Backup.Addon.hubic.Destination.getInfo": "object",
        "SYNO.Backup.Addon.hubic.Restore.DestStep": "object",
        "SYNO.Backup.Addon.hubic.Task.SettingPanel": "object",
        "SYNO.Backup.Addon.ibm_softlayer.Destination.EditPanel": "object",
        "SYNO.Backup.Addon.ibm_softlayer.Destination.SettingPanel": "object",
        "SYNO.Backup.Addon.ibm_softlayer.Destination.getInfo": "object",
        "SYNO.Backup.Addon.ibm_softlayer.Restore.DestStep": "object",
        "SYNO.Backup.Addon.ibm_softlayer.Task.SettingPanel": "object",
        "SYNO.Backup.Addon.jdcloud_s3.Destination.EditPanel": "object",
        "SYNO.Backup.Addon.jdcloud_s3.Destination.SettingPanel": "object",
        "\u2026": "+86 more keys"
      },
      "webman/3rdparty/HyperBackup/backup.js": {
        "SYNO.SDS.Backup.AppGridPanel": "object",
        "SYNO.SDS.Backup.AppParamsPanel": "object",
        "SYNO.SDS.Backup.Application": "object",
        "SYNO.SDS.Backup.BackupTypePanel": "object",
        "SYNO.SDS.Backup.BaseTaskSourceSelector": "object",
        "SYNO.SDS.Backup.C2CloudEditSchedulePanel": "object",
        "SYNO.SDS.Backup.DataRepoTypePanel": "object",
        "SYNO.SDS.Backup.EditSchedulePanel": "object",
        "SYNO.SDS.Backup.EditSourcePanel": "object",
        "SYNO.SDS.Backup.EditSourcePanelWrapper": "object",
        "SYNO.SDS.Backup.EmptyPage": "object",
        "SYNO.SDS.Backup.EntireDSMRepoTypePanel": "object",
        "SYNO.SDS.Backup.LUNDestEditPanel": "object",
        "SYNO.SDS.Backup.LUNDestTypePanel": "object",
        "SYNO.SDS.Backup.LUNEditDialog": "object",
        "SYNO.SDS.Backup.LUNResTypePanel": "object",
        "SYNO.SDS.Backup.MainWindow": "object",
        "SYNO.SDS.Backup.RepoTypePanel": "object",
        "SYNO.SDS.Backup.Restore.AppStep": "object",
        "SYNO.SDS.Backup.Restore.AppUtil": "object",
        "SYNO.SDS.Backup.Restore.BasicRestoreWizard": "object",
        "SYNO.SDS.Backup.Restore.ConfigStep": "object",
        "SYNO.SDS.Backup.Restore.IssueStageView": "object",
        "SYNO.SDS.Backup.Restore.LunProgressPanel": "object",
        "SYNO.SDS.Backup.Restore.LunProgressView": "object",
        "SYNO.SDS.Backup.Restore.LunProgressWindow": "object",
        "SYNO.SDS.Backup.Restore.MainBranch": "object",
        "SYNO.SDS.Backup.Restore.MultiVerLunProgressPanel": "object",
        "SYNO.SDS.Backup.Restore.MultiVerLunProgressView": "object",
        "SYNO.SDS.Backup.Restore.MultiVerLunProgressWindow": "object",
        "SYNO.SDS.Backup.Restore.ProgressPanel": "object",
        "SYNO.SDS.Backup.Restore.ProgressView": "object",
        "SYNO.SDS.Backup.Restore.ProgressWindow": "object",
        "SYNO.SDS.Backup.Restore.RepoTypePanel": "object",
        "SYNO.SDS.Backup.Restore.RestoreListView": "object",
        "SYNO.SDS.Backup.Restore.RestoreWizard": "object",
        "SYNO.SDS.Backup.Restore.SelectMultiVerLunStep": "object",
        "SYNO.SDS.Backup.Restore.ShareStep": "object",
        "SYNO.SDS.Backup.Restore.SuccessStageView": "object",
        "SYNO.SDS.Backup.RestoreTypePanel": "object",
        "SYNO.SDS.Backup.RotationParamsPanel": "object",
        "SYNO.SDS.Backup.SchedulePanel": "object",
        "SYNO.SDS.Backup.SelectBackupDestination": "object",
        "SYNO.SDS.Backup.SelectSingleOrMultiple": "object",
        "SYNO.SDS.Backup.SummaryPanel": "object",
        "SYNO.SDS.Backup.Task.DataMainPage": "object",
        "SYNO.SDS.Backup.Task.LunMainPage": "object",
        "SYNO.SDS.Backup.Task.MainPage": "object",
        "SYNO.SDS.Backup.Task.SubPanel": "object",
        "SYNO.SDS.Backup.TaskCreateWizard": "object",
        "SYNO.SDS.Backup.TaskEditDialog": "object",
        "SYNO.SDS.Backup.TaskImportWizard": "object",
        "SYNO.SDS.Backup.TaskSourceContainer": "object",
        "SYNO.SDS.Backup.TaskSourceContainerWrapper": "object",
        "SYNO.SDS.Backup.TaskSourceQuadSelector": "object",
        "SYNO.SDS.Backup.TaskSourceTriSelector": "object",
        "SYNO.SDS.Backup.VersionFileTree": "object",
        "SYNO.SDS.Backup.VersionSelector": "object",
        "SYNO.SDS.LunBackup": "object"
      },
      "webman/3rdparty/HyperBackup/backupwidget.js": {
        "SYNO.SDS.Backup.ScheduleBackupWidget": "object"
      },
      "webman/3rdparty/HyperBackup/common.js": {
        "SYNO.SDS.Backup.Client.Common.ErrorReportWindow": "object",
        "SYNO.SDS.Backup.Client.Common.FilterSetting": "object",
        "SYNO.SDS.Backup.Client.Common.FilterSettingWindow": "object",
        "SYNO.SDS.Backup.Client.Common.FormPanel": "object",
        "SYNO.SDS.Backup.Client.Common.Log..LogsPage": "object",
        "SYNO.SDS.Backup.Client.Common.Log.AdvancedSearchField": "object",
        "SYNO.SDS.Backup.Client.Common.Log.BaseLog": "object",
        "SYNO.SDS.Backup.Client.Common.Log.BaseLogUI": "object",
        "SYNO.SDS.Backup.Client.Common.Log.GeneralLogBuilder": "object",
        "SYNO.SDS.Backup.Client.Common.Log.LogsWindow": "object",
        "SYNO.SDS.Backup.Client.Common.Log.SearchFormPanel": "object",
        "SYNO.SDS.Backup.Client.Common.Password.Window": "object",
        "SYNO.SDS.Backup.Client.Common.QuickTip": "object",
        "SYNO.SDS.Backup.Client.Common.QuickTips": "object",
        "SYNO.SDS.Backup.Client.Common.RetentionSetting.CustomizedPanel": "object",
        "SYNO.SDS.Backup.Client.Common.RetentionSetting.CustomizedWindow": "object",
        "SYNO.SDS.Backup.Client.Common.Space.Chart": "object",
        "SYNO.SDS.Backup.Client.Common.Space.Legend": "object",
        "SYNO.SDS.Backup.Client.Common.Space.PieChart": "object",
        "SYNO.SDS.Backup.Client.Common.Statistic.MainWindow": "object",
        "SYNO.SDS.Backup.Client.Common.Statistic.SourceChangeLineChart": "object",
        "SYNO.SDS.Backup.Client.Common.Statistic.SourceChangePanel": "object",
        "SYNO.SDS.Backup.Client.Common.Statistic.SourceLineChart": "object",
        "SYNO.SDS.Backup.Client.Common.Statistic.SourcePanel": "object",
        "SYNO.SDS.Backup.Client.Common.Statistic.TargetLineChart": "object",
        "SYNO.SDS.Backup.Client.Common.Statistic.TargetPanel": "object",
        "SYNO.SDS.Backup.Client.Common.Statistic.TargetParamsPanel": "object",
        "SYNO.SDS.Backup.Client.Common.Tag": "object",
        "SYNO.SDS.Backup.Client.Common.Utils.AccountMeta": "object",
        "SYNO.SDS.Backup.Client.Common.Utils.AddTip": "object",
        "SYNO.SDS.Backup.Client.Common.Utils.DateScheduleToString": "object",
        "SYNO.SDS.Backup.Client.Common.Utils.DateTimeFormatter": "object",
        "SYNO.SDS.Backup.Client.Common.Utils.GenWeekString": "object",
        "SYNO.SDS.Backup.Client.Common.Utils.GetErrorString": "object",
        "SYNO.SDS.Backup.Client.Common.Utils.GetString": "object",
        "SYNO.SDS.Backup.Client.Common.Utils.TimeScheduleToString": "object",
        "SYNO.SDS.Backup.Client.Common.Utils.WeekArray": "object",
        "SYNO.SDS.Backup.Client.Common.Utils.createAccountMeta": "object",
        "SYNO.SDS.Backup.Client.Common.Utils.getConvertSize": "object",
        "SYNO.SDS.Backup.Client.Common.Utils.getDSMStyleDateTimeString": "object",
        "SYNO.SDS.Backup.Client.Common.Utils.getPercentage": "object",
        "SYNO.SDS.Backup.Client.Common.Utils.getRepoTargetPermissionMsg": "object",
        "SYNO.SDS.Backup.Client.Common.Utils.getScheduleStr": "object",
        "SYNO.SDS.Backup.Client.Common.Utils.getUnit": "object",
        "SYNO.SDS.Backup.Client.Common.Utils.htmlEncodeTip": "object",
        "SYNO.SDS.Backup.Client.Common.Utils.observeEvent": "object",
        "SYNO.SDS.Backup.Client.Common.Version.MainWindow": "object",
        "SYNO.SDS.Backup.Client.Common.Version.SourceInfoPanel": "object",
        "SYNO.SDS.Backup.Client.Common.Version.VersionInfoPanel": "object",
        "SYNO.SDS.Backup.Client.Common.Version.VersionInfoWindow": "object"
      },
      "webman/3rdparty/HyperBackup/component.js": {
        "SYNO.SDS.Backup.ApiHelper": "object",
        "SYNO.SDS.Backup.BasicTreePanel": "object",
        "SYNO.SDS.Backup.ComboBox": "object",
        "SYNO.SDS.Backup.ComboBoxAndDisplayField": "object",
        "SYNO.SDS.Backup.EnableColumn": "object",
        "SYNO.SDS.Backup.ExpandableListView": "object",
        "SYNO.SDS.Backup.FormPanel": "object",
        "SYNO.SDS.Backup.HotTiering.ConfirmDialog": "object",
        "SYNO.SDS.Backup.IntegrityCheckSchedulePanel": "object",
        "SYNO.SDS.Backup.ModuleList": "object",
        "SYNO.SDS.Backup.NewFeaturePanel": "object",
        "SYNO.SDS.Backup.PageListAppWindow": "object",
        "SYNO.SDS.Backup.PathBar": "object",
        "SYNO.SDS.Backup.QuadTreeNodeEmptyState": "object",
        "SYNO.SDS.Backup.QuadTreeNodeFullState": "object",
        "SYNO.SDS.Backup.QuadTreeNodePartialState": "object",
        "SYNO.SDS.Backup.QuadTreeNodeState": "object",
        "SYNO.SDS.Backup.QuadTreeNodeUI": "object",
        "SYNO.SDS.Backup.QuadTreePanel": "object",
        "SYNO.SDS.Backup.RepoTypeButton": "object",
        "SYNO.SDS.Backup.SimpleIntegrityCheckPanel": "object",
        "SYNO.SDS.Backup.SimpleScheduleComponent": "object",
        "SYNO.SDS.Backup.TreeLoader": "object",
        "SYNO.SDS.Backup.TriTreeDisableCheckNodeUI": "object",
        "SYNO.SDS.Backup.TriTreeNodeUI": "object"
      },
      "webman/3rdparty/HyperBackup/explore.js": {
        "SYNO.SDS.Backup.Client.Explore.AppInstance": "object",
        "SYNO.SDS.Backup.Client.Explore.AppWindow": "object",
        "SYNO.SDS.Backup.Client.Explore.ShareDecyptDialog": "object",
        "SYNO.SDS.Backup.Client.Explore.TimeLine": "object",
        "SYNO.SDS.Backup.Client.Explore.Utils.GetErrorString": "object",
        "SYNO.SDS.Backup.Client.Explore.Utils.GetJobTrayCls": "object",
        "SYNO.SDS.Backup.Client.Explore.Utils.GetString": "object",
        "SYNO.SDS.Backup.Client.Explore.Utils.checkFn": "object",
        "SYNO.SDS.Backup.Client.Explore.Utils.checkFn_v1": "object",
        "SYNO.SDS.Backup.Client.Explore.Utils.checkThumbnailFn": "object",
        "SYNO.SDS.Backup.Client.Explore.Utils.getIconFn": "object",
        "SYNO.SDS.Backup.Client.Explore.Utils.getThumbnailFn": "object",
        "SYNO.SDS.Backup.Client.Explore.Utils.launchFn": "object",
        "SYNO.SDS.Backup.Client.Explore.VersionMenu": "object"
      },
      "webman/3rdparty/HyperBackup/fuse.js": {
        "SYNO.SDS.Backup.Client.Fuse.MountWindow": "object",
        "SYNO.SDS.Backup.Client.Fuse.Utils.GetErrorString": "object",
        "SYNO.SDS.Backup.Client.Fuse.Utils.GetFuseCls": "object",
        "SYNO.SDS.Backup.Client.Fuse.Utils.GetString": "object",
        "SYNO.SDS.Backup.Client.Fuse.Utils.bundleCheckFn": "object",
        "SYNO.SDS.Backup.Client.Fuse.Utils.bundleLaunchFn": "object",
        "SYNO.SDS.Backup.Client.Fuse.Utils.vtCheckFn": "object",
        "SYNO.SDS.Backup.Client.Fuse.Utils.vtCheckThumbnailFn": "object",
        "SYNO.SDS.Backup.Client.Fuse.Utils.vtGetIconFn": "object",
        "SYNO.SDS.Backup.Client.Fuse.Utils.vtGetThumbnailFn": "object",
        "SYNO.SDS.Backup.Client.Fuse.Utils.vtLaunchFn": "object"
      },
      "webman/3rdparty/HyperBackup/hyperbackup-vue-lib.js": {
        "SYNO.SDS.Backup.Vue.SelectBackupDestination": "object",
        "SYNO.SDS.Backup.Vue.SelectMutliVerLunVersion": "object",
        "SYNO.SDS.Backup.Vue.SelectSingleOrMultiple": "object"
      },
      "webman/3rdparty/HyperBackup/jobtray.js": {
        "SYNO.SDS.Backup.Client.JobTray.AppInstance": "object",
        "SYNO.SDS.Backup.Client.JobTray.TrayItem": "object"
      },
      "webman/3rdparty/HyperBackup/module.js": {
        "SYNO.SDS.Backup.AlertWindow": "object",
        "SYNO.SDS.Backup.PrivateKeyDownloadWindow": "object",
        "SYNO.SDS.Backup.Rotation.Previewer": "object",
        "SYNO.SDS.Backup.SummaryStep": "object",
        "SYNO.SDS.Backup.Wizard": "object"
      },
      "webman/3rdparty/HyperBackup/util.js": {
        "SYNO.Backup.Util.ExtractPattern": "object",
        "SYNO.Backup.Util.GetMultiVerLunDisplayName": "object",
        "SYNO.Backup.Util.IsImage": "object",
        "SYNO.Backup.Util.IsSubClass": "object",
        "SYNO.Backup.Util.deepCopyObject": "object",
        "SYNO.Backup.Util.getPkgVersion": "object",
        "SYNO.Backup.Util.getSharePath": "object",
        "SYNO.Backup.Util.parseVolName": "object",
        "SYNO.Backup.Util.updateAppShareTip": "object",
        "SYNO.SDS.Backup.GetBkpResultStr": "object",
        "SYNO.SDS.Backup.GetErrorString": "object",
        "SYNO.SDS.Backup.HostCombobox": "object",
        "SYNO.SDS.Backup.String": "object",
        "SYNO.SDS.Backup.Util.getEncryption": "object",
        "SYNO.SDS.Backup.Util.lengthEllipsis": "object",
        "SYNO.SDS.Backup.Util.widthEllipsis": "object",
        "SYNO.SDS.Backup.Vtypes": "object",
        "SYNO.SDS.Backup.converLanString": "object",
        "SYNO.SDS.Backup.convertAppError": "object",
        "SYNO.SDS.Backup.convertDisabledShareType": "object",
        "SYNO.SDS.Backup.createTimeItemStore": "object",
        "SYNO.SDS.Backup.getReadOnlyOwnerString": "object",
        "SYNO.SDS.Backup.getShareListTpl": "object",
        "SYNO.SDS.Backup.getShareName": "object",
        "SYNO.SDS.Backup.getStatusIcon": "object",
        "SYNO.SDS.Backup.getTreeNodeByCaseId": "object",
        "SYNO.SDS.Backup.parseAppDependFolderInfo": "object",
        "SYNO.SDS.Backup.setAppGridDependency": "object"
      },
      "webman/3rdparty/OAuthService/OAuthService.js": {
        "SYNO.SDS.OAuthService.AddEditDialog": "object",
        "SYNO.SDS.OAuthService.CommonSettingDialog": "object",
        "SYNO.SDS.OAuthService.ConnectionInfoDialog": "object",
        "SYNO.SDS.OAuthService.Instance": "object"
      },
      "webman/3rdparty/QuickConnect/QuickConnect.js": {
        "SYNO.SDS.AdminCenter.QuickConnect.AdminTab": "object"
      },
      "webman/3rdparty/SMBService/directory-admin-list-dialog.js": {
        "SYNO.SDS.SMBService.Domain.Alert": "object",
        "SYNO.SDS.SMBService.Domain.DirectoryAdminDialog": "object",
        "SYNO.SDS.SMBService.Domain.Error2Msg": "object",
        "SYNO.SDS.SMBService.Domain.UserChooser": "object"
      },
      "webman/3rdparty/SMBService/domain-filter.js": {
        "SYNO.SDS.SMBService.Domain.Filter": "object"
      },
      "webman/3rdparty/SMBService/domain-options-dialog.js": {
        "SYNO.SDS.SMBService.Domain.OptionsDialog": "object",
        "SYNO.SDS.SMBService.Domain.OptionsForm": "object"
      },
      "webman/3rdparty/SMBService/smb-resource-monitor-perf.js": {
        "SYNO.SDS.SMBService.Performance.SMB.Charts": "object",
        "SYNO.SDS.SMBService.Performance.SMB.CmdSelector": "object",
        "SYNO.SDS.SMBService.Performance.SMB.CommandCategory": "object",
        "SYNO.SDS.SMBService.Performance.SMB.CommandConvertor": "object",
        "SYNO.SDS.SMBService.Performance.SMB.CommandList": "object",
        "SYNO.SDS.SMBService.Performance.SMB.Current": "object",
        "SYNO.SDS.SMBService.Performance.SMB.CurrentCard": "object",
        "SYNO.SDS.SMBService.Performance.SMB.Dataset": "object",
        "SYNO.SDS.SMBService.Performance.SMB.DefaultColors": "object",
        "SYNO.SDS.SMBService.Performance.SMB.History": "object",
        "SYNO.SDS.SMBService.Performance.SMB.HistoryCard": "object",
        "SYNO.SDS.SMBService.Performance.SMB.InitConst": "object",
        "SYNO.SDS.SMBService.Performance.SMB.Main": "object",
        "SYNO.SDS.SMBService.Performance.SMB.MaxDisplayCommands": "object",
        "SYNO.SDS.SMBService.Performance.SMB.PktCategory": "object",
        "SYNO.SDS.SMBService.Performance.SMB.PktType": "object"
      },
      "webman/3rdparty/SMBService/smb-tab.js": {
        "SYNO.SDS.SMBService.AppPrivilege.Instance": "object",
        "SYNO.SDS.SMBService.Instance": "object",
        "SYNO.SDS.SMBService.PkgVer": "object",
        "SYNO.SDS.SMBService.SMB.AdvancedSettingsConfirmDialog": "object",
        "SYNO.SDS.SMBService.SMB.AdvancedSettingsDialog": "object",
        "SYNO.SDS.SMBService.SMB.AdvancedSettingsTabPanel": "object",
        "SYNO.SDS.SMBService.SMB.GeneralTab": "object",
        "SYNO.SDS.SMBService.SMB.MacTab": "object",
        "SYNO.SDS.SMBService.SMB.MsdfsRuleAddEditDialog": "object",
        "SYNO.SDS.SMBService.SMB.MsdfsRulesData": "object",
        "SYNO.SDS.SMBService.SMB.MsdfsRulesDialog": "object",
        "SYNO.SDS.SMBService.SMB.MsdfsRulesGrid": "object",
        "SYNO.SDS.SMBService.SMB.MsdfsRulesGridPageLessToolBar": "object",
        "SYNO.SDS.SMBService.SMB.MsdfsTestAccountDialog": "object",
        "SYNO.SDS.SMBService.SMB.OthersTab": "object",
        "SYNO.SDS.SMBService.SMB.SMBProtocolComboBox": "object",
        "SYNO.SDS.SMBService.SMB.SmbLogSettingDialog": "object",
        "SYNO.SDS.SMBService.SMB.WinTab": "object",
        "SYNO.SDS.SMBService.SMB.WinTab.Utils": "object",
        "SYNO.SDS.SMBService.SupportConfig": "object",
        "SYNO.SDS.SMBService.Utils": "object"
      },
      "webman/3rdparty/SMBService/smb.bundle.js": {
        "SYNO.SDS.SMBService.Vue.SMB.KerberosSettingsDialog": "object"
      },
      "webman/3rdparty/ScsiTarget/iscsi.js": {
        "SYNO.SDS.SAN.CardsMainPanel": "object",
        "SYNO.SDS.SAN.EmptyMainPanel": "object",
        "SYNO.SDS.SAN.Fibre.ConnectionStatus": "object",
        "SYNO.SDS.SAN.Fibre.EmptyMain": "object",
        "SYNO.SDS.SAN.Fibre.Main": "object",
        "SYNO.SDS.SAN.Fibre.NormalMain": "object",
        "SYNO.SDS.SAN.Host.EmptyMain": "object",
        "SYNO.SDS.SAN.LUN.EmptyMain": "object",
        "SYNO.SDS.SAN.LUN.Selecting.GridPanel": "object",
        "SYNO.SDS.SAN.Snapshot.EmptyMain": "object",
        "SYNO.SDS.SAN.Target.EmptyMain": "object",
        "SYNO.SDS.iSCSI.ADVREPLICA_ENC_SHARE": "object",
        "SYNO.SDS.iSCSI.ADVREPLICA_HOMES": "object",
        "SYNO.SDS.iSCSI.AdvancedSearchField": "object",
        "SYNO.SDS.iSCSI.Application": "object",
        "SYNO.SDS.iSCSI.Comp.TextItem": "object",
        "SYNO.SDS.iSCSI.DATASITE_MAX": "object",
        "SYNO.SDS.iSCSI.DEFAULT_MAX_REPLICA": "object",
        "SYNO.SDS.iSCSI.DSM_HTTPS_PORT": "object",
        "SYNO.SDS.iSCSI.DSM_HTTP_PORT": "object",
        "SYNO.SDS.iSCSI.DataView": "object",
        "SYNO.SDS.iSCSI.FCTARGET.DefaultWWPN": "object",
        "SYNO.SDS.iSCSI.FCTARGET.MAX_MAPPING_LUNS": "object",
        "SYNO.SDS.iSCSI.GetDRErrMsg": "object",
        "SYNO.SDS.iSCSI.HOST_PERMISSSION_HELP_WEB_LINK": "object",
        "SYNO.SDS.iSCSI.Host.Create": "object",
        "SYNO.SDS.iSCSI.Host.Detail": "object",
        "SYNO.SDS.iSCSI.Host.Edit": "object",
        "SYNO.SDS.iSCSI.Host.Initiator": "object",
        "SYNO.SDS.iSCSI.Host.InitiatorDisplay": "object",
        "SYNO.SDS.iSCSI.Host.InitiatorEditWindow": "object",
        "SYNO.SDS.iSCSI.Host.Main": "object",
        "SYNO.SDS.iSCSI.Host.NormalMain": "object",
        "SYNO.SDS.iSCSI.Host.Overview": "object",
        "SYNO.SDS.iSCSI.Host.Privilege": "object",
        "SYNO.SDS.iSCSI.Host.PrivilegeDisplay": "object",
        "SYNO.SDS.iSCSI.Host.Property": "object",
        "SYNO.SDS.iSCSI.Host.Wizard.PrivilegeStep": "object",
        "SYNO.SDS.iSCSI.Host.Wizard.PropertyStep": "object",
        "SYNO.SDS.iSCSI.Host.Wizard.SummaryStep": "object",
        "SYNO.SDS.iSCSI.LUN.AdvSettings": "object",
        "SYNO.SDS.iSCSI.LUN.Clone": "object",
        "SYNO.SDS.iSCSI.LUN.Delete": "object",
        "SYNO.SDS.iSCSI.LUN.DisplayField": "object",
        "SYNO.SDS.iSCSI.LUN.Edit": "object",
        "SYNO.SDS.iSCSI.LUN.EditPrivilegeTab": "object",
        "SYNO.SDS.iSCSI.LUN.FeasibilityCheck": "object",
        "SYNO.SDS.iSCSI.LUN.GeneralFeasChkFailCallback": "object",
        "SYNO.SDS.iSCSI.LUN.Main": "object",
        "SYNO.SDS.iSCSI.LUN.Mapping": "object",
        "SYNO.SDS.iSCSI.LUN.NormalMain": "object",
        "SYNO.SDS.iSCSI.LUN.Privilege": "object",
        "SYNO.SDS.iSCSI.LUN.Property": "object",
        "SYNO.SDS.iSCSI.LUN.Status": "object",
        "SYNO.SDS.iSCSI.LUN.Wizard.ConvertReadmeStep": "object",
        "SYNO.SDS.iSCSI.LUN.Wizard.ConvertSummaryStep": "object",
        "SYNO.SDS.iSCSI.LUN.Wizard.CreateHost": "object",
        "SYNO.SDS.iSCSI.LUN.Wizard.CreateSummaryStep": "object",
        "SYNO.SDS.iSCSI.LUN.Wizard.HostMappingStep": "object",
        "SYNO.SDS.iSCSI.LUN.Wizard.LunTypeBox": "object",
        "\u2026": "+194 more keys"
      },
      "webman/3rdparty/SecureSignIn/SecureSignIn.js": {
        "SYNO.SDS.SecureSignIn.AdvanceSigninMethod": "object",
        "SYNO.SDS.SecureSignIn.Instance": "object",
        "SYNO.SDS.SecureSignIn.Passwordless.Settings": "object",
        "SYNO.SDS.SecureSignIn.Register.InheritDialog": "object",
        "SYNO.SDS.SecureSignIn.Register.PasswordlessWizard": "object",
        "SYNO.SDS.SecureSignIn.Register.TwoFactorWizard": "object",
        "SYNO.SDS.SecureSignIn.TwoFactor.Settings": "object",
        "SYNO.SDS.SecureSignIn.Utils.Note": "object"
      },
      "webman/3rdparty/Spreadsheet/dist/ui.basic_app.js": {
        "SYNO.SDS.Office.AppInstance": "object",
        "SYNO.SDS.Office.BasicApp": "object",
        "SYNO.SDS.Office.BasicInstance": "object"
      },
      "webman/3rdparty/Spreadsheet/dist/ui.doc.js": {
        "SYNO.SDS.Office.Doc.Application": "object",
        "SYNO.SDS.Office.Doc.MainWindow": "object"
      },
      "webman/3rdparty/Spreadsheet/dist/ui.drive.js": {
        "SYNO.SDS.Office.Drive": "object"
      },
      "webman/3rdparty/Spreadsheet/dist/ui.drive_admin_console.js": {
        "SYNO.SDS.Office.AdminSetting": "object"
      },
      "webman/3rdparty/Spreadsheet/dist/ui.fb_ext.js": {
        "SYNO.SDS.Office.FBExt.checkImport": "object",
        "SYNO.SDS.Office.FBExt.checkOffice": "object",
        "SYNO.SDS.Office.FBExt.launchImport": "object",
        "SYNO.SDS.Office.FBExt.launchOffice": "object"
      },
      "webman/3rdparty/Spreadsheet/dist/ui.finder_plugin.js": {
        "SYNO.SDS.Office.Finder.Action.Open": "object",
        "SYNO.SDS.Office.Finder.Action.View": "object"
      },
      "webman/3rdparty/Spreadsheet/dist/ui.legacy_app.js": {
        "SYNO.SDS.SheetStation.Sheet.Application": "object"
      },
      "\u2026": "+154 more keys"
    },
    "ServiceStatus": {},
    "Session": {
      "AdvControlPanel": "boolean",
      "authType": "string",
      "boot_done": "boolean",
      "brm_enable": "string",
      "builddate": "string",
      "buildphase": "string",
      "date_format": "string",
      "domainUser": "string",
      "dsm_timeout": "integer",
      "fullversion": "string",
      "gpo_enable_java": "string",
      "ha_active_hostname": "string",
      "ha_active_model": "string",
      "ha_allow_bond_manage": "boolean",
      "ha_handle_set_ovs": "boolean",
      "ha_heartbeat_ip_list": "array<string>",
      "ha_hide_hw_setting": "boolean",
      "ha_hide_ntb": "boolean",
      "ha_hide_ntp_setting": "boolean",
      "ha_host0": "string",
      "ha_host1": "string",
      "ha_hw_spectre_meltdown": "boolean",
      "ha_not_support_bridge": "boolean",
      "ha_not_support_ipv6": "boolean",
      "ha_not_support_pppoe": "boolean",
      "ha_not_support_usb_modem": "boolean",
      "ha_passive_hostname": "string",
      "ha_passive_model": "string",
      "ha_running": "boolean",
      "ha_safemode": "boolean",
      "ha_snmp_show_hostname": "boolean",
      "ha_support_controller_notify": "boolean",
      "ha_support_node_notify": "boolean",
      "ha_support_pw_btn": "boolean",
      "ha_support_volume_encryption": "boolean",
      "ha_support_worm": "boolean",
      "has_ha_if": "boolean",
      "hostname": "string",
      "ip_country": "string",
      "isLogined": "boolean",
      "isMobile": "boolean",
      "is_admin": "boolean",
      "is_dual_chain": "boolean",
      "is_ha_empty_passive": "boolean",
      "is_ha_upgrading": "boolean",
      "is_hybrid_ha": "boolean",
      "is_secure": "boolean",
      "is_system_recovering": "boolean",
      "is_system_recovering_type": "string",
      "is_upgrading": "boolean",
      "join_dsm_cms": "boolean",
      "juniormodedata_exist": "boolean",
      "lang": "string",
      "majorversion": "string",
      "manage_eth_in_ha_pkg": "boolean",
      "manage_hostname_in_ha_pkg": "boolean",
      "manage_pw_btn_in_ha_pkg": "boolean",
      "minorversion": "string",
      "productversion": "string",
      "promote_ew": "boolean",
      "\u2026": "+11 more keys"
    },
    "Strings": {
      "SYNO.ActiveBackup.AppInstance": {
        "app": "object",
        "common": "object",
        "package": "object"
      },
      "SYNO.ActiveBackup.FileStation.Utils.checkActionFn": {
        "filestation": "object"
      },
      "SYNO.Application.Service.Instance": {},
      "SYNO.Finder.Application": {
        "app": "object",
        "audio_player": "object",
        "common": "object"
      },
      "SYNO.Finder.MainWindow": {},
      "SYNO.Finder.Spotlight.Application": {},
      "SYNO.Finder.Spotlight.MainWindow": {},
      "SYNO.Finder.TaskCard.FileIndex": {},
      "SYNO.Foto.AppInstance": {
        "app": "object",
        "warning": "object"
      },
      "SYNO.Foto.Sharing.AppInstance": {
        "app": "object"
      },
      "SYNO.SDS.AI.Strings": {},
      "SYNO.SDS.ActiveBackupGSuite.Instance": {
        "app": "object"
      },
      "SYNO.SDS.ActiveBackupGSuite.Portal.Instance": {
        "app": "object"
      },
      "SYNO.SDS.ActiveBackupGSuite.Portal.MainWindow": {},
      "SYNO.SDS.ActiveBackupGSuite.View.MainWindow": {},
      "SYNO.SDS.ActiveBackupPortal.Application": {},
      "SYNO.SDS.ActiveInsight.FileActivity.TruncateDatabase.BackgroundTask": {},
      "SYNO.SDS.ActiveInsight.Instance": {
        "app": "object"
      },
      "SYNO.SDS.AdminCenter.QuickConnect.AdminTab": {
        "relayservice": "object"
      },
      "SYNO.SDS.App.AI.Instance": {
        "api_integration": "object",
        "app": "object"
      },
      "SYNO.SDS.App.FileStation3.Instance": {
        "common": "object",
        "filetable": "object",
        "mainmenu": "object",
        "sharing": "object",
        "tree": "object",
        "upload": "object",
        "warning": "object"
      },
      "SYNO.SDS.App.SharingUpload.Application": {
        "tree": "object"
      },
      "SYNO.SDS.Backup.Application": {
        "app": "object",
        "fuse": "object",
        "mainmenu": "object"
      },
      "SYNO.SDS.Backup.Client.Explore.AppInstance": {
        "backup": "object"
      },
      "SYNO.SDS.Backup.Client.Fuse.Utils.bundleLaunchFn": {},
      "SYNO.SDS.Backup.Client.JobTray.AppInstance": {},
      "SYNO.SDS.Backup.ScheduleBackupWidget": {},
      "SYNO.SDS.C2FS.App.PinDownloadBackgroundTask": {},
      "SYNO.SDS.C2FS.Application": {
        "app": "object",
        "attribute": "object",
        "common": "object",
        "error": "object",
        "file_station": "object",
        "warn": "object"
      },
      "SYNO.SDS.C2FS.Share.Transform.BackgroundTask": {},
      "SYNO.SDS.CSTN.Explore.Instance": {
        "func": "object"
      },
      "SYNO.SDS.CSTN.Instance": {
        "app": "object"
      },
      "SYNO.SDS.CSTN.Tray.DesktopIndex.Instance": {},
      "SYNO.SDS.ContainerManager.Application": {
        "project": "object"
      },
      "SYNO.SDS.Drive.Application": {
        "drive": "object",
        "warning": "object"
      },
      "SYNO.SDS.Drive.Extension.Instance": {
        "app": "object",
        "btn": "object",
        "func": "object"
      },
      "SYNO.SDS.LogCenter.BuiltIn": {
        "helptoc": "object",
        "mainmenu": "object"
      },
      "SYNO.SDS.LogCenter.MainWindow": {},
      "SYNO.SDS.OAuthService.Instance": {
        "app": "object"
      },
      "SYNO.SDS.Office.AdminSetting": {},
      "SYNO.SDS.Office.AppInstance": {
        "app": "object",
        "error": "object",
        "feasibility": "object",
        "warning": "object"
      },
      "SYNO.SDS.RecycleBin.Cleaner.FBExt": {
        "recycle_bin": "object"
      },
      "SYNO.SDS.RecycleBin.Restore.FBExt": {
        "recycle_bin": "object"
      },
      "SYNO.SDS.SMBService.Instance": {
        "error": "object",
        "network": "object"
      },
      "SYNO.SDS.SecureSignIn.Instance": {
        "authenticator": "object",
        "error": "object",
        "fido": "object"
      },
      "SYNO.SDS.SecurityScan.Instance": {
        "helptoc": "object"
      },
      "SYNO.SDS.SecurityScan.MainWindow": {},
      "SYNO.SDS.SynologyDriveShareSync.Instance": {
        "app": "object",
        "warning": "object"
      },
      "SYNO.SDS.SynologyDriveShareSync.TrayApp": {
        "app": "object"
      },
      "SYNO.SDS.SynologyDriveShareSync.View.Tray.Viewport": {},
      "SYNO.SDS.SynologyDriveShareSync.View.Viewport": {},
      "SYNO.SDS.VideoPlayer2.Application": {
        "video_player": "object"
      },
      "SYNO.SDS.iSCSI.Application": {
        "common": "object",
        "feasibilitycheck": "object",
        "poweroff": "object",
        "san_fibre": "object"
      },
      "SYNO.SDS.iSCSI.MainWindow": {}
    },
    "UserSettings": {
      "BackgroundTask": {},
      "Desktop": {
        "ShortcutItems": "array",
        "new_app_list": "array<empty>",
        "valid_appview_order": "array"
      },
      "SYNO.SDS.App.DiskMessageApp.Instance": {
        "restoreSizePos": "object"
      },
      "SYNO.SDS.App.FileStation3.Instance": {
        "activeViewItemId": "string",
        "restoreSizePos": "object",
        "treePanelWidth": "integer"
      },
      "SYNO.SDS.App.PersonalSettings.Instance": {
        "search_count": "integer"
      },
      "SYNO.SDS.App.PromotionApp": {
        "ew_promoted": "boolean",
        "last_promote_patch": "object",
        "not_done_ew": "boolean",
        "not_done_ss": "boolean",
        "not_done_udc": "boolean",
        "show_quick_tour_tray": "boolean"
      },
      "SYNO.SDS.Backup.Application": {
        "restoreSizePos": "object"
      },
      "SYNO.SDS.DSMNotify.CheckMailIsEnabledTray.Instance": {
        "show_notification_tray": "boolean"
      },
      "SYNO.SDS.StorageManager.Instance": {
        "disk_grid_hidden": "array",
        "restoreSizePos": "object"
      },
      "SYNO.SDS.SynologyApplicationService": {
        "app_order": "array<empty>"
      },
      "SYNO.SDS._Widget.Instance": {
        "restoreParams": "object"
      }
    }
  }
}
```

## SYNO.Core.Desktop.Timeout

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Desktop.Timeout`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "timeout": "integer"
  }
}
```

## SYNO.Core.DisableAdmin

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.DisableAdmin`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "notify_disable_admin": "boolean"
  }
}
```

## SYNO.Core.EW.Info

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.EW.Info`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "have_applied_eunit": "boolean",
    "info": {
      "advertisement": "boolean",
      "drma_region": "string",
      "expired_at": "string",
      "promotion_expired_at": "null",
      "sn": "string",
      "status": "string"
    },
    "mail": "string",
    "show_welcome_page": "boolean"
  }
}
```

## SYNO.Core.EventScheduler

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.EventScheduler`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

Confirmed present: DSM returned error 117 rather than 103, so the method exists. What it additionally requires was not determined.
The exact signature was not determined; it is listed here so it is known to exist.

**Response:**

```json
{
  "success": false,
  "error": {
    "code": 117
  }
}
```

#### Method: `list`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.EventScheduler`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": "array<empty>"
}
```

## SYNO.Core.File.Thumbnail

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

## SYNO.Core.FileHandle

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.FileHandle`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "OpenedFiles": "array<empty>",
    "total": "integer"
  }
}
```

## SYNO.Core.Findhost

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `list`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Findhost`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": "array<empty>"
}
```

## SYNO.Core.Group.ExtraAdmin

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Group.ExtraAdmin`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

Confirmed present: DSM returned error 3201 rather than 103, so the method exists. What it additionally requires was not determined.
The exact signature was not determined; it is listed here so it is known to exist.

**Response:**

```json
{
  "success": false,
  "error": {
    "code": 3201
  }
}
```

## SYNO.Core.Group.ValidLocalAdmin

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `list`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Group.ValidLocalAdmin`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "users": [
      {
        "name": "string"
      }
    ]
  }
}
```

## SYNO.Core.GroupSettings

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.GroupSettings`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

Confirmed present: DSM returned error 117 rather than 103, so the method exists. What it additionally requires was not determined.
The exact signature was not determined; it is listed here so it is known to exist.

**Response:**

```json
{
  "success": false,
  "error": {
    "code": 117
  }
}
```

## SYNO.Core.OAuth.Scope

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.OAuth.Scope`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "scope": "array<empty>"
  }
}
```

## SYNO.Core.OAuth.Server

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.OAuth.Server`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": [
    {
      "enabled": "boolean",
      "endpoint": "string",
      "expect": {
        "data": "object"
      },
      "header": "string",
      "id": "string",
      "params": "string"
    }
  ]
}
```

## SYNO.Core.OTP.Admin

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.OTP.Admin`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

Confirmed present: DSM returned error 4203 rather than 103, so the method exists. What it additionally requires was not determined.
The exact signature was not determined; it is listed here so it is known to exist.

**Response:**

```json
{
  "success": false,
  "error": {
    "code": 4203
  }
}
```

## SYNO.Core.OTP.EnforcePolicy

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.OTP.EnforcePolicy`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "otp_enforce_option": "string"
  }
}
```

#### Method: `list`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.OTP.EnforcePolicy`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID from `SYNO.API.Auth`

Confirmed present: DSM returned error 4203 rather than 103, so the method exists. What it additionally requires was not determined.
The exact signature was not determined; it is listed here so it is known to exist.

**Response:**

```json
{
  "success": false,
  "error": {
    "code": 4203
  }
}
```

## SYNO.Core.PhotoViewer

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `info`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.PhotoViewer`
- `version` (required): `1`
- `method` (required): `info`
- `_sid` (required): Session ID from `SYNO.API.Auth`

Confirmed present, but not callable with the four parameters above — it requires additional parameters — DSM names the missing one in `error.errors`.
The exact signature was not determined; it is listed here so it is known to exist.

**Response:**

```json
{
  "success": false,
  "error": {
    "code": 120
  }
}
```

#### Method: `list`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.PhotoViewer`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID from `SYNO.API.Auth`

Confirmed present, but not callable with the four parameters above — it requires additional parameters — DSM names the missing one in `error.errors`.
The exact signature was not determined; it is listed here so it is known to exist.

**Response:**

```json
{
  "success": false,
  "error": {
    "code": 120
  }
}
```

## SYNO.Core.Quota

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Quota`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

Confirmed present: DSM returned error 5403 rather than 103, so the method exists. What it additionally requires was not determined.
The exact signature was not determined; it is listed here so it is known to exist.

**Response:**

```json
{
  "success": false,
  "error": {
    "code": 5403
  }
}
```

## SYNO.Core.RecycleBin

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.RecycleBin`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "is_cleaning": "boolean"
  }
}
```

## SYNO.Core.RecycleBin.User

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.RecycleBin.User`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "is_cleaning": "boolean"
  }
}
```

## SYNO.Core.SNMP

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.SNMP`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "contact": "string",
    "enable_snmp": "boolean",
    "enable_snmp_v1v2": "boolean",
    "enable_snmp_v3": "boolean",
    "location": "string",
    "name": "string",
    "node0_name": "string",
    "node1_name": "string",
    "rocommunity": "string",
    "rouser": "string"
  }
}
```

## SYNO.Core.Service

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1–3

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Service`
- `version` (required): `3`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "service": [
      {
        "display_name_section_key": "string",
        "enable_status": "string",
        "service_id": "string"
      }
    ]
  }
}
```

## SYNO.Core.Service.Conf

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Service.Conf`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "service_fw_target_interface": "string"
  }
}
```

## SYNO.Core.Synohdpack

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

## SYNO.Core.TFTP

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.TFTP`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "enable": "boolean",
    "enable_log": "boolean",
    "endip": "string",
    "permission": "string",
    "root_path": "string",
    "startip": "string",
    "timeout": "integer"
  }
}
```

## SYNO.Core.TrustDevice

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.TrustDevice`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

Confirmed present, but not callable with the four parameters above — it requires additional parameters.
The exact signature was not determined; it is listed here so it is known to exist.

**Response:**

```json
{
  "success": false,
  "error": {
    "code": 114
  }
}
```

## SYNO.Core.User.Group

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.User.Group`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

Confirmed present: DSM returned error 3103 rather than 103, so the method exists. What it additionally requires was not determined.
The exact signature was not determined; it is listed here so it is known to exist.

**Response:**

```json
{
  "success": false,
  "error": {
    "code": 3103
  }
}
```

## SYNO.Core.User.UsernamePolicy

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `list`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.User.UsernamePolicy`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": "array<string>"
}
```

## SYNO.Core.UserSettings

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.UserSettings`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "BackgroundTask": {},
    "Desktop": {
      "ShortcutItems": "array<object>",
      "new_app_list": "array<empty>",
      "valid_appview_order": "array<string>"
    },
    "SYNO.SDS.App.DiskMessageApp.Instance": {
      "restoreSizePos": {
        "fromRestore": "boolean",
        "x": "integer",
        "y": "integer"
      }
    },
    "SYNO.SDS.App.FileStation3.Instance": {
      "activeViewItemId": "string",
      "restoreSizePos": {
        "fromRestore": "boolean",
        "height": "integer",
        "pageX": "integer",
        "pageY": "integer",
        "width": "integer"
      },
      "treePanelWidth": "integer"
    },
    "SYNO.SDS.App.PersonalSettings.Instance": {
      "search_count": "integer"
    },
    "SYNO.SDS.App.PromotionApp": {
      "ew_promoted": "boolean",
      "last_promote_patch": {
        "buildnumber": "string",
        "major": "string",
        "micro": "string",
        "minor": "string",
        "nano": "string"
      },
      "not_done_ew": "boolean",
      "not_done_ss": "boolean",
      "not_done_udc": "boolean",
      "show_quick_tour_tray": "boolean"
    },
    "SYNO.SDS.Backup.Application": {
      "restoreSizePos": {
        "fromRestore": "boolean",
        "height": "integer",
        "pageX": "integer",
        "pageY": "integer",
        "width": "integer"
      }
    },
    "SYNO.SDS.DSMNotify.CheckMailIsEnabledTray.Instance": {
      "show_notification_tray": "boolean"
    },
    "SYNO.SDS.StorageManager.Instance": {
      "disk_grid_hidden": "array<string>",
      "restoreSizePos": {
        "fromRestore": "boolean",
        "height": "integer",
        "maximized": "boolean",
        "width": "integer",
        "x": "integer",
        "y": "integer"
      }
    },
    "SYNO.SDS.SynologyApplicationService": {
      "app_order": "array<empty>"
    },
    "SYNO.SDS._Widget.Instance": {
      "restoreParams": {
        "windowState": "object"
      }
    }
  }
}
```

## SYNO.Core.Virtualization.Host.Capability

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Virtualization.Host.Capability`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "capable": "boolean"
  }
}
```

## SYNO.Core.VolEncKeepKey

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.VolEncKeepKey`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "notify_vol_enc_keep_key": "boolean"
  }
}
```
