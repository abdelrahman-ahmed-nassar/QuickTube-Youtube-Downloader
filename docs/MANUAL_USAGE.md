# ⚡ QuickTube - Manual Installation Guide

**Fast YouTube downloads - run from source code**

[![Download Releases](https://img.shields.io/github/v/release/abdelrahman-ahmed-nassar/YouTube-Media-Downloader-using-yt-dlp?label=Download&style=for-the-badge)](https://github.com/abdelrahman-ahmed-nassar/YouTube-Media-Downloader-using-yt-dlp/releases/latest)
[![Platform Support](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-blue?style=for-the-badge)]()

## 🚀 Quick Start

**Just 3 steps to start downloading:**

1. **[Download the executable](https://github.com/abdelrahman-ahmed-nassar/YouTube-Media-Downloader-using-yt-dlp/releases/latest)** for your platform
2. **Run it** (double-click or run in terminal)
3. **Paste a YouTube URL** and start downloading!

**That's it!** No Python, no dependencies, no setup. Everything is bundled.

---

## 📥 Installation

### Windows

1. Download `yt-downloader-windows.exe` from [Releases](https://github.com/abdelrahman-ahmed-nassar/YouTube-Media-Downloader-using-yt-dlp/releases/latest)
2. Double-click the file to run
3. _(Optional)_ Move to a permanent location like `C:\Program Files\yt-downloader\`

### macOS

1. Download `yt-downloader-macos` from [Releases](https://github.com/abdelrahman-ahmed-nassar/YouTube-Media-Downloader-using-yt-dlp/releases/latest)
2. Open Terminal and navigate to your Downloads folder:
   ```sh
   cd ~/Downloads
   chmod +x yt-downloader-macos
   ./yt-downloader-macos
   ```
3. _(Optional)_ Move to `/usr/local/bin/` for system-wide access:
   ```sh
   sudo mv yt-downloader-macos /usr/local/bin/yt-downloader
   ```

### Linux

1. Download `yt-downloader-linux` from [Releases](https://github.com/abdelrahman-ahmed-nassar/YouTube-Media-Downloader-using-yt-dlp/releases/latest)
2. Open Terminal and navigate to your Downloads folder:
   ```sh
   cd ~/Downloads
   chmod +x yt-downloader-linux
   ./yt-downloader-linux
   ```
3. _(Optional)_ Move to `/usr/local/bin/` for system-wide access:
   ```sh
   sudo mv yt-downloader-linux /usr/local/bin/yt-downloader
   ```

> **✅ No dependencies required!** Python, yt-dlp, and ffmpeg are all bundled in the executable.

---

## ✨ Features

- 🎬 **Download YouTube videos** in MP4 format (360p, 720p, 1080p)
- 🎵 **Extract audio** in MP3 format (50kbps, 128kbps, 192kbps)
- 📋 **Playlist support** - download entire playlists or single videos
- 🔄 **Format conversion** - convert between MP4 and MKV formats
- 📊 **Real-time progress** - see download and conversion progress
- 🎯 **QuickTime compatible** - works on all Apple devices and players
- 🌐 **Universal compatibility** - plays on VLC, Windows Media Player, and all modern devices
- 🎨 **Beautiful UI** - emoji feedback and clear status messages
- 🔒 **SSL handling** - automatic certificate management
- 📁 **Organized output** - all downloads saved to `output/` folder

---

## 🎮 Usage

Simply run the executable and follow the interactive prompts:

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
```

### What You Can Download

- **Single videos** - just paste the video URL
- **Playlists** - paste playlist URL and choose to download all or single video
- **MP3 audio** - extract audio only in high quality
- **MP4 videos** - download videos with audio included

### Quality Options

**Video (MP4):**

- `low` - 360p (small file size)
- `medium` - 720p HD (balanced)
- `high` - 1080p Full HD (best quality)

**Audio (MP3):**

- `low` - 50kbps (minimal file size)
- `medium` - 128kbps (good quality)
- `high` - 192kbps (excellent quality)

---

## 📂 Output Location

All downloads are saved to the `output/` folder:

- **Windows:** `C:\path\to\executable\output\`
- **macOS:** `/path/to/executable/output/`
- **Linux:** `/path/to/executable/output/`

Files are named automatically based on the YouTube video title.

---

## 🛠️ Advanced Usage

### For Developers: Run from Source

If you want to modify the code or run from source:

**Requirements:**

- Python 3.6+
- yt-dlp: `pip install yt-dlp`
- ffmpeg: `brew install ffmpeg` (macOS) or equivalent

**Run:**

```sh
python3 quicktube.py
```

### Build Your Own Executable

Want to build the executable yourself? See [docs/BUILD-EXECUTABLE.md](docs/BUILD-EXECUTABLE.md)

### Create Cross-Platform Builds

See [docs/CROSS-PLATFORM-BUILD.md](docs/CROSS-PLATFORM-BUILD.md) for building executables for all platforms

## Usage

Run the script in a terminal:

```sh
# Windows (Command Prompt or PowerShell)
python quicktube.py

# macOS/Linux
python3 quicktube.py
```

### Navigating to the Script Directory

**Windows (Command Prompt):**

```cmd
cd C:\Users\YourName\Downloads\YOUTUBE-MEDIA-DOWNLOADER-USING-YT-DLP
python quicktube.py
```

**Windows (PowerShell):**

```powershell
cd C:\Users\YourName\Downloads\YOUTUBE-MEDIA-DOWNLOADER-USING-YT-DLP
python quicktube.py
```

**macOS (Terminal):**

```sh
cd ~/Downloads/YOUTUBE-MEDIA-DOWNLOADER-USING-YT-DLP
python3 quicktube.py
```

**Linux (Terminal):**

```sh
cd ~/Downloads/YOUTUBE-MEDIA-DOWNLOADER-USING-YT-DLP
python3 quicktube.py
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
chmod +x quicktube.py
python3 quicktube.py
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
