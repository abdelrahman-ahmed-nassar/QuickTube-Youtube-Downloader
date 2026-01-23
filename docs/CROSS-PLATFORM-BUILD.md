# Cross-Platform Build Guide

## Building Executables for All Platforms

As a Mac user, you have three options to create executables for Windows and Linux:

---

## Option 1: GitHub Actions (RECOMMENDED - Easiest)

GitHub Actions automatically builds executables for all platforms in the cloud.

### Setup Steps:

1. **Push your code to GitHub** (if not already done):

   ```sh
   git add .
   git commit -m "Add build automation"
   git push origin main
   ```

2. **Create a new release on GitHub:**
   - Go to your repository on GitHub
   - Click "Releases" → "Create a new release"
   - Create a new tag (e.g., `v1.0.0`)
   - Fill in release title and description
   - Click "Publish release"

3. **GitHub Actions will automatically:**
   - Build executables for Windows, macOS, and Linux
   - Upload them to the release page
   - Takes about 5-10 minutes

4. **Download the executables:**
   - Go to the release page
   - All three executables will be attached:
     - `yt-downloader-windows.exe`
     - `yt-downloader-macos`
     - `yt-downloader-linux`

### Manual Trigger (Without Creating Release):

You can also manually trigger builds:

1. Go to your repository on GitHub
2. Click "Actions" tab
3. Click "Build Executables" workflow
4. Click "Run workflow" dropdown
5. Click "Run workflow" button
6. Download artifacts from the workflow run

**Pros:**

- ✅ No need for Windows/Linux machines
- ✅ Fully automated
- ✅ Free for public repositories
- ✅ Consistent build environment

**Cons:**

- ❌ Requires GitHub repository

---

## Option 2: Docker (Advanced)

Use Docker to build Linux and Windows executables from your Mac.

### For Linux Executable:

```sh
# Install Docker Desktop for Mac (if not installed)
# Download from: https://www.docker.com/products/docker-desktop

# Create a Docker build script
docker run --rm -v "$(pwd):/src" python:3.11-slim bash -c "
  cd /src && \
  pip install pyinstaller yt-dlp && \
  pyinstaller --onefile --name yt-downloader-linux quicktube.py
"

# Output will be in dist/yt-downloader-linux
```

### For Windows Executable:

```sh
# Use Wine to run Windows PyInstaller
docker run --rm -v "$(pwd):/src" tobix/pywine:3.11 bash -c "
  cd /src && \
  pip install pyinstaller yt-dlp && \
  pyinstaller --onefile --name yt-downloader-windows quicktube.py
"

# Output will be in dist/yt-downloader-windows.exe
```

**Pros:**

- ✅ Build from Mac without extra machines
- ✅ No GitHub required

**Cons:**

- ❌ Requires Docker installation
- ❌ More complex setup
- ❌ Windows builds via Wine may have issues

---

## Option 3: Virtual Machines or Cloud Services

Use virtual machines or cloud computers to build on actual Windows/Linux.

### Using VirtualBox/VMware:

1. Install VirtualBox or VMware on your Mac
2. Create Windows and Linux virtual machines
3. Install Python, PyInstaller, and dependencies in each VM
4. Clone your repository in each VM
5. Run `python build-executable.py` in each VM
6. Transfer executables back to Mac

### Using Cloud Services:

**AWS EC2 / Azure / Google Cloud:**

1. Launch Windows and Linux instances
2. Connect via RDP (Windows) or SSH (Linux)
3. Install dependencies and build
4. Download executables

**GitHub Codespaces:**

1. Open your repo in Codespaces
2. Run build commands in the cloud environment
3. Download built executables

**Pros:**

- ✅ Native builds (most reliable)
- ✅ Full control

**Cons:**

- ❌ Requires VM setup or cloud costs
- ❌ More time-consuming
- ❌ Manual process each time

---

## Option 4: Ask Community Members

If you have Windows/Linux users in your community:

1. Share the `build-executable.py` script
2. Ask them to run it on their platform
3. They send you the built executable

---

## Recommended Workflow

**For initial release:**

1. Use **Option 1 (GitHub Actions)** - easiest and free
2. Test executables on each platform (ask friends/community)
3. If issues arise, use Option 2 or 3 for debugging

**For regular releases:**

1. Push changes to GitHub
2. Create a new release with a version tag
3. GitHub Actions automatically builds and uploads executables
4. Done! ✅

---

## Testing Cross-Platform Builds

After building, test on each platform:

### Windows Testing (from Mac):

- Use Windows VM in VirtualBox/Parallels
- Or ask a Windows user to test
- Or use [BrowserStack](https://www.browserstack.com/) (paid)

### Linux Testing (from Mac):

- Use Docker: `docker run -it -v $(pwd):/app ubuntu bash`
- Or use Linux VM
- Or use GitHub Codespaces (free for public repos)

---

## Quick Start: GitHub Actions Setup

1. **Ensure `.github/workflows/build-executables.yml` exists** (already created)

2. **Commit and push:**

   ```sh
   git add .github/workflows/build-executables.yml
   git commit -m "Add GitHub Actions build workflow"
   git push origin main
   ```

3. **Create a release:**

   ```sh
   git tag v1.0.0
   git push origin v1.0.0
   ```

   Then go to GitHub → Releases → Draft a new release

4. **Wait 5-10 minutes** for builds to complete

5. **Download executables** from the release page!

---

## File Sizes (Approximate)

- **Windows:** 15-25 MB
- **macOS:** 15-20 MB
- **Linux:** 15-20 MB

---

## Troubleshooting

### GitHub Actions Fails

Check the Actions tab for error logs:

1. Go to repository → Actions tab
2. Click on the failed workflow
3. Click on the failed job
4. Read the error messages

### Executables Don't Work

- Ensure ffmpeg is installed on user's machine
- Check antivirus isn't blocking (Windows)
- Check execution permissions (macOS/Linux)
- Test with `--debug` flag in PyInstaller

---

## Need Help?

- GitHub Actions Documentation: https://docs.github.com/actions
- PyInstaller Documentation: https://pyinstaller.org/
- Docker Documentation: https://docs.docker.com/
