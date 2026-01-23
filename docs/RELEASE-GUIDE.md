# Creating Your First Release

This guide walks you through creating your first release with executables for all platforms.

## Prerequisites

- Your code is on GitHub
- `.github/workflows/build-executables.yml` exists in your repository

## Step-by-Step Guide

### 1. Prepare Your Code

Make sure all changes are committed:

```sh
git status  # Check for uncommitted changes
git add .
git commit -m "Prepare for v1.0.0 release"
git push origin main
```

### 2. Create a Version Tag

```sh
# Create a tag for version 1.0.0
git tag v1.0.0

# Push the tag to GitHub
git push origin v1.0.0
```

### 3. Create the Release on GitHub

**Option A: Via GitHub Website (Recommended)**

1. Go to your repository on GitHub
2. Click on "Releases" (right sidebar)
3. Click "Draft a new release"
4. Fill in the details:
   - **Tag:** Select `v1.0.0` (or create new tag)
   - **Release title:** `Version 1.0.0 - Initial Release`
   - **Description:**
     ```markdown
     ## What's New
     
     - YouTube video and playlist downloader
     - MP3 and MP4 format support
     - Quality selection (low, medium, high)
     - Video format conversion (MP4/MKV)
     - QuickTime Player compatible output
     - Real-time progress display
     
     ## Installation
     
     ### Pre-built Executables (No Python Required)
     
     Download the executable for your platform:
     - **Windows:** `yt-downloader-windows.exe`
     - **macOS:** `yt-downloader-macos`
     - **Linux:** `yt-downloader-linux`
     
     **Requirements:**
     - Only ffmpeg needs to be installed ([ffmpeg.org](https://ffmpeg.org))
     
     ### Python Script
     
     Requires Python 3.6+ and dependencies:
     ```sh
     pip install yt-dlp
     python yt-downloader.py
     ```
     
     ## Usage
     
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
     
     See [README.md](README.md) for full documentation.
     ```
5. Click "Publish release"

**Option B: Via Command Line (Advanced)**

Using GitHub CLI (`gh`):

```sh
# Install GitHub CLI first: https://cli.github.com/

gh release create v1.0.0 \
  --title "Version 1.0.0 - Initial Release" \
  --notes "See README.md for details"
```

### 4. Wait for Build to Complete

1. Go to the "Actions" tab in your repository
2. You'll see the "Build Executables" workflow running
3. Wait 5-10 minutes for all three builds to complete
4. ✅ Green checkmarks mean success!

### 5. Verify the Release

1. Go back to "Releases"
2. Click on your release
3. You should see three executable files attached:
   - `yt-downloader-windows.exe`
   - `yt-downloader-macos`
   - `yt-downloader-linux`

### 6. Update Release Description (If Needed)

If the executables didn't auto-attach (older workflows):

1. Edit your release
2. Manually upload the files from the Actions artifacts
3. Save changes

## Testing Your Release

### Download and Test Each Executable

**Windows:**
```cmd
# Download yt-downloader-windows.exe
# Double-click or run in Command Prompt
yt-downloader-windows.exe
```

**macOS:**
```sh
# Download yt-downloader-macos
chmod +x yt-downloader-macos
./yt-downloader-macos
```

**Linux:**
```sh
# Download yt-downloader-linux
chmod +x yt-downloader-linux
./yt-downloader-linux
```

## Future Releases

For subsequent releases:

```sh
# 1. Make your changes
git add .
git commit -m "Add new feature"
git push origin main

# 2. Create new tag
git tag v1.1.0
git push origin v1.1.0

# 3. Create release on GitHub (same as before)
# GitHub Actions will automatically build all executables
```

## Version Numbering

Follow [Semantic Versioning](https://semver.org/):

- **v1.0.0** - Initial release
- **v1.0.1** - Bug fixes
- **v1.1.0** - New features (backward compatible)
- **v2.0.0** - Breaking changes

Examples:
- Fixed a bug: `v1.0.0` → `v1.0.1`
- Added playlist support: `v1.0.1` → `v1.1.0`
- Changed command-line interface: `v1.1.0` → `v2.0.0`

## Troubleshooting

### Build Failed

1. Go to Actions tab
2. Click on the failed workflow
3. Check error logs
4. Common issues:
   - Missing dependencies in workflow file
   - Python syntax errors
   - PyInstaller issues

### Executables Missing from Release

1. Check if workflow completed successfully
2. If successful, manually download artifacts:
   - Go to Actions → Click on workflow run
   - Download artifacts at the bottom
   - Upload manually to release

### Executables Don't Work

- Windows: May be blocked by antivirus (false positive)
- macOS: Users need to right-click → Open (first time only)
- Linux: Ensure execute permissions (`chmod +x`)

## Advanced: Pre-release Testing

Test builds before official release:

```sh
# Create pre-release tag
git tag v1.0.0-beta.1
git push origin v1.0.0-beta.1

# Create release and mark as "pre-release"
# Test thoroughly before promoting to full release
```

## Getting Your Release to Users

### Announce Your Release

1. Update README.md with release notes
2. Post on social media (Twitter, Reddit, etc.)
3. Submit to relevant communities
4. Add to package managers (Homebrew, Chocolatey, etc.)

### Example Announcement:

```
🎉 yt-downloader v1.0.0 is now available!

Download YouTube videos and audio with ease:
✅ Standalone executables (no Python required)
✅ MP3/MP4 support with quality selection
✅ QuickTime compatible output
✅ Real-time progress display

Download: https://github.com/yourusername/yt-downloader/releases/latest

#YouTube #Downloader #OpenSource
```

## Need Help?

- Check [CROSS-PLATFORM-BUILD.md](CROSS-PLATFORM-BUILD.md) for detailed build instructions
- See [BUILD-EXECUTABLE.md](BUILD-EXECUTABLE.md) for local builds
- Open an issue on GitHub if you encounter problems

---

**Ready to create your first release?** Follow the steps above! 🚀
