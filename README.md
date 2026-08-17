# WakeUp

A Windows desktop reminder that shows a health tip notification every 30 minutes.

## Features

- Shows a random health/ergonomics reminder every 30 minutes
- Windows toast notification with custom icon and sound
- No notification on launch (first reminder appears at the next 30-minute boundary)
- Runs automatically at Windows login (toggleable in Settings > Apps > Startup)
- Proper installer/uninstaller

## Usage

Run directly from source:

```powershell
uv run python main.py
```

Or use the packaged installer (`installer\WakeUpSetup.exe`). See [Installation](#installation).

## Installation

1. Build the executable (requires [PyInstaller](https://pyinstaller.org)):

   ```powershell
   uv run pyinstaller --onefile --noconsole --name WakeUp --icon "assets\256x256.ico" --add-data "assets;assets" main.py
   ```

2. Build the installer (requires [Inno Setup](https://jrsoftware.org/isinfo.php)):

   ```powershell
   & "C:\Users\<user_name>\AppData\Local\Programs\Inno Setup 6\ISCC.exe" installer.iss
   ```

3. Run `installer\WakeUpSetup.exe` and follow the wizard.

The installer places the app in `%LOCALAPPDATA%\WakeUp`, registers it under
**Settings > Apps > Startup** so it launches at login, and creates Start Menu
(and optional desktop) shortcuts.

## Uninstallation

- Run `WakeUpSetup.exe` again and choose Uninstall, or
- Uninstall from **Settings > Apps > Installed apps** > WakeUp

Both remove the executable, startup registration, shortcuts, and assets.

## Project layout

| Path                | Description                                  |
|---------------------|----------------------------------------------|
| `main.py`           | Application entry point                      |
| `reminders`         | Health tip messages (top of `main.py`)       |
| `assets/`           | App icon (`256x256.ico`) and toast image (`256x256.png`) |
| `dist/WakeUp.exe`   | Built executable                             |
| `installer.iss`     | Inno Setup script                            |
| `installer/WakeUpSetup.exe` | Compiled installer                   |