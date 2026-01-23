import subprocess
import os
import re
import sys

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

def get_ytdlp_path():
    """Get the path to yt-dlp binary (bundled or system)"""
    if getattr(sys, 'frozen', False):
        # Running as compiled executable
        base_path = sys._MEIPASS
        ytdlp_name = "yt-dlp.exe" if os.name == 'nt' else "yt-dlp"
        bundled_ytdlp = os.path.join(base_path, ytdlp_name)
        if os.path.exists(bundled_ytdlp):
            return bundled_ytdlp
    # Fall back to system yt-dlp
    return "yt-dlp"

def extract_video_url(playlist_url):
    """Extracts the single video URL from a playlist URL."""
    match = re.search(r"v=([a-zA-Z0-9_-]+)", playlist_url)
    if match:
        return f"https://www.youtube.com/watch?v={match.group(1)}"
    return playlist_url

def convert_video(input_file, target_format):
    """Converts the video to the specified format using H.264 for video and AAC for audio."""
    # Get the current file extension
    current_ext = os.path.splitext(input_file)[1][1:].lower()
    
    # Check if trying to convert to the same format
    if current_ext == target_format.lower():
        print(f"⚠️  File is already in {target_format.upper()} format. No conversion needed.")
        return input_file
    
    # Use the base name of the downloaded file for the converted output
    base_name = os.path.splitext(os.path.basename(input_file))[0]
    output_file = os.path.join(os.path.dirname(input_file), f"{base_name}_converted.{target_format}")

    # Get ffmpeg path (bundled or system)
    ffmpeg_cmd = get_ffmpeg_path()

    if target_format == "mp4":
        command = [
            ffmpeg_cmd, "-y", "-i", input_file,
            "-vcodec", "libx264", "-profile:v", "high", "-level", "4.1",
            "-acodec", "aac", "-strict", "experimental",
            "-b:v", "1000k", "-b:a", "128k",
            "-preset", "fast", "-crf", "23",
            "-pix_fmt", "yuv420p",
            "-movflags", "+faststart",
            "-loglevel", "error", "-stats",
            output_file
        ]
    elif target_format == "mkv":
        command = [
            ffmpeg_cmd, "-y", "-i", input_file,
            "-c:v", "libx264", "-c:a", "aac",
            "-b:v", "1000k", "-b:a", "128k",
            "-pix_fmt", "yuv420p",
            "-loglevel", "error", "-stats",
            output_file
        ]
    else:
        print("❌ Unsupported format. No conversion performed.")
        return None

    print(f"🔄 Converting to {target_format.upper()}...")
    try:
        # Don't capture output so user can see ffmpeg progress
        result = subprocess.run(command, timeout=300)  # 5 minute timeout
        
        if result.returncode == 0:
            print(f"✅ Successfully converted to {target_format.upper()}!")
            return output_file
        else:
            print(f"❌ Conversion failed.")
            return None
    except subprocess.TimeoutExpired:
        print("❌ Conversion timeout (exceeded 5 minutes).")
        return None
    except Exception as e:
        print(f"❌ Conversion error: {str(e)}")
        return None

