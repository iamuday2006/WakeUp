[Setup]
AppId={{73E5B0A8-2C4E-4F2B-9A8E-3C6D5B1E2F40}}
AppName=WakeUp
AppVersion=1.0.0
AppPublisher=iamuday2006
DefaultDirName={localappdata}\WakeUp
DisableProgramGroupPage=yes
OutputDir=installer
OutputBaseFilename=WakeUpSetup
Compression=lzma2
SolidCompression=yes
WizardStyle=modern
PrivilegesRequired=lowest
ArchitecturesAllowed=x64compatible
ArchitecturesInstallIn64BitMode=x64compatible
UninstallDisplayIcon={app}\WakeUp.exe
UninstallDisplayName=WakeUp

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "Create a &desktop shortcut"; GroupDescription: "Additional icons:"; Flags: unchecked

[Files]
Source: "dist\WakeUp.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "assets\256x256.png"; DestDir: "{app}\assets"; Flags: ignoreversion
Source: "assets\256x256.ico"; DestDir: "{app}\assets"; Flags: ignoreversion

[Registry]
Root: HKCU; Subkey: "Software\Microsoft\Windows\CurrentVersion\Run"; ValueType: string; ValueName: "WakeUp"; ValueData: """{app}\WakeUp.exe"""; Flags: uninsdeletevalue

[Icons]
Name: "{group}\WakeUp"; Filename: "{app}\WakeUp.exe"
Name: "{autodesktop}\WakeUp"; Filename: "{app}\WakeUp.exe"; Tasks: desktopicon

[InstallDelete]
Type: files; Name: "{userstartup}\WakeUp.lnk"
Type: files; Name: "{app}\*"

[UninstallDelete]
Type: files; Name: "{userstartup}\WakeUp.lnk"
Type: filesandordirs; Name: "{app}\assets"
Type: dirifempty; Name: "{app}"
