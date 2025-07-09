# Requirements

## Install uv environment

```powershell
uv sync
```

## Install [Scoop](https://scoop.sh/) to manage packages on Windows.

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression
```

## Install ffmpeg

```powershell
scoop install ffmpeg
```

# Usage

Run `main.py` to transcribe selected audio file.
