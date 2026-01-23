# 📥 QuickTube Installation Guide

**Super simple installation - just download and run!**

---

## Windows

### Step 1: Download

1. Go to the [Releases page](https://github.com/abdelrahman-ahmed-nassar/YouTube-Downloader-using-yt-dlp/releases/latest)
2. Download `quicktube-windows.exe`
3. Save it to a folder you can find (like `Downloads` or `Desktop`)

### Step 2: Run

- **Option A (Easy):** Double-click `quicktube-windows.exe`
- **Option B (Terminal):**
  1. Press `Win + R` to open Run dialog
  2. Type `cmd` and press Enter
  3. Navigate to where you saved the file:
     ````cmd
     cd C:\Users\YourName\Downloads
     quicktube-windows.exe
     ```### Common Windows Issues
     ````

**"Windows protected your PC" warning:**

1. Click "More info"
2. Click "Run anyway"

This warning appears because the app isn't digitally signed (costs $$$ for developers). The app is safe - it's open source!

**Want to run from anywhere?**
Move `quicktube-windows.exe` to `C:\Program Files\QuickTube\` and add it to your PATH.

---

## macOS

### Step 1: Download

1. Go to the [Releases page](https://github.com/abdelrahman-ahmed-nassar/YouTube-Downloader-using-yt-dlp/releases/latest)
2. Download `quicktube-macos`
3. Save it to your `Downloads` folder

### Step 2: Make it Executable

1. Open **Terminal** (press `Cmd + Space`, type "Terminal", press Enter)
2. Run these commands:
   ```sh
   cd ~/Downloads
   chmod +x quicktube-macos
   ```

### Step 3: Run

```sh
./quicktube-macos
```

### Common macOS Issues

**"App is damaged and can't be opened" or "Unidentified developer":**

This is macOS Gatekeeper being protective. Fix it with:

```sh
xattr -cr ~/Downloads/quicktube-macos
chmod +x ~/Downloads/quicktube-macos
./quicktube-macos
```

**OR** right-click the file → select "Open" → click "Open" in the dialog.

**Want to run from anywhere?**

Move it to `/usr/local/bin/`:

```sh
sudo mv ~/Downloads/yt-downloader-macos /usr/local/bin/yt-downloader
```

Now you can just type `yt-downloader` in any Terminal window!

---

## Linux

### Step 1: Download

1. Go to the [Releases page](https://github.com/abdelrahman-ahmed-nassar/YouTube-Media-Downloader-using-yt-dlp/releases/latest)
2. Download `yt-downloader-linux`
3. Save it to your `Downloads` folder

### Step 2: Make it Executable

Open Terminal and run:

```sh
cd ~/Downloads
chmod +x yt-downloader-linux
```

### Step 3: Run

```sh
./yt-downloader-linux
```

### Common Linux Issues

**Permission denied:**

```sh
chmod +x yt-downloader-linux
```

**Want to run from anywhere?**

Move it to `/usr/local/bin/`:

```sh
sudo mv ~/Downloads/yt-downloader-linux /usr/local/bin/yt-downloader
```

Now you can just type `yt-downloader` in any terminal!

---

## ✅ You're Done!

**No Python, no dependencies, no setup needed!**

Everything is bundled inside the executable:

- Python interpreter
- yt-dlp library
- ffmpeg binary

Just run it and start downloading! 🎉

---

## 🆘 Still Having Issues?

- Check the [README.md](README.md) troubleshooting section
- [Open an issue](https://github.com/abdelrahman-ahmed-nassar/YouTube-Media-Downloader-using-yt-dlp/issues) on GitHub
- Make sure you downloaded the correct version for your operating system

---

## 🎓 Want to Use the Python Script Instead?

If you're a developer or want to modify the code:

1. Install Python 3.6+ from [python.org](https://www.python.org/downloads/)
2. Install dependencies:
   ```sh
   pip install yt-dlp
   brew install ffmpeg  # macOS
   # or apt install ffmpeg  # Linux
   ```
3. Run the script:
   ```sh
   python3 yt-downloader.py
   ```

See [README.md](README.md) for full developer documentation.
