# Core · Sharing APIs (probed)

**Category:** System Management

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

## SYNO.Core.Sharing

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Sharing`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

Confirmed present: DSM returned error 1005 rather than 103, so the method exists. What it additionally requires was not determined.
The exact signature was not determined; it is listed here so it is known to exist.

**Response:**

```json
{
  "success": false,
  "error": {
    "code": 1005
  }
}
```

#### Method: `list`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Sharing`
- `version` (required): `1`
- `method` (required): `list`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "limit": "integer",
    "offset": "integer",
    "sharings": "array<empty>",
    "total": "integer"
  }
}
```

## SYNO.Core.Sharing.Initdata

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1

#### Method: `get`

**HTTP Method:** POST

**Parameters:**
- `api` (required): `SYNO.Core.Sharing.Initdata`
- `version` (required): `1`
- `method` (required): `get`
- `_sid` (required): Session ID from `SYNO.API.Auth`

**Response:**

```json
{
  "success": true,
  "data": {
    "ActionPrivilege": "array<empty>",
    "AppPrivilege": {},
    "CSSFiles": "array<string>",
    "GroupSettings": {},
    "JSConfig": {
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
      "webman/3rdparty/SynologyPhotos/fileStationExtension.min.js": {
        "SYNO.Foto.FileStationExtension.getIconFn": "object"
      },
      "webman/3rdparty/SynologyPhotos/pkg_index.min.js": {
        "SYNO.Foto.AppInstance": "object",
        "SYNO.Foto.Sharing.AppInstance": "object"
      },
      "webman/3rdparty/SynologyPhotos/react_bundle.js": {
        "FotoReactLibrary": "object"
      },
      "webman/3rdparty/SynologyPhotos/three.min.js": {
        "Three": "object"
      },
      "webman/3rdparty/SynologyPhotos/videojs/video.min.js": {
        "VideoJSLibrary": "object"
      },
      "webman/3rdparty/SynologyPhotos/videojs/videojs-qualityselector.min.js": {
        "VideoJSPlugin-QualitySelector": "object"
      },
      "webman/3rdparty/SynologyPhotos/videojs/videojs-vr.min.js": {
        "VideoJSPlugin-Vr": "object"
      },
      "webman/3rdparty/UniversalViewer/uv.application.js": {
        "SYNO.SDS.UniversalViewer.Application": "object",
        "SYNO.SDS.UniversalViewer.Window": "object"
      },
      "webman/3rdparty/UniversalViewer/uv.dsmloader.js": {
        "SYNO.SDS.UniversalViewer": "object"
      },
      "webman/modules/Chooser/Chooser.js": {
        "SYNO.SDS.ShareChooser": "object",
        "SYNO.SDS.UserChooser": "object"
      },
      "webman/modules/DSMNotify/CheckAFPIsEnabledTray.js": {
        "SYNO.SDS.DSMNotify.CheckAFPIsEnabledTray.Instance": "object",
        "SYNO.SDS.DSMNotify.CheckAFPIsEnabledTray.notified": "object"
      },
      "webman/modules/DSMNotify/CheckMailIsEnabledTray.js": {
        "SYNO.SDS.DSMNotify.CheckMailIsEnabledTray.Instance": "object",
        "SYNO.SDS.DSMNotify.CheckMailIsEnabledTray.notified": "object"
      },
      "webman/modules/DSMNotify/DSMNotify.js": {
        "SYNO.SDS.DSMNotify.Application": "object",
        "SYNO.SDS.DSMNotify.Panel": "object",
        "SYNO.SDS.DSMNotify.Tray": "object",
        "SYNO.SDS.DSMNotify.Utils": "object"
      },
      "webman/modules/DSMNotify/DSMNotifyVueBundle.js": {
        "SYNO.SDS.DSMNotify.Detail.Instance": "object",
        "SYNO.SDS.DSMNotify.Setting.Application": "object",
        "SYNO.SDS.DSMNotify.ShowAll.Instance": "object"
      },
      "webman/modules/FileChooser/FileChooser.js": {
        "SYNO.SDS.Utils.FileChooser": "object",
        "SYNO.SDS.Utils.FileChooser.Chooser": "object",
        "SYNO.SDS.Utils.FileChooser.CrtFdrDialog": "object",
        "SYNO.SDS.Utils.FileChooser.Utils": "object"
      },
      "webman/modules/PollingTask/PollingTask.js": {
        "SYNO.SDS.PollingTask.Application": "object",
        "SYNO.SDS.PollingTask.Tray": "object"
      },
      "webman/modules/SharingManager/SharingManager.js": {
        "SYNO.SDS.Utils.SharingManager.CreateSharingDialog": "object",
        "SYNO.SDS.Utils.SharingManager.EditSharingDialog": "object",
        "SYNO.SDS.Utils.SharingManager.Manager": "object",
        "SYNO.SDS.Utils.SharingManager.ShareWithMePanel": "object",
        "SYNO.SDS.Utils.SharingManager.SharingDateDialog": "object",
        "SYNO.SDS.Utils.SharingManager.SharingEntryDialog": "object",
        "SYNO.SDS.Utils.SharingManager.SharingPanel": "object"
      },
      "webman/modules/TinyMCE/TinyMCE.js": {
        "SYNO.ux.TinyMCE": "object"
      },
      "webman/modules/TinyMCE/TinyMCEVue.js": {
        "SYNO.Vue.TinyMCE": "object"
      },
      "webman/modules/TinyMCE/tinymce.min.js": {
        "SYNO.ux.tinyMCE.Core": "object"
      },
      "webman/modules/Utils/AccountPasswordDialog.js": {
        "SYNO.SDS.Utils.AccountPasswordDialog": "object"
      },
      "webman/modules/Utils/PasswordConfirmDialog.js": {
        "SYNO.SDS.Utils.PasswordConfirmDialog": "object"
      },
      "webman/modules/Utils/PercentageBar.js": {
        "SYNO.SDS.Utils.PercentageBar": "object"
      },
      "webman/modules/Utils/QRCodeDialog.js": {
        "SYNO.SDS.Utils.QRCodeDialog": "object"
      },
      "webman/modules/Utils/S2S.js": {
        "SYNO.SDS.Utils.S2S": "object"
      },
      "webman/modules/Utils/TimeLine.js": {
        "SYNO.SDS.Utils.IScroll": "object",
        "SYNO.SDS.Utils.TimeLine": "object"
      },
      "webman/modules/Utils/TreeGrid.js": {
        "Ext.tree.BooleanColumn": "object",
        "Ext.tree.Column": "object",
        "Ext.tree.ColumnResizer": "object",
        "Ext.tree.DateColumn": "object",
        "Ext.tree.NumberColumn": "object",
        "Ext.ux.tree.FleXcrollTreeGrid": "object",
        "Ext.ux.tree.TreeGrid": "object",
        "Ext.ux.tree.TreeGridLoader": "object",
        "Ext.ux.tree.TreeGridNodeUI": "object",
        "Ext.ux.tree.TreeGridRootNodeUI": "object",
        "Ext.ux.tree.TreeGridSorter": "object"
      },
      "webman/modules/Utils/circleGradient.js": {
        "SYNO.SDS.Utils.canvas.circlegradient": "object"
      },
      "webman/modules/Utils/deprecated.js": {
        "SYNO.SDS.Utils.Flash": "object",
        "SYNO.SDS.Utils.Flash.FlashBlockDetect": "object"
      },
      "webman/modules/Utils/external_device_util.js": {
        "SYNO.SDS.Utils.ExternalDevices": "object"
      },
      "webman/modules/Utils/image_load.js": {
        "SYNO.SDS.Utils.ImageLoad": "object"
      },
      "webman/modules/Utils/image_selector.js": {
        "SYNO.SDS.Utils.ImageSelector": "object"
      },
      "webman/modules/Utils/lazyDataView.js": {
        "SYNO.SDS.Utils.DataView.LazyDataView": "object"
      },
      "webman/modules/Widgets/Main.js": {
        "SYNO.SDS._Widget.GridPanel": "object",
        "SYNO.SDS._Widget.MiniWidget": "object",
        "SYNO.SDS._Widget.Utils": "object"
      },
      "webman/modules/Widgets/MainVue.js": {
        "SYNO.SDS._Widget.Instance": "object"
      }
    },
    "Private": {},
    "ServiceStatus": {},
    "Session": {
      "boot_done": "boolean",
      "hostname": "string",
      "isLogined": "boolean",
      "isMobile": "boolean",
      "isPublic": "boolean",
      "is_admin": "boolean",
      "is_secure": "boolean",
      "lang": "string",
      "show_autoupdatetype_notify": "string",
      "sys_lang": "string",
      "theme_cls": "string"
    },
    "Sharing": {
      "app": "null",
      "auto_gc": "boolean",
      "enable_match_ip": "boolean",
      "enabled": "boolean",
      "expire_at": "string",
      "expire_times": "integer",
      "hash": "string",
      "owner_user": "string",
      "project_name": "string",
      "protect_groups": "array<empty>",
      "protect_title": "string",
      "protect_type": "string",
      "protect_users": "array<empty>",
      "redirect_type": "string",
      "redirect_uri": "string",
      "start_at": "string",
      "use_count": "integer"
    },
    "Strings": {
      "SYNO.ActiveBackup.AppInstance": {
        "app": "object",
        "common": "object",
        "package": "object"
      },
      "SYNO.Foto.AppInstance": {
        "app": "object",
        "warning": "object"
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
      }
    },
    "UserSettings": {}
  }
}
```

## SYNO.Core.Sharing.Session

**Endpoint:** `/webapi/entry.cgi` · **Versions:** 1
