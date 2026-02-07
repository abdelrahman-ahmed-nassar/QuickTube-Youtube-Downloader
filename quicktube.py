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

def probe_url_with_ytdlp(url):
    """Check if yt-dlp can extract the URL and get basic info."""
    ytdlp_cmd = get_ytdlp_path()
    try:
        import json
        # Use --dump-single-json to get metadata without downloading
        result = subprocess.run(
            [ytdlp_cmd, "--dump-single-json", "--no-warnings", "--no-check-certificate", "--no-playlist", url],
            capture_output=True,
            text=True,
            timeout=20
        )
        if result.returncode == 0:
            info = json.loads(result.stdout)
            return True, info
        return False, None
    except Exception:
        return False, None

def check_if_playlist(url):
    """Check if URL is a playlist by probing with yt-dlp."""
    ytdlp_cmd = get_ytdlp_path()
    try:
        import json
        # Probe with playlist support to detect if it's a playlist
        result = subprocess.run(
            [ytdlp_cmd, "--dump-single-json", "--no-warnings", "--no-check-certificate", "--yes-playlist", url],
            capture_output=True,
            text=True,
            timeout=20
        )
        if result.returncode == 0:
            info = json.loads(result.stdout)
            # Check if it's a playlist type or has multiple entries
            return info.get('_type') == 'playlist' or 'entries' in info
        return False
    except Exception:
        return False

def extract_video_url(playlist_url):
    """Extracts the single video URL from a playlist URL (YouTube-specific fallback)."""
    match = re.search(r"v=([a-zA-Z0-9_-]+)", playlist_url)
    if match:
        return f"https://www.youtube.com/watch?v={match.group(1)}"
    return playlist_url

def sanitize_filename(filename):
    """Remove or replace characters that cause issues on various filesystems."""
    # Characters that are problematic on Windows/macOS/Linux
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        filename = filename.replace(char, '_')
    return filename

