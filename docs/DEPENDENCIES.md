# QuickTube - Dependency Management

## Quick Answer

**For users with the executable files:**

| Dependency | Required? | Why?                                    |
| ---------- | --------- | --------------------------------------- |
| **Python** | ❌ NO     | Bundled in executable                   |
| **yt-dlp** | ❌ NO     | Bundled in executable                   |
| **ffmpeg** | ❌ NO     | Bundled in executable (GitHub releases) |

**Users just run the executable - nothing else needed!** ✅

---

## How It Works

### 1. Python (Bundled Automatically)

PyInstaller includes the Python interpreter in the executable.

- Users don't see Python
- No PATH configuration needed
- Works on machines without Python installed

### 2. yt-dlp (Bundled Automatically)

yt-dlp is a Python package, so PyInstaller bundles it automatically.

- All yt-dlp functionality included
- Users don't need `pip install yt-dlp`
- Updates require new executable release

### 3. ffmpeg (Can Be Bundled)

ffmpeg is an external binary program. We have two options:

#### Option A: Bundled ffmpeg (Recommended)

**Using `build-with-ffmpeg.py`:**

```sh
python3 build-with-ffmpeg.py
```

**Using GitHub Actions:**

- Automatically bundles ffmpeg in CI/CD
- See `.github/workflows/build-executables.yml`

**Result:**

- ✅ Users need nothing
- ✅ Fully portable
- ❌ Larger file size (~70-150 MB)

#### Option B: System ffmpeg (Basic Build)

**Using `build-executable.py`:**

```sh
python3 build-executable.py
```

**Result:**

- ✅ Smaller file size (~15-25 MB)
- ❌ Users must install ffmpeg separately

---

## Building with Bundled ffmpeg

### Local Build

```sh
# Simple - downloads and bundles ffmpeg automatically
python3 build-with-ffmpeg.py
```

The script:

1. Downloads ffmpeg for your platform
2. Bundles it with PyInstaller
3. Creates fully portable executable
4. Cleans up temporary files

### GitHub Actions Build

GitHub Actions workflow automatically:

1. Downloads ffmpeg on each platform
2. Bundles with PyInstaller
3. Uploads executables to releases

**No manual work needed!**

---

## File Size Comparison

| Build Type         | Windows | macOS  | Linux  |
| ------------------ | ------- | ------ | ------ |
| **Without ffmpeg** | ~20 MB  | ~15 MB | ~18 MB |
| **With ffmpeg**    | ~100 MB | ~70 MB | ~90 MB |

---

## For Users: What to Download

### Pre-built Executables (From GitHub Releases)

**Includes everything:**

- ✅ Python interpreter
- ✅ yt-dlp library
- ✅ ffmpeg binary

**Download and run - that's it!**

```sh
# Windows
yt-downloader-windows.exe

# macOS
chmod +x yt-downloader-macos
./yt-downloader-macos

# Linux
chmod +x yt-downloader-linux
./yt-downloader-linux
```

---

## For Developers: Building Options

### Option 1: Basic Build (Requires User to Install ffmpeg)

```sh
python3 build-executable.py
```

**Pros:**

- Small file size
- Fast build

**Cons:**

- Users need to install ffmpeg
- Extra setup step for users

### Option 2: Full Build (Everything Included)

```sh
python3 build-with-ffmpeg.py
```

**Pros:**

- Zero user setup
- Truly portable
- Professional

**Cons:**

- Larger file size
- Longer build time

### Option 3: GitHub Actions (Recommended)

Push to GitHub and create a release:

```sh
git tag v1.0.0
git push origin v1.0.0
```

**Pros:**

- Builds for all platforms automatically
- Bundles ffmpeg
- No local build needed
- Free for public repos

**Cons:**

- Requires GitHub repository

---

## Technical Details

### How ffmpeg is Bundled

PyInstaller's `--add-binary` flag:

```sh
# Windows
pyinstaller --add-binary "ffmpeg.exe;." yt-downloader.py

# macOS/Linux
pyinstaller --add-binary "ffmpeg:." yt-downloader.py
```

### How Script Finds ffmpeg

The script automatically detects bundled ffmpeg:

```python
def get_ffmpeg_path():
    """Get the path to ffmpeg binary (bundled or system)"""
    if getattr(sys, 'frozen', False):
        # Running as compiled executable
        base_path = sys._MEIPASS
        ffmpeg_name = "ffmpeg.exe" if os.name == 'nt' else "ffmpeg"
        bundled_ffmpeg = os.path.join(base_path, ffmpeg_name)
        if os.path.exists(bundled_ffmpeg):
            return bundled_ffmpeg
    # Fall back to system ffmpeg
    return "ffmpeg"
```

**When running as executable:**

- Uses bundled ffmpeg from `sys._MEIPASS` temp directory

**When running as Python script:**

- Falls back to system ffmpeg

---

## Troubleshooting

### "ffmpeg not found" Error

**If using executable:**

- Executable was built without ffmpeg bundled
- User needs to install ffmpeg separately

**If using Python script:**

- Install ffmpeg: `brew install ffmpeg` (macOS) or see README

### Large File Size

This is normal when bundling ffmpeg:

- ffmpeg alone is ~60-80 MB
- Python interpreter is ~15-20 MB
- Total: ~70-150 MB

**Can't be reduced significantly while keeping full functionality.**

### Build Takes Long Time

Building with ffmpeg download:

- Downloads ~50-100 MB
- May take 2-5 minutes
- Only needed once per platform

---

## Recommendation

**For distribution:**

- ✅ Use GitHub Actions with bundled ffmpeg
- ✅ Provides best user experience
- ✅ No user setup required
- ✅ Professional appearance

**For development:**

- Use Python script directly
- Install ffmpeg on your system once
- Faster iteration during development

---

## Summary

**Executable users need:** NOTHING ✅

**Python script users need:**

- Python 3.6+
- yt-dlp: `pip install yt-dlp`
- ffmpeg: `brew install ffmpeg` (or platform equivalent)

**Your GitHub releases include everything users need!** 🎉
