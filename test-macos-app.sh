#!/bin/bash
set -e

echo "🧪 Testing macOS .app bundle creation locally..."
echo ""

# Clean up any previous builds
echo "🧹 Cleaning up previous builds..."
rm -rf build dist QuickTube.app quicktube-macos.zip ffmpeg yt-dlp 2>/dev/null || true

# Download dependencies
echo "📥 Downloading ffmpeg..."
curl -L -o ffmpeg.zip "https://evermeet.cx/ffmpeg/getrelease/ffmpeg/zip"
unzip -q ffmpeg.zip
chmod +x ffmpeg
rm ffmpeg.zip

echo "📥 Downloading yt-dlp..."
curl -L -o yt-dlp "https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp_macos"
chmod +x yt-dlp

# Build with PyInstaller
echo "🔨 Building executable with PyInstaller..."
pyinstaller --onefile --name QuickTube --console --add-binary "ffmpeg:." --add-binary "yt-dlp:." quicktube.py

# Create .app bundle structure
echo "📦 Creating .app bundle structure..."
mkdir -p QuickTube.app/Contents/MacOS
mkdir -p QuickTube.app/Contents/Resources

# Move the executable
echo "📦 Moving executable into bundle..."
mv dist/QuickTube QuickTube.app/Contents/MacOS/

# Create launcher script that opens Terminal
echo "📝 Creating launcher script..."
cat > QuickTube.app/Contents/MacOS/launcher.sh << 'EOF'
#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
open -a Terminal "$DIR/QuickTube"
EOF
chmod +x QuickTube.app/Contents/MacOS/launcher.sh

# Create Info.plist
echo "📝 Creating Info.plist..."
cat > QuickTube.app/Contents/Info.plist << 'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CFBundleExecutable</key>
    <string>launcher.sh</string>
    <key>CFBundleName</key>
    <string>QuickTube</string>
    <key>CFBundleIdentifier</key>
    <string>com.quicktube.app</string>
    <key>CFBundleVersion</key>
    <string>1.0</string>
    <key>CFBundlePackageType</key>
    <string>APPL</string>
    <key>LSMinimumSystemVersion</key>
    <string>10.13</string>
</dict>
</plist>
EOF

# Create zip archive
echo "📦 Creating zip archive..."
zip -r quicktube-macos.zip QuickTube.app

echo ""
echo "✅ Build complete!"
echo ""
echo "📂 Files created:"
echo "  - QuickTube.app (macOS application)"
echo "  - quicktube-macos.zip (distribution archive)"
echo ""
echo "🧪 Testing options:"
echo ""
echo "1. Test the executable directly:"
echo "   ./QuickTube.app/Contents/MacOS/QuickTube"
echo ""
echo "2. Test the launcher script:"
echo "   ./QuickTube.app/Contents/MacOS/launcher.sh"
echo ""
echo "3. Test double-clicking QuickTube.app in Finder"
echo "   (Open Finder, navigate to this folder, double-click QuickTube.app)"
echo ""
echo "4. Test the .app from command line:"
echo "   open QuickTube.app"
echo ""
echo "💡 If you get security warnings, right-click the .app and select 'Open'"
