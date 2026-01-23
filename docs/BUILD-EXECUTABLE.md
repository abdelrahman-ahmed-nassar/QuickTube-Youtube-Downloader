# Building Standalone Executables

This guide explains how to create standalone executable files for yt-downloader that don't require Python installation.

> **💡 Building for all platforms?** See [CROSS-PLATFORM-BUILD.md](CROSS-PLATFORM-BUILD.md) for instructions on building Windows, macOS, and Linux executables from any platform using GitHub Actions.

## Quick Start

### Option 1: Use the Build Script (Easiest)

```sh
# Run the automated build script
python3 build-executable.py
```

The script will:

- Check if PyInstaller is installed
- Install PyInstaller if needed
- Build the executable for your platform
- Place it in the `dist/` folder

### Option 2: Manual Build

```sh
# Install PyInstaller
pip install pyinstaller

# Build the executable
pyinstaller --onefile --name yt-downloader --console yt-downloader.py

# Find the executable in dist/ folder
```

## Platform-Specific Instructions

### Windows

**Build on Windows:**

```cmd
python build-executable.py
```

**Output:**

- `dist/yt-downloader.exe` (approximately 15-50 MB)

**Distribute:**

- Users can run `yt-downloader.exe` directly
- No Python installation required
- ffmpeg still needs to be installed separately

### macOS

**Build on macOS:**

```sh
python3 build-executable.py
```

**Output:**

- `dist/yt-downloader` (Unix executable)

**Distribute:**

```sh
# Users may need to make it executable
chmod +x yt-downloader
./yt-downloader
```

**Note:** macOS users may see a security warning. They need to:

1. Go to System Preferences > Security & Privacy
2. Click "Open Anyway" for yt-downloader

### Linux

**Build on Linux:**

```sh
python3 build-executable.py
```

**Output:**

- `dist/yt-downloader` (Unix executable)

**Distribute:**

```sh
# Make executable
chmod +x yt-downloader
./yt-downloader
```

## Important Notes

### Dependencies

- **yt-dlp**: Bundled automatically with the executable
- **ffmpeg**: Must be installed separately by users (same as before)

### File Size

- Windows: ~15-50 MB (includes Python interpreter)
- macOS/Linux: ~15-40 MB

### Cross-Platform Building

- **Windows executables** can only be built on Windows
- **macOS executables** can only be built on macOS
- **Linux executables** can only be built on Linux

To support all platforms, you need to build on each platform separately.

## Advanced Options

### Custom Icon

Add an icon to your executable:

**Windows:**

```sh
pyinstaller --onefile --icon=icon.ico --name yt-downloader yt-downloader.py
```

**macOS:**

```sh
pyinstaller --onefile --icon=icon.icns --name yt-downloader yt-downloader.py
```

### Reduce File Size

Use UPX compression (optional):

```sh
pip install upx
pyinstaller --onefile --upx-dir=/path/to/upx --name yt-downloader yt-downloader.py
```

### Debug Build

If you encounter issues:

```sh
pyinstaller --onefile --console --debug all --name yt-downloader yt-downloader.py
```

## Testing the Executable

After building:

1. Navigate to the `dist/` folder
2. Run the executable:

   ```sh
   # Windows
   dist\yt-downloader.exe

   # macOS/Linux
   ./dist/yt-downloader
   ```

3. Test all features (download MP3, MP4, conversion, etc.)

## Distribution

### GitHub Releases

1. Build executables on each platform
2. Create a GitHub release
3. Upload executables:
   - `yt-downloader-windows.exe`
   - `yt-downloader-macos`
   - `yt-downloader-linux`

### User Instructions

Users only need to:

1. Download the executable for their platform
2. Install ffmpeg (same as before)
3. Run the executable - no Python required!

## Troubleshooting

### "PyInstaller not found"

```sh
pip install pyinstaller
```

### "Module not found" errors

Ensure all dependencies are installed:

```sh
pip install yt-dlp
```

### Antivirus False Positives

Some antivirus software may flag PyInstaller executables. This is normal for packed executables.

### Large File Size

This is expected - the executable includes the Python interpreter and all dependencies.

## Cleanup

After building, you can delete temporary files:

```sh
# Remove build artifacts
rm -rf build/
rm -rf __pycache__/
rm *.spec
```

Keep the `dist/` folder - it contains your executable!
