# AGENTS.md

Guidance for AI agents and contributors working on this project.

## Overview

WakeUp is a Windows-only reminder app. It runs an infinite loop, sleeps until the
next 30-minute boundary, then shows a random health tip as a Windows toast
notification using `winotify`. It is packaged as a single-file executable with
PyInstaller and distributed with an Inno Setup installer.

## Commands

- Run from source: `uv run python main.py`
- Build exe: `uv run pyinstaller --onefile --noconsole --name WakeUp --icon "assets\256x256.ico" --add-data "assets;assets" main.py`
- Build installer: `& "C:\Users\faithX\AppData\Local\Programs\Inno Setup 6\ISCC.exe" installer.iss`

## Conventions

- Python dependencies are managed with `uv` (see `pyproject.toml`). Add deps with `uv add`.
- Do not add code comments unless the task explicitly requires them.
- `winotify` requires `set_audio()` to be called **before** `show()`; `show()` serializes
  the toast XML from the notification state at call time.
- Toast icons must be an absolute path to a PNG; `.ico` files are not reliably rendered
  in toast images. Resolve paths via `getattr(sys, "_MEIPASS", ...)` so they work both
  from source and from the frozen exe.
- When building the exe, `--add-data "assets;assets"` must be passed so the icon is bundled
  into the onefile archive (`_MEIPASS` points at the extracted location).
- `installer.iss` must list any new bundled assets under `[Files]` and corresponding
  cleanup under `[UninstallDelete]`.

## Startup registration

The app registers itself for auto-start via the HKCU Run key
(`Software\Microsoft\Windows\CurrentVersion\Run`) in `installer.iss`, which makes it
toggleable in Windows Settings > Apps > Startup.

## Testing

There is no formal test suite. To verify toast output without showing a real
notification, monkeypatch `winotify._run_ps` to capture the generated PowerShell
script and assert it contains the expected `<audio>` element and icon path.