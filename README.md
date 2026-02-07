# ⚡ QuickTube

**The fastest way to download videos and audio from YouTube, Facebook, LinkedIn, and X - no installation required!**

[![Download Releases](https://img.shields.io/github/v/release/abdelrahman-ahmed-nassar/QuickTube-Youtube-Downloader?label=Download&style=for-the-badge)](https://github.com/abdelrahman-ahmed-nassar/QuickTube-Youtube-Downloader/releases/latest)
[![Platform Support](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-blue?style=for-the-badge)]()

## 🚀 Quick Start

**Just 3 steps to start downloading:**

1. **[Download the executable](https://github.com/abdelrahman-ahmed-nassar/QuickTube-Youtube-Downloader/releases/latest)** for your platform
2. **Run it** (double-click or run in terminal)
3. **Select your platform** (YouTube, Facebook, LinkedIn, or X)
4. **Paste a video URL** and start downloading!

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

- 🌐 **Multi-platform support** - YouTube, Facebook, LinkedIn, and X (Twitter)
- 🎬 **Download videos** in MP4 format (144p to 4K)
- 🎵 **Extract audio** in MP3 format (64kbps to 320kbps)
- 📋 **Playlist support** - download entire playlists or single videos
- 🔄 **Format conversion** - convert between MP4 and MKV formats (full or quick remux)
- 📊 **Real-time progress** - see download and conversion progress
- 🎯 **Universal compatibility** - works on all devices and players
- 🎨 **Beautiful UI** - emoji feedback and clear status messages
- 🔒 **Smart URL handling** - automatically handles tracking parameters
- 📁 **Organized output** - downloads saved to organized folders (output/mp3, output/mp4)

---

## 🎮 Usage

Simply run the executable and follow the interactive prompts:

```
============================================================
⚡ QuickTube - Universal Media Downloader ⚡
============================================================

🌐 Select platform:
   1. YouTube (default)
   2. Facebook
   3. LinkedIn
   4. X (Twitter)
Enter your choice (1-4) or press Enter for YouTube: 1

📎 Enter YouTube URL: https://www.youtube.com/watch?v=example

🔍 Checking URL...
✅ Supported! Found: Example Video Title...

📁 Select file type:
   1. MP3 (Audio only)
   2. MP4 (Video)
Enter your choice (1-2, default: 2): 2

🎬 Select video resolution:
   1. 144p
   2. 240p
   3. 360p
   4. 480p
   5. 720p (HD - Recommended)
   6. 1080p (Full HD)
   7. 1440p (2K)
   8. 2160p (4K)
Enter your choice (1-8, default: 5): 6

============================================================
⏳ Downloading MP4 (1080p)...
[Download progress shown here]
============================================================
🎉 Successfully downloaded MP4: Example Video Title.mp4
📁 Saved to: /path/to/output/mp4/Example Video Title.mp4
```

### What You Can Download

- **YouTube** - Videos, playlists, shorts, music
- **Facebook** - Public video posts
- **LinkedIn** - Public video posts and articles
- **X (Twitter)** - Public video posts and tweets
- **Playlists/Collections** - Download entire playlists or single items
- **MP3 audio** - Extract audio only in high quality (64-320 kbps)
- **MP4 videos** - Download videos with audio included (144p-4K)

### Quality Options

**Video (MP4):**

- `144p` - Lowest quality (minimal file size)
- `240p` - Low quality
- `360p` - Standard quality
- `480p` - Enhanced quality
- `720p` - HD (recommended, balanced)
- `1080p` - Full HD (high quality)
- `1440p` - 2K (very high quality)
- `2160p` - 4K (best quality, largest file)

**Audio (MP3):**

- `64 kbps` - Low quality (minimal file size)
- `128 kbps` - Good quality (recommended)
- `192 kbps` - High quality
- `320 kbps` - Highest quality (best audio)

---

## 📂 Output Location

All downloads are saved to the `output/` folder with organized subfolders:

- **Windows:** `C:\path\to\executable\output\mp3\` and `output\mp4\`
- **macOS:** `output/mp3/` and `output/mp4/` folders created next to `QuickTube.app`
- **Linux:** `/path/to/executable/output/mp3/` and `output/mp4/`

Files are named automatically based on the video title.

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
- **Update yt-dlp** - Run: `pip install --upgrade yt-dlp` (if using manual installation)
- **Try a different video** - some videos may be restricted in your region
- **Private/Age-restricted videos** may not download
- **Platform-specific issues:**
  - Facebook: Ensure video is public
  - LinkedIn: Requires public post access
  - X/Twitter: May have rate limiting

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

This tool is for personal use only. Please respect the Terms of Service and copyright laws of each platform (YouTube, Facebook, LinkedIn, X). Only download content you have permission to download.

---

**Made with ❤️ by [Abdelrahman Ahmed Nassar](https://github.com/abdelrahman-ahmed-nassar)**
