import subprocess
import os
import re
import glob

def extract_video_url(playlist_url):
    """Extracts the single video URL from a playlist URL."""
    match = re.search(r"v=([a-zA-Z0-9_-]+)", playlist_url)
    if match:
        return f"https://www.youtube.com/watch?v={match.group(1)}"
    return playlist_url

def convert_video(input_file, target_format):
    """Converts the video to the specified format using H.264 for video and AAC for audio."""
    # Use the base name of the downloaded file for the converted output
    base_name = os.path.splitext(os.path.basename(input_file))[0]
    output_file = os.path.join(os.path.dirname(input_file), f"{base_name}.{target_format}")

    if target_format == "mp4":
        command = [
            "ffmpeg", "-i", input_file,
            "-vcodec", "libx264", "-acodec", "aac",
            "-b:v", "1000k", "-b:a", "128k",
            "-preset", "fast", "-crf", "23", "-movflags", "+faststart",
            output_file
        ]
    elif target_format == "mkv":
        command = [
            "ffmpeg", "-i", input_file,
            "-c:v", "libx264", "-c:a", "aac",
            "-b:v", "1000k", "-b:a", "128k",
            output_file
        ]
    else:
        print("❌ Unsupported format. No conversion performed.")
        return None

    print(f"🔄 Converting to {target_format.upper()}...")
    result = subprocess.run(command, capture_output=True, text=True)
    
    if result.returncode == 0:
        print(f"✅ Successfully converted to {target_format.upper()}!")
        return output_file
    else:
        print(f"❌ Conversion failed. Error: {result.stderr[:200]}")
        return None

def download_media(video_url, file_type, quality, is_playlist):
    """Downloads media (MP3 or MP4) based on user choices and offers conversion afterward."""
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    audio_quality_map = {"low": "50K", "medium": "128K", "high": "192K"}
    video_quality_map = {"low": "360", "medium": "720", "high": "1080"}

    # Filename template uses YouTube video title and extension
    filename = os.path.join(output_dir, "%(title)s.%(ext)s")
    command = ["yt-dlp", "-o", filename]

    if file_type == "mp3":
        bitrate = audio_quality_map.get(quality, "128K")
        command += ["-x", "--audio-format", "mp3", "--audio-quality", bitrate]
    elif file_type == "mp4":
        resolution = video_quality_map.get(quality, "720")
        command += [
            "-f", f"bv*[height<={resolution}]+ba/best",
            "--merge-output-format", "mp4"
        ]

    if not is_playlist:
        command.append("--no-playlist")

    # Use yt-dlp's --print after_move:filepath to capture the output filename
    command += ["--print", "after_move:filepath"]
    command.append(video_url)
    
    print(f"⏳ Downloading {file_type.upper()} ({quality.upper()} quality)...")
    result = subprocess.run(command, capture_output=True, text=True)

    # Check if download was successful
    if result.returncode != 0:
        print(f"❌ Download failed!")
        print(f"Error: {result.stderr[:300]}")
        return

    # Conversion step for video files
    if file_type == "mp4":
        # Get the actual output filename from yt-dlp's output
        output_lines = result.stdout.strip().splitlines()
        mp4_files = [line for line in output_lines if line.lower().endswith(".mp4")]
        if mp4_files:
            input_file = mp4_files[-1]  # Use the last .mp4 file printed
            print(f"✅ Successfully downloaded: {os.path.basename(input_file)}")
            print(f"📁 Saved to: {input_file}")
            
            convert_choice = input("\n🎬 Do you want to convert the file to another format? (yes/no): ").strip().lower()
            if convert_choice == "yes":
                target_format = input("Enter target format (mp4/mkv): ").strip().lower()
                output_file = convert_video(input_file, target_format)
                if output_file:
                    print(f"🎉 Conversion complete!")
                    print(f"📁 Saved to: {output_file}")
        else:
            print("❌ No MP4 file found. Conversion skipped.")
    
    elif file_type == "mp3":
        # Get the actual output filename from yt-dlp's output
        output_lines = result.stdout.strip().splitlines()
        mp3_files = [line for line in output_lines if line.lower().endswith(".mp3")]
        if mp3_files:
            full_path = mp3_files[-1]
            print(f"🎉 Successfully downloaded MP3: {os.path.basename(full_path)}")
            print(f"📁 Saved to: {full_path}")
        else:
            print("❌ No MP3 file found.")
    
if __name__ == "__main__":
    print("=" * 60)
    print("🎵 YouTube Media Downloader 🎵")
    print("=" * 60)
    
    url = input("\n📎 Enter YouTube URL: ").strip()

    # Check if the URL contains a playlist
    is_playlist = "list=" in url
    if is_playlist:
        choice = input("📦 This is a playlist. Download entire playlist? (yes/no): ").strip().lower()
        if choice != "yes":
            url = extract_video_url(url)
            is_playlist = False

    file_type = input("📁 Enter file type (mp3/mp4): ").strip().lower()
    if file_type not in ["mp3", "mp4"]:
        print("⚠️  Invalid file type! Defaulting to mp4.")
        file_type = "mp4"

    print("\n🔊 Choose quality: low, medium, high")
    quality = input("Enter quality (default: medium): ").strip().lower() or "medium"

    print("\n" + "=" * 60)
    download_media(url, file_type, quality, is_playlist)
    print("=" * 60)
