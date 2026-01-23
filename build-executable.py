#!/usr/bin/env python3
"""
Build script for creating standalone executables for yt-downloader
Supports Windows, macOS, and Linux
"""

import subprocess
import sys
import platform
import os

def check_pyinstaller():
    """Check if PyInstaller is installed"""
    try:
        import PyInstaller
        return True
    except ImportError:
        return False

def install_pyinstaller():
    """Install PyInstaller"""
    print("📦 Installing PyInstaller...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
    print("✅ PyInstaller installed successfully!\n")

def build_executable():
    """Build the executable using PyInstaller"""
    system = platform.system()
    print(f"🔨 Building executable for {system}...")
    print("=" * 60)
    
    # Base PyInstaller command
    command = [
        "pyinstaller",
        "--onefile",  # Single executable file
        "--name", "yt-downloader",  # Output name
        "--console",  # Console application
        "--clean",  # Clean PyInstaller cache
    ]
    
    # Platform-specific options
    if system == "Windows":
        # Add icon for Windows (if exists)
        if os.path.exists("icon.ico"):
            command.extend(["--icon", "icon.ico"])
    elif system == "Darwin":  # macOS
        # Add icon for macOS (if exists)
        if os.path.exists("icon.icns"):
            command.extend(["--icon", "icon.icns"])
    
    # Add the main script
    command.append("quicktube.py")
    
    # Run PyInstaller
    try:
        subprocess.check_call(command)
        print("\n" + "=" * 60)
        print("✅ Build completed successfully!")
        print(f"\n📁 Executable location:")
        
        if system == "Windows":
            print(f"   dist/yt-downloader.exe")
            print(f"\n💡 To run: dist\\yt-downloader.exe")
        else:
            print(f"   dist/yt-downloader")
            print(f"\n💡 To run: ./dist/yt-downloader")
        
        print("\n📦 You can distribute the file in the 'dist' folder")
        print("=" * 60)
        return True
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Build failed: {e}")
        return False

def main():
    print("=" * 60)
    print("⚡ QuickTube Executable Builder ⚡")
    print("=" * 60)
    print(f"Platform: {platform.system()} {platform.release()}")
    print(f"Python: {sys.version.split()[0]}")
    print("=" * 60 + "\n")
    
    # Check and install PyInstaller if needed
    if not check_pyinstaller():
        print("⚠️  PyInstaller not found!")
        install = input("Install PyInstaller now? (yes/no): ").strip().lower()
        if install == "yes":
            install_pyinstaller()
        else:
            print("❌ Cannot build without PyInstaller. Exiting.")
            return
    else:
        print("✅ PyInstaller is installed\n")
    
    # Build the executable
    success = build_executable()
    
    if success:
        print("\n🎉 Build process complete!")
        print("\n📝 Next steps:")
        print("   1. Test the executable in the 'dist' folder")
        print("   2. Distribute the executable to users")
        print("   3. No Python installation required for users!")
    else:
        print("\n❌ Build failed. Please check the error messages above.")

if __name__ == "__main__":
    main()
