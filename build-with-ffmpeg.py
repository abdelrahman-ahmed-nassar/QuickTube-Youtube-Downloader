#!/usr/bin/env python3
"""
Advanced build script that bundles ffmpeg with the executable
"""

import subprocess
import sys
import platform
import os
import urllib.request
import zipfile
import tarfile
import shutil

def download_ffmpeg():
    """Download ffmpeg binary for the current platform"""
    system = platform.system()
    ffmpeg_dir = "ffmpeg_binaries"
    
    print(f"📥 Downloading ffmpeg for {system}...")
    
    if system == "Windows":
        # Download Windows ffmpeg
        url = "https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip"
        zip_path = "ffmpeg.zip"
        urllib.request.urlretrieve(url, zip_path)
        
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(ffmpeg_dir)
        
        # Find ffmpeg.exe
        for root, dirs, files in os.walk(ffmpeg_dir):
            if "ffmpeg.exe" in files:
                ffmpeg_path = os.path.join(root, "ffmpeg.exe")
                shutil.copy(ffmpeg_path, "ffmpeg.exe")
                print(f"✅ ffmpeg.exe extracted")
                break
        
        os.remove(zip_path)
        shutil.rmtree(ffmpeg_dir)
        return "ffmpeg.exe"
    
    elif system == "Darwin":  # macOS
        # Download macOS ffmpeg
        url = "https://evermeet.cx/ffmpeg/getrelease/ffmpeg/zip"
        zip_path = "ffmpeg.zip"
        urllib.request.urlretrieve(url, zip_path)
        
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(".")
        
        os.remove(zip_path)
        os.chmod("ffmpeg", 0o755)
        print(f"✅ ffmpeg extracted")
        return "ffmpeg"
    
    elif system == "Linux":
        # Download Linux ffmpeg static build
        url = "https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz"
        tar_path = "ffmpeg.tar.xz"
        urllib.request.urlretrieve(url, tar_path)
        
        with tarfile.open(tar_path, 'r:xz') as tar_ref:
            tar_ref.extractall(ffmpeg_dir)
        
        # Find ffmpeg binary
        for root, dirs, files in os.walk(ffmpeg_dir):
            if "ffmpeg" in files:
                ffmpeg_path = os.path.join(root, "ffmpeg")
                shutil.copy(ffmpeg_path, "ffmpeg")
                os.chmod("ffmpeg", 0o755)
                print(f"✅ ffmpeg extracted")
                break
        
        os.remove(tar_path)
        shutil.rmtree(ffmpeg_dir)
        return "ffmpeg"

def download_ytdlp():
    """Download yt-dlp binary for the current platform"""
    system = platform.system()
    
    print(f"📥 Downloading yt-dlp for {system}...")
    
    if system == "Windows":
        url = "https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp.exe"
        filename = "yt-dlp.exe"
    elif system == "Darwin":  # macOS
        url = "https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp_macos"
        filename = "yt-dlp"
    else:  # Linux
        url = "https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp"
        filename = "yt-dlp"
    
    try:
        urllib.request.urlretrieve(url, filename)
        
        # Make executable on Unix-like systems
        if system != "Windows":
            os.chmod(filename, 0o755)
        
        print(f"✅ {filename} downloaded")
        return filename
    except Exception as e:
        print(f"⚠️ Could not download yt-dlp: {e}")
        return None

def build_with_ffmpeg():
    """Build executable with ffmpeg and yt-dlp bundled"""
    system = platform.system()
    
    print("=" * 60)
    print("🔨 Building executable with bundled ffmpeg and yt-dlp...")
    print("=" * 60)
    
    # Download ffmpeg
    try:
        ffmpeg_binary = download_ffmpeg()
    except Exception as e:
        print(f"⚠️  Could not download ffmpeg: {e}")
        print("Building without bundled ffmpeg...")
        ffmpeg_binary = None
    
    # Download yt-dlp
    try:
        ytdlp_binary = download_ytdlp()
    except Exception as e:
        print(f"⚠️  Could not download yt-dlp: {e}")
        print("Building without bundled yt-dlp...")
        ytdlp_binary = None
    
    # Build command
    command = [
        "pyinstaller",
        "--onefile",
        "--name", "quicktube",
        "--console",
        "--clean",
    ]
    
    # Add ffmpeg as data file if downloaded
    if ffmpeg_binary and os.path.exists(ffmpeg_binary):
        command.extend([
            "--add-binary", f"{ffmpeg_binary}:.",
        ])
        print(f"✅ Bundling {ffmpeg_binary} with executable")
    
    # Add yt-dlp as data file if downloaded
    if ytdlp_binary and os.path.exists(ytdlp_binary):
        command.extend([
            "--add-binary", f"{ytdlp_binary}:.",
        ])
        print(f"✅ Bundling {ytdlp_binary} with executable")
    
    # Add the main script
    command.append("quicktube.py")
    
    # Run PyInstaller
    try:
        subprocess.check_call(command)
        
        # Cleanup
        if ffmpeg_binary and os.path.exists(ffmpeg_binary):
            os.remove(ffmpeg_binary)
        if ytdlp_binary and os.path.exists(ytdlp_binary):
            os.remove(ytdlp_binary)
        
        print("\n" + "=" * 60)
        print("✅ Build completed successfully!")
        print("\n🎉 Executable includes ffmpeg and yt-dlp - no separate installation needed!")
        print(f"\n📁 Executable location: dist/quicktube{'.exe' if system == 'Windows' else ''}")
        print("=" * 60)
        return True
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Build failed: {e}")
        return False

def main():
    print("=" * 60)
    print("⚡ QuickTube Executable Builder (with FFmpeg) ⚡")
    print("=" * 60)
    print(f"Platform: {platform.system()} {platform.release()}")
    print(f"Python: {sys.version.split()[0]}")
    print("=" * 60 + "\n")
    
    # Check PyInstaller
    try:
        import PyInstaller
        print("✅ PyInstaller is installed\n")
    except ImportError:
        print("❌ PyInstaller not found!")
        install = input("Install PyInstaller now? (yes/no): ").strip().lower()
        if install == "yes":
            subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
            print("✅ PyInstaller installed\n")
        else:
            print("Cannot build without PyInstaller. Exiting.")
            return
    
    # Build
    print("⚠️  This will download ffmpeg and yt-dlp (~50-100 MB)")
    proceed = input("Proceed? (yes/no): ").strip().lower()
    
    if proceed == "yes":
        success = build_with_ffmpeg()
        
        if success:
            print("\n🎉 Build complete!")
            print("\n📝 Important:")
            print("   ✅ Users do NOT need to install Python")
            print("   ✅ Users do NOT need to install yt-dlp")
            print("   ✅ Users do NOT need to install ffmpeg")
            print("   ✅ Just run the executable - everything is included!")
    else:
        print("Build cancelled.")

if __name__ == "__main__":
    main()
