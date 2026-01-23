# YouTube Media Downloader

## Comprehensive User Guide

## Table of Contents

- [YouTube Media Downloader](#youtube-media-downloader)
  - [Comprehensive User Guide](#comprehensive-user-guide)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Features](#features)
  - [Prerequisites](#prerequisites)
    - [System Requirements](#system-requirements)
    - [Required Software](#required-software)
  - [Installation Guide](#installation-guide)
    - [Windows Installation](#windows-installation)
      - [1. Install Python](#1-install-python)
      - [2. Add Python to Environment Variables (if not already added)](#2-add-python-to-environment-variables-if-not-already-added)
      - [3. Install yt-dlp](#3-install-yt-dlp)
      - [4. Install ffmpeg](#4-install-ffmpeg)
      - [5. Get the Script](#5-get-the-script)
    - [macOS Installation](#macos-installation)
    - [Linux Installation](#linux-installation)
  - [Usage Instructions](#usage-instructions)
    - [Basic Usage](#basic-usage)
    - [Advanced Options](#advanced-options)
  - [Step-by-Step Examples](#step-by-step-examples)
    - [Example 1: Download a Single Video as MP4](#example-1-download-a-single-video-as-mp4)
    - [Example 2: Download Audio Only (MP3)](#example-2-download-audio-only-mp3)
    - [Example 3: Download a Playlist](#example-3-download-a-playlist)
    - [Example 4: Convert Video Format](#example-4-convert-video-format)
  - [Quality Settings](#quality-settings)
    - [MP3 Quality Settings](#mp3-quality-settings)
    - [MP4 Quality Settings](#mp4-quality-settings)
  - [Troubleshooting](#troubleshooting)
    - [Common Issues and Solutions](#common-issues-and-solutions)
  - [FAQ](#faq)
  - [License](#license)

## Overview

The YouTube Media Downloader is a powerful Python script that allows you to download YouTube videos and playlists in various formats and quality levels. The tool leverages the capabilities of `yt-dlp` for reliable downloads and `ffmpeg` for high-quality media conversion, providing a seamless experience for obtaining media content from YouTube.

## Features

- **Flexible Download Options**: Download individual videos or entire playlists
- **Multiple Format Support**: Convert videos to MP3, MP4, or MKV formats
- **Quality Control**: Choose from low, medium, or high quality settings
- **Playlist Management**: Select specific videos from playlists or download the entire collection
- **Format Conversion**: Convert between video formats using ffmpeg
- **Organized Output**: All downloaded media is stored in a dedicated output directory
- **User-Friendly Interface**: Simple command-line prompts guide you through the process

## Prerequisites

### System Requirements

- 64-bit operating system (Windows 10/11, macOS 10.15+, or Linux)
- Minimum 4GB RAM
- At least 1GB free disk space (more recommended for storing downloads)
- Active internet connection

### Required Software

1. **Python 3.6+**

   - Required to run the script
   - Latest version recommended for optimal performance

2. **yt-dlp**

   - Core component for downloading YouTube content
   - Regularly updated to handle YouTube's changing protocols

3. **ffmpeg**
   - Required for media conversion and processing
   - Handles audio extraction and video format conversion

## Installation Guide

### Windows Installation

#### 1. Install Python

1. Download Python from the official website: https://www.python.org/downloads/windows/
2. Run the installer. **Important:** On the first screen, check the box that says **"Add Python to PATH"** before clicking "Install Now".
3. Complete the installation.

To verify Python is installed and added to PATH, open Command Prompt and run:

```sh
python --version
```

You should see the installed Python version.

#### 2. Add Python to Environment Variables (if not already added)

If you forgot to check "Add Python to PATH" during installation:

1.  Open the Start menu and search for **Environment Variables**.
2.  Click **Edit the system environment variables**.
3.  In the System Properties window, click **Environment Variables...**
4.  Under **System variables**, find and select the **Path** variable, then click **Edit**.

5.  Click **New** and add the path to your Python installation. For most users, add these two lines (replace <YourUsername> with your actual Windows username):

C:\Users\<YourUsername>\AppData\Local\Programs\Python\Python313\
 C:\Users\<YourUsername>\AppData\Local\Programs\Python\Python313\Scripts\

    > **Important:** Replace `YourName` with your actual Windows username (do not use `JohnDoe` or `YourName` literally). For example, if your username is `JohnDoe`, the path should be:
    >
    >     C:\Users\JohnDoe\AppData\Local\Programs\Python\Python313\
    >     C:\Users\JohnDoe\AppData\Local\Programs\Python\Python313\Scripts\

    If you are unsure of your username, you can check it by opening Command Prompt and running:

    ```sh
    echo %USERNAME%
    ```

    Also add the `Scripts` folder as shown above.

6.  Click **OK** to save and close all windows.
7.  Restart Command Prompt and verify with `python --version` and `pip --version`.

#### 3. Install yt-dlp

Open Command Prompt and run:

```sh
pip install yt-dlp
```

If you get a 'pip not found' error, try:

```sh
python -m pip install yt-dlp
```

#### 4. Install ffmpeg

1. Download the latest ffmpeg build from [ffmpeg.org](https://ffmpeg.org/download.html)
2. Extract the ZIP file to a folder (e.g., `C:\ffmpeg`)
3. Add ffmpeg to PATH:
   - Search for "Environment Variables" in Windows search
   - Click "Edit the system environment variables"
   - Click "Environment Variables"
   - Under "System variables", find "Path" and click "Edit"
   - Click "New" and add the path to the ffmpeg bin folder (e.g., `C:\ffmpeg\bin`)
   - Click "OK" to close all dialogs
4. Verify installation: `ffmpeg -version`

#### 5. Get the Script

Download the script from the repository or copy it from a shared location. Save it as `youtube_downloader.py` in a directory of your choice.

### macOS Installation

1. **Install Python**:

   - Download the latest Python installer from [python.org](https://www.python.org/downloads/)
   - Follow the installation instructions
   - Verify installation: `python3 --version`

2. **Install Homebrew** (if not already installed):

   - Open Terminal
   - Run: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`

3. **Install yt-dlp and ffmpeg**:

   - Run: `brew install yt-dlp ffmpeg`
   - Verify installations:
     - `yt-dlp --version`
     - `ffmpeg -version`

4. **Get the Script**:
   - Download the script from the repository or copy it from a shared location
   - Save it as `youtube_downloader.py` in a directory of your choice

### Linux Installation

1. **Install Python and pip**:

   - Debian/Ubuntu: `sudo apt update && sudo apt install python3 python3-pip`
   - Fedora: `sudo dnf install python3 python3-pip`
   - Arch: `sudo pacman -S python python-pip`

2. **Install yt-dlp**:

   - Run: `pip3 install yt-dlp`
   - Verify installation: `yt-dlp --version`

3. **Install ffmpeg**:

   - Debian/Ubuntu: `sudo apt install ffmpeg`
   - Fedora: `sudo dnf install ffmpeg`
   - Arch: `sudo pacman -S ffmpeg`
   - Verify installation: `ffmpeg -version`

4. **Get the Script**:
   - Download the script from the repository or copy it from a shared location
   - Save it as `youtube_downloader.py` in a directory of your choice

## Usage Instructions

### Basic Usage

1. **Open Terminal or Command Prompt**:

   - Navigate to the directory containing the script
   - Example: `cd /path/to/script` (Linux/macOS) or `cd C:\path\to\script` (Windows)

2. **Run the Script**:

   - Windows: `python youtube_downloader.py`
   - macOS/Linux: `python3 youtube_downloader.py`

3. **Follow the Interactive Prompts**:

   - Enter the YouTube URL when prompted
   - Choose between downloading a single video or an entire playlist
   - Select the desired file type (MP3 or MP4)
   - Choose the quality level (low, medium, or high)
   - For MP4 files, decide whether to convert to another format

4. **Wait for Download**:
   - The script will display progress information
   - Downloaded files will be saved to the `output/` directory

### Advanced Options

The script supports additional features that can be accessed through the interactive prompts:

- **Playlist Management**: When a playlist URL is entered, you can choose to download the entire playlist or select specific videos
- **Format Conversion**: After downloading an MP4 file, you can convert it to another format like MKV
- **Quality Settings**: Customize the quality of your downloads based on your needs and storage capacity

## Step-by-Step Examples

### Example 1: Download a Single Video as MP4

1. Run the script:

   ```
   python youtube_downloader.py
   ```

2. Enter the URL of the video:

   ```
   Enter YouTube URL: https://www.youtube.com/watch?v=example
   ```

3. If the URL is a playlist, you'll be asked if you want to download the entire playlist:

   ```
   This appears to be a playlist. Do you want to download the entire playlist? (y/n): n
   ```

4. Choose the file type:

   ```
   Enter file type (mp3/mp4): mp4
   ```

5. Select the quality:

   ```
   Enter quality (low/medium/high) [default: medium]: high
   ```

6. Decide if you want to convert the video:

   ```
   Do you want to convert the video to another format? (y/n): n
   ```

7. The script will download the video and save it to the `output/` directory.
   ```
   Downloading video...
   [info] Downloading video 1 of 1
   [download] 100% of 50.25MiB
   Download complete! File saved to: output/Video_Title.mp4
   ```

### Example 2: Download Audio Only (MP3)

1. Run the script:

   ```
   python youtube_downloader.py
   ```

2. Enter the URL of the video:

   ```
   Enter YouTube URL: https://www.youtube.com/watch?v=example
   ```

3. Choose MP3 as the file type:

   ```
   Enter file type (mp3/mp4): mp3
   ```

4. Select the quality:

   ```
   Enter quality (low/medium/high) [default: medium]: medium
   ```

5. The script will extract the audio and save it as an MP3 file:
   ```
   Extracting audio...
   [info] Downloading audio 1 of 1
   [download] 100% of 7.38MiB
   Audio extraction complete! File saved to: output/Audio_Title.mp3
   ```

### Example 3: Download a Playlist

1. Run the script:

   ```
   python youtube_downloader.py
   ```

2. Enter the URL of the playlist:

   ```
   Enter YouTube URL: https://www.youtube.com/playlist?list=example
   ```

3. Choose to download the entire playlist:

   ```
   This appears to be a playlist. Do you want to download the entire playlist? (y/n): y
   ```

4. Choose the file type:

   ```
   Enter file type (mp3/mp4): mp4
   ```

5. Select the quality:

   ```
   Enter quality (low/medium/high) [default: medium]: medium
   ```

6. The script will download all videos in the playlist:
   ```
   Downloading playlist...
   [info] Downloading video 1 of 15
   [download] 100% of 42.57MiB
   [info] Downloading video 2 of 15
   [download] 100% of 38.12MiB
   ...
   Download complete! All videos saved to: output/
   ```

### Example 4: Convert Video Format

1. Follow steps 1-5 from Example 1 to download an MP4 video.

2. When asked about conversion, choose yes:

   ```
   Do you want to convert the video to another format? (y/n): y
   ```

3. Select the output format:

   ```
   Enter the output format (mp4/mkv): mkv
   ```

4. The script will convert the video:
   ```
   Converting video format...
   Conversion complete! File saved to: output/Video_Title.mkv
   ```

## Quality Settings

The script offers three quality levels that affect both audio and video downloads:

### MP3 Quality Settings

- **Low**: 128 kbps bitrate
- **Medium**: 192 kbps bitrate
- **High**: 320 kbps bitrate

### MP4 Quality Settings

- **Low**: Up to 480p resolution
- **Medium**: Up to 720p resolution
- **High**: Up to 1080p resolution

## Troubleshooting

### Common Issues and Solutions

1. **"Command not found" Error**

   - **Problem**: Python, yt-dlp, or ffmpeg is not in your system PATH
   - **Solution**: Ensure all dependencies are properly installed and added to PATH

2. **Download Fails with HTTP Error**

   - **Problem**: Network issues or YouTube restrictions
   - **Solution**:
     - Check your internet connection
     - Try again later
     - Update yt-dlp (`pip install -U yt-dlp`)

3. **Conversion Fails**

   - **Problem**: ffmpeg issues or incompatible formats
   - **Solution**:
     - Ensure ffmpeg is properly installed
     - Check if the selected output format is supported

4. **Script Crashes During Download**

   - **Problem**: Memory issues or corrupted download
   - **Solution**:
     - Try downloading at a lower quality
     - Free up system resources
     - Restart your computer

5. **"URL not supported" Error**
   - **Problem**: The URL is invalid or not supported
   - **Solution**:
     - Check if the URL is correct
     - Ensure the video is publicly available
     - Try a different video

## FAQ

**Q: Can I download age-restricted videos?**
A: Yes, but you may need to update yt-dlp to the latest version as YouTube frequently changes its restrictions.

**Q: Is there a limit to how many videos I can download?**
A: There's no limit imposed by the script, but be mindful of your storage space and YouTube's terms of service.

**Q: Does this work for private or unlisted videos?**
A: It works for unlisted videos if you have the link. Private videos cannot be accessed without proper authentication.

**Q: Can I download videos from other platforms besides YouTube?**
A: The script is optimized for YouTube, but yt-dlp supports many other platforms. Results may vary.

**Q: Is downloading YouTube videos legal?**
A: Laws vary by country. Downloading copyrighted content without permission is generally against YouTube's terms of service. This tool is intended for downloading content you have the right to download.

**Q: How can I update the script?**
A: Download the latest version from the repository. To update dependencies:

- yt-dlp: `pip install -U yt-dlp`
- ffmpeg: Reinstall following the installation instructions

**Q: Where are my downloaded files stored?**
A: All downloaded files are stored in the `output/` directory in the same folder as the script. If this directory doesn't exist, it will be created automatically.

## License

This script is open-source and available under the MIT License, which allows for:

- Commercial use
- Modification
- Distribution
- Private use

The full license text can be found in the LICENSE file accompanying the script.

---

**Disclaimer**: This tool is provided for educational and personal use only. Users are responsible for complying with YouTube's terms of service and applicable copyright laws.