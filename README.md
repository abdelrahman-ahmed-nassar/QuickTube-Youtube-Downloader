# YouTube Media Downloader

## Overview

This script allows users to download and convert YouTube videos and playlists into MP3 or MP4 formats. It utilizes `yt-dlp` for downloading and `ffmpeg` for conversion, ensuring high-quality media processing.

## Features

- Download YouTube videos or entire playlists
- Convert downloaded videos to MP4 or MKV format
- Supports multiple quality options for both audio and video
- Uses `yt-dlp` for reliable downloads
- Uses `ffmpeg` for high-quality media conversion

## Prerequisites

Ensure you have the following installed on your system:

- **Python** (latest version recommended)
- **yt-dlp** (`pip install yt-dlp`)
- **ffmpeg** (install via package manager or download from [ffmpeg.org](https://ffmpeg.org))

### Installing Prerequisites

**For Python:**

```sh
# Windows (using official installer)
# Download Python from: https://www.python.org/downloads/
# Run the installer and follow the setup instructions

# Windows (using winget)
winget install Python.Python.3

# macOS (using Homebrew)
brew install python

# Linux (Ubuntu/Debian)
sudo apt install python3

# Linux (Fedora)
sudo dnf install python3
```

**For yt-dlp:**

```sh
pip install yt-dlp
```

**For ffmpeg:**

- **Windows:**
  1.  Download the latest build from [gyan.dev/ffmpeg/builds/ffmpeg-git-full.7z](https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-full.7z).
  2.  Extract the archive to a folder, e.g., `C:\ffmpeg`.
  3.  Open the extracted folder and go to the `bin` directory.
  4.  You will find `ffmpeg.exe`, `ffplay.exe`, and `ffprobe.exe` inside `bin`.
  5.  Add the full path to the `bin` folder (e.g., `C:\ffmpeg\bin`) to your system PATH environment variable:
      - Open the Start menu and search for **Environment Variables**.
      - Click **Edit the system environment variables**.
      - In the System Properties window, click **Environment Variables...**
      - Under **System variables**, find and select the **Path** variable, then click **Edit**.
      - Click **New** and add the path to your ffmpeg `bin` folder (e.g., `C:\ffmpeg\bin`).
      - Click **OK** to save and close all windows.
  6.  Open a new Command Prompt and run `ffmpeg -version` to verify the installation.
- **macOS:** `brew install ffmpeg`
- **Linux (Ubuntu/Debian):** `sudo apt install ffmpeg`
- **Linux (Fedora):** `sudo dnf install ffmpeg`

To verify installation, open a terminal/command prompt and type:

```sh
python --version
yt-dlp --version
ffmpeg -version
```

## Installation

1. Clone or download the script.
2. Ensure `python`, `yt-dlp` and `ffmpeg` are installed and accessible from the command line.

> **Windows users:** For a step-by-step installation guide (including Python setup and environment variables), see the **Windows Installation Guide** section in [Detailed Installation Guide](https://github.com/abdelrahman-ahmed-nassar/YouTube-Media-Downloader-using-yt-dlp/wiki/Detailed-Installation-Guide).

## Usage

Run the script in a terminal:

```sh
python yt-dlp.py
```

### Navigating to the Script Directory

1. Open a terminal or command prompt
2. Navigate to the directory containing the script:
   ```sh
   cd path/to/script/directory
   ```
   - **Windows example:** `cd C:\Users\YourName\Downloads\YOUTUBE-MEDIA-DOWNLOADER-USING-YT-DLP`
   - **macOS/Linux example:** `cd ~/Downloads/YOUTUBE-MEDIA-DOWNLOADER-USING-YT-DLP`
3. Run the script with:
   ```sh
   python yt-dlp.py
   ```

Follow the prompts:

1. Enter the YouTube video or playlist URL.
2. Choose whether to download an entire playlist or a single video.
3. Select the file type (`mp3` or `mp4`).
4. Select the quality level (`low`, `medium`, or `high`).
5. If downloading an MP4 file, you may choose to convert it to another format.

### Example Usage

**Download a single video in MP4 format with high quality:**

```
Enter YouTube URL: https://www.youtube.com/watch?v=example
Enter file type (mp3/mp4): mp4
Enter quality (default: medium): high
```

**Download an MP3 file with medium quality:**

```
Enter YouTube URL: https://www.youtube.com/watch?v=example
Enter file type (mp3/mp4): mp3
Enter quality (default: medium): medium
```

## Output

- All downloaded media will be stored in the `output/` directory.
- Converted video files will be stored in the same directory with the chosen format.

## Notes

- If a playlist URL is provided, the script will prompt you to download the full playlist or just a single video.
- MP4 files are downloaded in the best available format up to the selected resolution.
- MP3 files are extracted with the specified bitrate.
- Conversion only applies to MP4 files and supports MP4 and MKV formats.

## License

This script is open-source and available for use and modification under the MIT License.

## Detailed Version

For advanced configuration options, troubleshooting tips, and developer documentation, please refer to the [Detailed Installation Guide](https://github.com/abdelrahman-ahmed-nassar/YouTube-Media-Downloader-using-yt-dlp/wiki/Detailed-Installation-Guide) file included with this project.