def download_media(video_url, file_type, quality, is_playlist):
    """Downloads media (MP3 or MP4) based on user choices and offers conversion afterward."""
    # Get the directory where the executable/script is located
    if getattr(sys, 'frozen', False):
        # Running as compiled executable - use executable's directory
        base_dir = os.path.dirname(sys.executable)
    else:
        # Running as script - use script's directory
        base_dir = os.path.dirname(os.path.abspath(__file__))
    
    output_dir = os.path.join(base_dir, "output")
    
    # Try to create output directory, handle read-only filesystem error
    try:
        os.makedirs(output_dir, exist_ok=True)
    except (OSError, PermissionError) as e:
        print("\n" + "="*60)
        print("❌ ERROR: Cannot create output folder in current location")
        print("="*60)
        print("\n⚠️  The app is in a read-only location (likely macOS security).")
        print("\n📋 SOLUTION:")
        print("   1. Move QuickTube.app to your Documents or Desktop folder")
        print("   2. Run it from there instead")
        print("\n💡 Why? macOS puts downloaded apps in a temporary read-only")
        print("   location for security. Moving the app fixes this.\n")
        print("="*60 + "\n")
        input("Press Enter to exit...")
        sys.exit(1)

    audio_quality_map = {"low": "50K", "medium": "128K", "high": "192K"}
    video_quality_map = {"low": "360", "medium": "720", "high": "1080"}

    # Filename template uses YouTube video title and extension
    filename = os.path.join(output_dir, "%(title)s.%(ext)s")
    
    # Get yt-dlp path (bundled or system)
    ytdlp_cmd = get_ytdlp_path()
    
    command = [ytdlp_cmd, "-o", filename, "--no-warnings", "--no-check-certificate", "--progress", "--newline"]

    if file_type == "mp3":
        bitrate = audio_quality_map.get(quality, "128K")
        command += ["-x", "--audio-format", "mp3", "--audio-quality", bitrate]
    elif file_type == "mp4":
        resolution = video_quality_map.get(quality, "720")
        command += [
            "-f", f"bv*[height<={resolution}]+ba/best",
            "--merge-output-format", "mp4",
            "--postprocessor-args", "ffmpeg:-movflags +faststart -vcodec libx264 -acodec aac -pix_fmt yuv420p"
        ]

    if not is_playlist:
        command.append("--no-playlist")

    # Use yt-dlp's --print after_move:filepath to capture the output filename (suppress this output)
    command.append(video_url)
    
    print(f"⏳ Downloading {file_type.upper()} ({quality.upper()} quality)...")
    print("=" * 60)
    
    # Run command without capturing output to show real-time progress
    result = subprocess.run(command, capture_output=False, text=True)
    
    print("=" * 60)

    # Check if download was successful
    if result.returncode != 0:
        print(f"❌ Download failed!")
        return

    # Find the downloaded file in the output directory
    output_files = []
    for file in os.listdir(output_dir):
        if file.lower().endswith(f".{file_type}"):
            output_files.append(os.path.join(output_dir, file))
    
    if not output_files:
        print(f"❌ No {file_type.upper()} file found.")
        return
    
    # Get the most recently created file
    output_file = max(output_files, key=os.path.getctime)
    
    print(f"🎉 Successfully downloaded {file_type.upper()}: {os.path.basename(output_file)}")
    print(f"📁 Saved to: {output_file}")
    
    # Conversion step for video files only
    if file_type == "mp4":
        convert_choice = input("\n🎬 Do you want to convert the file to another format? (yes/no): ").strip().lower()
        if convert_choice == "yes":
            while True:
                target_format = input("Enter target format (mp4/mkv): ").strip().lower()
                if target_format in ["mp4", "mkv"]:
                    break
                print("⚠️  Invalid format! Please enter 'mp4' or 'mkv'.")
            converted_file = convert_video(output_file, target_format)
            if converted_file:
                print(f"🎉 Conversion complete!")
                print(f"📁 Saved to: {converted_file}")
    
if __name__ == "__main__":
    while True:
        print("=" * 60)
        print("⚡ QuickTube - Fast YouTube Downloader ⚡")
        print("=" * 60)
        
        url = input("\n📎 Enter YouTube URL: ").strip()

        # Check if the URL contains a playlist
        is_playlist = "list=" in url
        if is_playlist:
            choice = input("📦 This is a playlist. Download entire playlist? (yes/no): ").strip().lower()
            if choice != "yes":
                url = extract_video_url(url)
                is_playlist = False

        while True:
            file_type = input("📁 Enter file type (mp3/mp4): ").strip().lower()
            if file_type in ["mp3", "mp4"]:
                break
            print("⚠️  Invalid file type! Please enter 'mp3' or 'mp4'.")

        print("\n🔊 Choose quality: low, medium, high")
        quality = input("Enter quality (default: medium): ").strip().lower() or "medium"
        if quality not in ["low", "medium", "high"]:
            print("⚠️  Invalid quality! Defaulting to medium.")
            quality = "medium"

        print("\n" + "=" * 60)
        download_media(url, file_type, quality, is_playlist)
        print("=" * 60)
        
        # Ask if user wants to download another video
        print("\n🔄 Download another video?")
        another = input("Enter 'yes' to continue or press Enter to exit: ").strip().lower()
        if another != "yes":
            print("\n👋 Thanks for using QuickTube!")
            print("=" * 60)
            break
        print("\n")  # Add spacing for next download
