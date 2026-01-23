# ⚡ QuickTube

**The fastest way to download YouTube videos and audio - no installation required!**

[![Download Releases](https://img.shields.io/github/v/release/abdelrahman-ahmed-nassar/QuickTube-Youtube-Downloader?label=Download&style=for-the-badge)](https://github.com/abdelrahman-ahmed-nassar/QuickTube-Youtube-Downloader/releases/latest)
[![Platform Support](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-blue?style=for-the-badge)]()

## 🚀 Quick Start

**Just 3 steps to start downloading:**

1. **[Download the executable](https://github.com/abdelrahman-ahmed-nassar/QuickTube-Youtube-Downloader/releases/latest)** for your platform
2. **Run it** (double-click or run in terminal)
3. **Paste a YouTube URL** and start downloading!

**That's it!** No Python, no dependencies, no setup. Everything is bundled.

---

## 📥 Installation

### Windows

1. Download `quicktube-windows.exe` from [Releases](https://github.com/abdelrahman-ahmed-nassar/QuickTube-Youtube-Downloader/releases/latest/download/quicktube-windows.exe)
2. Double-click the file to run
3. _(Optional)_ Move to a permanent location like `C:\Program Files\QuickTube\`

### macOS

1. Download `quicktube-macos.zip` from [Releases](https://github.com/abdelrahman-ahmed-nassar/QuickTube-Youtube-Downloader/releases/latest/download/quicktube-macos.zip)
2. Double-click the zip file to extract `QuickTube.app`
3. Right-click `QuickTube.app` → **Open** → **Open** (first time only to bypass Gatekeeper)
4. The app will open in Terminal automatically
5. _(Optional)_ Move `QuickTube.app` to your Applications folder for easy access

> **Note:** macOS will show a security warning the first time. This is normal for apps not signed with an Apple Developer certificate.

### Linux

1. Download `quicktube-linux` from [Releases](https://github.com/abdelrahman-ahmed-nassar/QuickTube-Youtube-Downloader/releases/latest/download/quicktube-linux)
2. Open Terminal and navigate to your Downloads folder:
   ```sh
   cd ~/Downloads
   chmod +x quicktube-linux
   ./quicktube-linux
   ```
3. _(Optional)_ Move to `/usr/local/bin/` for system-wide access:
   ```sh
   sudo mv quicktube-linux /usr/local/bin/quicktube
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

### For Developers: Run from Source (Manual Installation)

**Don't want to download the executable?** You can run the Python script directly!

See the complete manual installation and usage guide: **[Manual Usage Guide](https://github.com/abdelrahman-ahmed-nassar/QuickTube-Youtube-Downloader/wiki/Manual-Usage)**

**Quick summary:**

**Requirements:**

- Python 3.6+
- yt-dlp: `pip install yt-dlp`
- ffmpeg: `brew install ffmpeg` (macOS) or equivalent

**Run:**

```sh
python3 quicktube.py
```

This method is perfect if you:

- Want to modify the code
- Prefer installing dependencies yourself
- Are familiar with Python development
- Need to customize the download behavior

---

## ❓ Troubleshooting

### macOS: "App is damaged and can't be opened"

This is a Gatekeeper security warning. To bypass:

```sh
xattr -cr quicktube-macos
chmod +x quicktube-macos
./quicktube-macos
```

Or right-click the file and select "Open" from the menu.

### Windows: "Windows protected your PC"

Click "More info" → "Run anyway". This happens because the executable isn't digitally signed.

### Linux: Permission Denied

Make the file executable:

```sh
chmod +x quicktube-linux
```

### Slow Downloads or Errors

- **Check your internet connection**
- **Try a different video** - some videos may be restricted in your region
- **Age-restricted videos** may not download
- **Private videos** cannot be accessed

### No Progress Display

Run in a proper terminal:

- **Windows:** Use Command Prompt or PowerShell (not Python IDLE)
- **macOS/Linux:** Use Terminal app

---

## 📖 Documentation

- **[Quick Install Guide](https://github.com/abdelrahman-ahmed-nassar/QuickTube-Youtube-Downloader/wiki/Quick-Install)** - Get started in minutes
- **[Detailed Installation Guide](https://github.com/abdelrahman-ahmed-nassar/QuickTube-Youtube-Downloader/wiki/Detailed-Installation-Guide)** - Comprehensive setup instructions
- **[Manual Usage Guide](https://github.com/abdelrahman-ahmed-nassar/QuickTube-Youtube-Downloader/wiki/Manual-Usage)** - Running from source
- **[Dependencies](https://github.com/abdelrahman-ahmed-nassar/QuickTube-Youtube-Downloader/wiki/Dependencies)** - What's bundled in the executable
- **[Developer Documentation](docs/)** - For contributors (build guides, release process)

---

## 🤝 Contributing

Contributions are welcome! Feel free to:

- Report bugs via [Issues](https://github.com/abdelrahman-ahmed-nassar/QuickTube-Youtube-Downloader/issues)
- Submit feature requests
- Create pull requests

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🌟 Support

If you find this tool useful, please:

- ⭐ Star the repository
- 🐛 Report any issues you find
- 💡 Suggest new features
- 📢 Share with others

---

## ⚠️ Disclaimer

This tool is for personal use only. Please respect YouTube's Terms of Service and copyright laws. Only download content you have permission to download.

---

**Made with ❤️ by [Abdelrahman Ahmed Nassar](https://github.com/abdelrahman-ahmed-nassar)**