def get_cpu_thread_count():
    """Get optimal thread count for encoding (use half of available cores to prevent overheating)"""
    try:
        import multiprocessing
        cores = multiprocessing.cpu_count()
        # Use half the cores (minimum 1, maximum 4) to prevent device overheating
        return str(max(1, min(cores // 2, 4)))
    except:
        return "2"  # Safe default

def convert_video(input_file, target_format):
    """Converts the video to the specified format using H.264 for video and AAC for audio.
    Uses resource-efficient settings to prevent device overheating."""
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
    thread_count = get_cpu_thread_count()

    # Common ffmpeg settings to reduce CPU usage and prevent overheating:
    # - ultrafast preset: fastest encoding, lowest CPU usage
    # - threads: limit CPU threads used
    # - crf 23: good quality with reasonable file size
    if target_format == "mp4":
        command = [
            ffmpeg_cmd, "-y", "-i", input_file,
            "-threads", thread_count,
            "-vcodec", "libx264", "-profile:v", "high", "-level", "4.1",
            "-acodec", "aac",
            "-preset", "ultrafast",  # Much faster, less CPU intensive
            "-crf", "23",
            "-pix_fmt", "yuv420p",
            "-movflags", "+faststart",
            "-loglevel", "error", "-stats",
            output_file
        ]
    elif target_format == "mkv":
        command = [
            ffmpeg_cmd, "-y", "-i", input_file,
            "-threads", thread_count,
            "-c:v", "libx264", "-c:a", "aac",
            "-preset", "ultrafast",  # Much faster, less CPU intensive
            "-crf", "23",
            "-pix_fmt", "yuv420p",
            "-loglevel", "error", "-stats",
            output_file
        ]
    else:
        print("❌ Unsupported format. No conversion performed.")
        return None

    print(f"🔄 Converting to {target_format.upper()} (using {thread_count} CPU threads)...")
    try:
        # Don't capture output so user can see ffmpeg progress
        result = subprocess.run(command, timeout=600)  # 10 minute timeout for larger files
        
        if result.returncode == 0:
            print(f"✅ Successfully converted to {target_format.upper()}!")
            return output_file
        else:
            print(f"❌ Conversion failed.")
            return None
    except subprocess.TimeoutExpired:
        print("❌ Conversion timeout (exceeded 10 minutes).")
        return None
    except Exception as e:
        print(f"❌ Conversion error: {str(e)}")
        return None

def remux_video(input_file, target_format):
    """Remux video to another container without re-encoding (fast, no quality loss)."""
    current_ext = os.path.splitext(input_file)[1][1:].lower()
    
    if current_ext == target_format.lower():
        print(f"⚠️  File is already in {target_format.upper()} format. No remux needed.")
        return input_file
    
    base_name = os.path.splitext(os.path.basename(input_file))[0]
    output_file = os.path.join(os.path.dirname(input_file), f"{base_name}_remuxed.{target_format}")
    
    ffmpeg_cmd = get_ffmpeg_path()
    
    # Copy streams without re-encoding - very fast, no quality loss
    command = [
        ffmpeg_cmd, "-y", "-i", input_file,
        "-c", "copy",  # Copy all streams without re-encoding
        "-movflags", "+faststart" if target_format == "mp4" else "",
        "-loglevel", "error", "-stats",
        output_file
    ]
    # Remove empty arguments
    command = [arg for arg in command if arg]
    
    print(f"🔄 Remuxing to {target_format.upper()} (no re-encoding, instant)...")
    try:
        result = subprocess.run(command, timeout=120)  # 2 minute timeout (remux is fast)
        
        if result.returncode == 0:
            print(f"✅ Successfully remuxed to {target_format.upper()}!")
            return output_file
        else:
            print(f"❌ Remux failed.")
            return None
    except subprocess.TimeoutExpired:
        print("❌ Remux timeout.")
        return None
    except Exception as e:
        print(f"❌ Remux error: {str(e)}")
        return None

def download_media(video_url, file_type, quality, is_playlist):
    """Downloads media (MP3 or MP4) based on user choices and offers conversion afterward."""
    # Determine output directory based on platform and execution context
    if getattr(sys, 'frozen', False):
        # Running as compiled executable
        if sys.platform == 'darwin':
            # macOS: For .app bundles, save to output folder next to the .app
            # sys.executable is inside QuickTube.app/Contents/MacOS/QuickTube
            # We need to go up 3 levels to get to the parent directory of the .app
            executable_path = os.path.abspath(sys.executable)
            if '.app/Contents/MacOS' in executable_path:
                # Inside an app bundle - go to parent of .app
                app_bundle = executable_path.split('.app/Contents/MacOS')[0] + '.app'
                base_dir = os.path.dirname(app_bundle)
            else:
                # Not in app bundle (shouldn't happen, but fallback)
                base_dir = os.path.dirname(executable_path)
            output_dir = os.path.join(base_dir, "output")
        else:
            # Windows/Linux: Use executable's directory
            base_dir = os.path.dirname(sys.executable)
            output_dir = os.path.join(base_dir, "output")
    else:
        # Running as script - use script's directory
        base_dir = os.path.dirname(os.path.abspath(__file__))
        output_dir = os.path.join(base_dir, "output")
    
    # Try to create output directory, handle read-only filesystem error
    try:
        os.makedirs(output_dir, exist_ok=True)
    except (OSError, PermissionError) as e:
        print("\n" + "="*60)
        print("❌ ERROR: Cannot create output folder")
        print("="*60)
        print(f"\n⚠️  Could not create folder: {output_dir}")
        print(f"\n💡 Error: {e}")
        print("\n📋 SOLUTION:")
        print("   1. Check folder permissions")
        print("   2. Try running from a different location\n")
        print("="*60 + "\n")
        input("Press Enter to exit...")
        sys.exit(1)

    # Quality is now the actual resolution/bitrate value
    audio_quality_map = {"64": "64K", "128": "128K", "192": "192K", "320": "320K"}
    video_quality_map = {"144": "144", "240": "240", "360": "360", "480": "480", "720": "720", "1080": "1080", "1440": "1440", "2160": "2160"}

    # Store the base output directory as fallback
    base_output_dir = output_dir
    
    # Try to create subdirectory based on file type
    if file_type == "mp3":
        output_dir = os.path.join(output_dir, "mp3")
    elif file_type == "mp4":
        output_dir = os.path.join(output_dir, "mp4")
    
    # Try to create the subdirectory
    try:
        os.makedirs(output_dir, exist_ok=True)
    except (OSError, PermissionError) as e:
        # Fallback to base output directory
        print(f"\n⚠️  Could not create subfolder: {output_dir}")
        print(f"    Falling back to: {base_output_dir}")
        output_dir = base_output_dir
        try:
            os.makedirs(output_dir, exist_ok=True)
        except (OSError, PermissionError) as e2:
            print("\n" + "="*60)
            print("❌ ERROR: Cannot create output folder")
            print("="*60)
            print(f"\n⚠️  Could not create folder: {output_dir}")
            print(f"\n💡 Error: {e2}")
            print("\n📋 SOLUTION:")
            print("   1. Check folder permissions")
            print("   2. Try running from a different location\n")
            print("="*60 + "\n")
            input("Press Enter to exit...")
            sys.exit(1)

    # Filename template uses YouTube video title and extension
    filename = os.path.join(output_dir, "%(title)s.%(ext)s")
    
    # Get yt-dlp path (bundled or system)
    ytdlp_cmd = get_ytdlp_path()
    thread_count = get_cpu_thread_count()
    
    # Enhanced command with:
    # - Cleaner progress bar (single line updates)
    # - Anti-blocking measures
    # - Reduced CPU usage for merging
    # - Concurrent downloads for faster speeds
    command = [
        ytdlp_cmd, "-o", filename,
        "--no-warnings",
        "--no-check-certificate",
        # Concurrent fragment downloads (faster for DASH/HLS streams)
        "--concurrent-fragments", "4",
        # Progress bar settings - use default yt-dlp progress (updates in place)
        "--progress",
        "--console-title",
        # Add user agent to avoid blocking
        "--user-agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        # Retry on failures
        "--retries", "3",
        "--fragment-retries", "3",
    ]

    if file_type == "mp3":
        bitrate = audio_quality_map.get(quality, "128K")
        command += ["-x", "--audio-format", "mp3", "--audio-quality", bitrate]
    elif file_type == "mp4":
        resolution = video_quality_map.get(quality, "720")
        # IMPROVED FORMAT SELECTION with fallback for platforms with limited formats:
        # 1. Try: best format at or below requested resolution
        # 2. Fallback: best available format if exact resolution not available
        # 3. Always prefer mp4 container when possible
        command += [
            "-f", f"best[height<={resolution}][ext=mp4]/best[height<={resolution}]/bestvideo[height<={resolution}]+bestaudio/best",
            "--merge-output-format", "mp4",
            # Use lightweight ffmpeg settings for merging to reduce CPU/heat
            "--postprocessor-args", f"ffmpeg:-threads {thread_count} -preset ultrafast -movflags +faststart"
        ]

    if not is_playlist:
        command.append("--no-playlist")

    # Use yt-dlp's --print after_move:filepath to capture the output filename (suppress this output)
    command.append(video_url)
    
    # Display quality in user-friendly format
    quality_display = f"{quality}p" if file_type == "mp4" else f"{quality} kbps"
    
    print(f"\n⏳ Downloading {file_type.upper()} ({quality_display})...")
    print("=" * 60)
    
    # Run command without capturing output to show real-time progress
    result = subprocess.run(command, capture_output=False, text=True)
    
    print("=" * 60)

    # Check if download was successful
    if result.returncode != 0:
        print(f"❌ Download failed!")
        print("\n💡 Troubleshooting tips:")
        print("   1. Update yt-dlp: pip install --upgrade yt-dlp")
        print("   2. Check if video is region-restricted")
        print("   3. Try again later (rate limiting)")
        print("   4. For age-restricted videos, make sure you're logged into Chrome")
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
        print("\n🎬 Convert to another format?")
        print("   1. Yes (full conversion - slower, may fix playback issues)")
        print("   2. Yes (quick copy - instant, same quality)")
        print("   3. No")
        convert_choice = input("Enter your choice (1-3, default: 3): ").strip().lower() or "3"
        if convert_choice in ["1", "2", "yes", "y", "full", "quick", "copy"]:
            # Determine conversion type
            if convert_choice in ["2", "quick", "copy"]:
                is_quick = True
            elif convert_choice in ["1", "full"]:
                is_quick = False
            else:  # "yes" or "y" - ask which type
                print("\n⚡ Conversion type:")
                print("   1. Full conversion (slower, may fix issues)")
                print("   2. Quick copy (instant, same quality)")
                type_choice = input("Enter your choice (1-2, default: 2): ").strip().lower() or "2"
                is_quick = type_choice in ["2", "quick", "copy"]
            
            print("\n📦 Select target format:")
            print("   1. MP4")
            print("   2. MKV")
            while True:
                format_choice = input("Enter your choice (1-2): ").strip().lower()
                if format_choice in ["1", "mp4"]:
                    target_format = "mp4"
                    break
                elif format_choice in ["2", "mkv"]:
                    target_format = "mkv"
                    break
                print("⚠️  Invalid choice! Please enter 1, 2, or type 'mp4'/'mkv'.")
            
            if is_quick:
                # Quick remux - just copy streams without re-encoding
                converted_file = remux_video(output_file, target_format)
            else:
                converted_file = convert_video(output_file, target_format)
            
            if converted_file:
                print(f"🎉 Conversion complete!")
                print(f"📁 Saved to: {converted_file}")
    
if __name__ == "__main__":
    while True:
        print("=" * 60)
        print("⚡ QuickTube - Universal Media Downloader ⚡")
        print("=" * 60)
        
        # Platform selection
        print("\n🌐 Select platform:")
        print("   1. YouTube (default)")
        print("   2. Facebook")
        print("   3. LinkedIn")
        print("   4. X (Twitter)")
        platform_choice = input("Enter your choice (1-4) or press Enter for YouTube: ").strip().lower() or "1"
        
        platform_names = {
            "1": "YouTube", "youtube": "YouTube",
            "2": "Facebook", "facebook": "Facebook", "fb": "Facebook",
            "3": "LinkedIn", "linkedin": "LinkedIn",
            "4": "X/Twitter", "x": "X/Twitter", "twitter": "X/Twitter"
        }
        platform_name = platform_names.get(platform_choice, "YouTube")
        
        url = input(f"\n📎 Enter {platform_name} URL: ").strip()
        
        # Validate URL
        if not url:
            print("⚠️  No URL entered. Please try again.")
            continue
        
        # Probe if yt-dlp supports this URL
        print("\n🔍 Checking URL...")
        is_supported, info = probe_url_with_ytdlp(url)
        
        if not is_supported:
            print(f"⚠️  Unable to extract media from this URL.")
            print("   Make sure:")
            print("   • The URL is correct and accessible")
            print("   • The video/post is public (not private)")
            print("   • yt-dlp is up to date: pip install --upgrade yt-dlp")
            continue
        
        print(f"✅ Supported! Found: {info.get('title', 'media')[:50]}...")

        # Check if the URL is a playlist
        is_playlist = check_if_playlist(url)
        if is_playlist:
            print("\n📦 This is a playlist/collection. What would you like to do?")
            print("   1. Download entire playlist")
            print("   2. Download single item only")
            choice = input("Enter your choice (1-2): ").strip().lower()
            if choice in ["2", "single", "video", "one", "item"]:
                # For YouTube playlists, try to extract single video
                if "youtube.com" in url or "youtu.be" in url:
                    url = extract_video_url(url)
                is_playlist = False

        print("\n📁 Select file type:")
        print("   1. MP3 (Audio only)")
        print("   2. MP4 (Video)")
        while True:
            choice = input("Enter your choice (1-2, default: 2): ").strip().lower() or "2"
            if choice in ["1", "mp3", "audio"]:
                file_type = "mp3"
                break
            elif choice in ["2", "mp4", "video"]:
                file_type = "mp4"
                break
            print("⚠️  Invalid choice! Please enter 1, 2, or type 'mp3'/'mp4'.")

        # Quality selection based on file type
        if file_type == "mp3":
            print("\n🔊 Select audio quality:")
            print("   1. 64 kbps")
            print("   2. 128 kbps (Recommended)")
            print("   3. 192 kbps")
            print("   4. 320 kbps (Highest)")
            while True:
                choice = input("Enter your choice (1-4, default: 2): ").strip().lower() or "2"
                if choice in ["1", "64"]:
                    quality = "64"
                    break
                elif choice in ["2", "128"]:
                    quality = "128"
                    break
                elif choice in ["3", "192"]:
                    quality = "192"
                    break
                elif choice in ["4", "320"]:
                    quality = "320"
                    break
                print("⚠️  Invalid choice! Please enter 1-4 or the bitrate (64/128/192/320).")
        else:  # mp4
            print("\n🎬 Select video resolution:")
            print("   1. 144p")
            print("   2. 240p")
            print("   3. 360p")
            print("   4. 480p")
            print("   5. 720p (HD - Recommended)")
            print("   6. 1080p (Full HD)")
            print("   7. 1440p (2K)")
            print("   8. 2160p (4K)")
            while True:
                choice = input("Enter your choice (1-8, default: 5): ").strip().lower().replace('p', '') or "5"
                if choice in ["1", "144"]:
                    quality = "144"
                    break
                elif choice in ["2", "240"]:
                    quality = "240"
                    break
                elif choice in ["3", "360"]:
                    quality = "360"
                    break
                elif choice in ["4", "480"]:
                    quality = "480"
                    break
                elif choice in ["5", "720", "hd"]:
                    quality = "720"
                    break
                elif choice in ["6", "1080", "fullhd", "full hd"]:
                    quality = "1080"
                    break
                elif choice in ["7", "1440", "2k"]:
                    quality = "1440"
                    break
                elif choice in ["8", "2160", "4k"]:
                    quality = "2160"
                    break
                print("⚠️  Invalid choice! Please enter 1-8 or resolution (144/240/360/480/720/1080/1440/2160).")

        print("\n" + "=" * 60)
        download_media(url, file_type, quality, is_playlist)
        print("=" * 60)
        
        # Ask if user wants to download another video
        print("\n🔄 Download another video?")
        print("   1. Yes")
        print("   2. No (Exit)")
        another = input("Enter your choice (1-2): ").strip()
        if another.lower() not in ["1", "yes", "y"]:
            print("\n👋 Thanks for using QuickTube!")
            print("=" * 60)
            break
        print("\n")  # Add spacing for next download
