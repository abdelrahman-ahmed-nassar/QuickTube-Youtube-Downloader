# YouTube Media Downloader

## Overview

This script allows users to download and convert YouTube videos and playlists into MP3 or MP4 formats. It utilizes `yt-dlp` for downloading and `ffmpeg` for conversion, ensuring high-quality media processing.

## Features

- Download YouTube videos or entire playlists
- Convert downloaded videos to MP4 or MKV format
- Supports multiple quality options for both audio and video
- Real-time download and conversion progress display
- QuickTime Player compatible MP4 output (yuv420p pixel format)
- User-friendly interface with emoji feedback and clear status messages
- Input validation with helpful error messages
- Automatic SSL certificate handling
- Uses `yt-dlp` for reliable downloads
- Uses `ffmpeg` for high-quality media conversion

## Prerequisites

Ensure you have the following installed on your system:

- **Python** (latest version recommended)
- **yt-dlp** (`pip install yt-dlp`)
- **ffmpeg** (install via package manager or download from [ffmpeg.org](https://ffmpeg.org))

### Installing Prerequisites

**For Python:**

```sh
# Windows (using official installer)
# Download Python from: https://www.python.org/downloads/
# Run the installer and follow the setup instructions

# Windows (using winget)
winget install Python.Python.3

# macOS (using Homebrew)
brew install python

# Linux (Ubuntu/Debian)
sudo apt install python3

# Linux (Fedora)
sudo dnf install python3
```

**For yt-dlp:**

```sh
pip install yt-dlp
```

**For ffmpeg:**

- **Windows:**
  1.  Download the latest build from [gyan.dev/ffmpeg/builds/ffmpeg-git-full.7z](https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-full.7z).
  2.  Extract the archive to a folder, e.g., `C:\ffmpeg`.
  3.  Open the extracted folder and go to the `bin` directory.
  4.  You will find `ffmpeg.exe`, `ffplay.exe`, and `ffprobe.exe` inside `bin`.
  5.  Add the full path to the `bin` folder (e.g., `C:\ffmpeg\bin`) to your system PATH environment variable:
      - Open the Start menu and search for **Environment Variables**.
      - Click **Edit the system environment variables**.
      - In the System Properties window, click **Environment Variables...**
      - Under **System variables**, find and select the **Path** variable, then click **Edit**.
      - Click **New** and add the path to your ffmpeg `bin` folder (e.g., `C:\ffmpeg\bin`).
      - Click **OK** to save and close all windows.
  6.  Open a new Command Prompt and run `ffmpeg -version` to verify the installation.
- **macOS:** `brew install ffmpeg`
- **Linux (Ubuntu/Debian):** `sudo apt install ffmpeg`
- **Linux (Fedora):** `sudo dnf install ffmpeg`

To verify installation, open a terminal/command prompt and type:

```sh
python --version
yt-dlp --version
ffmpeg -version
```

## Installation

1. Clone or download the script.
2. Ensure `python`, `yt-dlp` and `ffmpeg` are installed and accessible from the command line.

> **Windows users:** For a step-by-step installation guide (including Python setup and environment variables), see the **Windows Installation Guide** section in [Detailed Installation Guide](https://github.com/abdelrahman-ahmed-nassar/YouTube-Media-Downloader-using-yt-dlp/wiki/Detailed-Installation-Guide).

## Usage

Run the script in a terminal:

```sh
# Windows (Command Prompt or PowerShell)
python yt-downloader.py

# macOS/Linux
python3 yt-downloader.py
```

### Navigating to the Script Directory

**Windows (Command Prompt):**

```cmd
cd C:\Users\YourName\Downloads\YOUTUBE-MEDIA-DOWNLOADER-USING-YT-DLP
python yt-downloader.py
```

**Windows (PowerShell):**

```powershell
cd C:\Users\YourName\Downloads\YOUTUBE-MEDIA-DOWNLOADER-USING-YT-DLP
python yt-downloader.py
```

**macOS (Terminal):**

```sh
cd ~/Downloads/YOUTUBE-MEDIA-DOWNLOADER-USING-YT-DLP
python3 yt-downloader.py
```

**Linux (Terminal):**

```sh
cd ~/Downloads/YOUTUBE-MEDIA-DOWNLOADER-USING-YT-DLP
python3 yt-downloader.py
```

Follow the prompts:

1. Enter the YouTube video or playlist URL.
2. Choose whether to download an entire playlist or a single video.
3. Select the file type (`mp3` or `mp4`).
4. Select the quality level (`low`, `medium`, or `high`).
5. If downloading an MP4 file, you may choose to convert it to another format.

### Example Usage

**Download a single video in MP4 format with high quality:**

```
============================================================
🎵 YouTube Media Downloader 🎵
============================================================

📎 Enter YouTube URL: https://www.youtube.com/watch?v=example
📁 Enter file type (mp3/mp4): mp4

🔊 Choose quality: low, medium, high
Enter quality (default: medium): high

============================================================
⏳ Downloading MP4 (HIGH quality)...
[Download progress shown here]
============================================================
🎉 Successfully downloaded MP4: video-title.mp4
📁 Saved to: /path/to/output/video-title.mp4

🎬 Do you want to convert the file to another format? (yes/no): no
============================================================
```

**Download an MP3 file with medium quality:**

```
📎 Enter YouTube URL: https://www.youtube.com/watch?v=example
📁 Enter file type (mp3/mp4): mp3

🔊 Choose quality: low, medium, high
Enter quality (default: medium):

⏳ Downloading MP3 (MEDIUM quality)...
[Download progress shown here]
🎉 Successfully downloaded MP3: audio-title.mp3
📁 Saved to: /path/to/output/audio-title.mp3
```

## Output

- All downloaded media will be stored in the `output/` directory (relative to the script location)
- Converted video files will be stored in the same directory with the `_converted` suffix
- Original files are kept after conversion

**Output Paths:**

- **Windows:** `C:\path\to\script\output\video-title.mp4`
- **macOS:** `/Users/YourName/path/to/script/output/video-title.mp4`
- **Linux:** `/home/username/path/to/script/output/video-title.mp4`

## Troubleshooting

### SSL Certificate Errors

**macOS:**

```sh
# Install Python certificates
/Applications/Python\ 3.*/Install\ Certificates.command

# Or update certifi
pip3 install --upgrade certifi
```

**Windows:**

```cmd
# Update certifi
pip install --upgrade certifi

# Or reinstall Python with "Install pip" and "Add Python to PATH" options checked
```

**Linux:**

```sh
# Ubuntu/Debian
sudo apt install ca-certificates
sudo update-ca-certificates

# Fedora
sudo dnf install ca-certificates
sudo update-ca-trust

# Or update certifi
pip3 install --upgrade certifi
```

### Python Command Not Found

**Windows:**

- Use `python` instead of `python3`
- Ensure Python is added to PATH during installation
- Reinstall Python with "Add Python to PATH" option checked

**macOS/Linux:**

- Use `python3` instead of `python`
- Install Python via package manager (see Prerequisites section)

### No Progress Display

**All Platforms:**

- Run the script in a proper terminal (Command Prompt, PowerShell, Terminal, etc.)
- Avoid running through IDE output panels

**Windows:**

- Use Command Prompt or PowerShell, not Python IDLE
- Enable ANSI color support in older Windows versions

### Conversion Hangs

**All Platforms:**

- The script includes a 5-minute timeout for conversions
- For very large files, this may need adjustment in the code
- Press `Ctrl+C` (Windows/Linux) or `Cmd+C` (macOS) to cancel

### Invalid Format Errors

**All Platforms:**
Always enter exact formats as prompted:

- File type: `mp3` or `mp4` (lowercase)
- Conversion format: `mp4` or `mkv` (lowercase)

### Permission Denied Errors

**macOS/Linux:**

```sh
# If you encounter permission issues
chmod +x yt-downloader.py
python3 yt-downloader.py
```

**Windows:**

- Run Command Prompt or PowerShell as Administrator
- Check antivirus software isn't blocking the script

## Notes

- If a playlist URL is provided, the script will prompt you to download the full playlist or just a single video.
- MP4 files are downloaded with H.264 video codec and AAC audio codec in yuv420p pixel format for maximum compatibility.
- Videos are compatible with QuickTime Player, VLC, iOS devices, Android devices, and all modern media players.
- MP3 files are extracted with the specified bitrate (50K for low, 128K for medium, 192K for high).
- Video quality options: low (360p), medium (720p), high (1080p).
- Conversion supports MP4 and MKV formats with optimized settings.
- The script shows real-time progress for both downloads and conversions.
- Downloaded files are automatically named using the YouTube video title.
- All output files include success confirmations with full file paths.

## License

This script is open-source and available for use and modification under the MIT License.

## Detailed Version

For advanced configuration options, troubleshooting tips, and developer documentation, please refer to the [Detailed Installation Guide](https://github.com/abdelrahman-ahmed-nassar/YouTube-Media-Downloader-using-yt-dlp/wiki/Detailed-Installation-Guide) file included with this project.
