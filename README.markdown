# File Cleanup Script

A Python script to delete files older than a specified number of days (default: 30) in a directory, packaged in a Docker container and scheduled with `cron`. Logs actions to `file_cleanup.log`.

## Features
- Deletes files older than a specified age (e.g., 30 days).
- Logs actions and errors to `file_cleanup.log`.
- Runs in a Docker container for portability.
- Scheduled via `cron` for automation.

## Tech Stack
- Python (`pathlib`, `logging`, `argparse`)
- Docker
- Cron

## Prerequisites
- Python 3.9+ (for local testing)
- Docker Desktop (for Mac)
- `cron` (available on macOS)

## Setup
1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd file-cleanup-project
   ```
2. **Build Docker Image**:
   ```bash
   docker build -t file-cleanup .
   ```
3. **Create a Test Directory**:
   ```bash
   mkdir -p ~/test
   ```

## Usage
- **Run Locally**:
   ```bash
   python3 file_cleanup.py --dir ~/test --days 30
   ```
   - `--dir`: Directory to clean (default: `/tmp`).
   - `--days`: Delete files older than N days (default: 30).
- **Run in Docker**:
   ```bash
   docker run --rm -v ~/test:/tmp file-cleanup
   ```
   - Mounts `~/test` to the container’s `/tmp`.
   - Logs saved to `file_cleanup.log` in the project directory.
- **Check Logs**:
   ```bash
   cat file_cleanup.log
   ```

## Schedule with Cron
1. Edit `crontab`:
   ```bash
   crontab -e
   ```
2. Add (runs daily at midnight):
   ```bash
   0 0 * * * docker run --rm -v /Users/samvelkhachatryan/test:/tmp file-cleanup
   ```
3. Test manually:
   ```bash
   docker run --rm -v /Users/samvelkhachatryan/test:/tmp file-cleanup
   ```

## Testing
1. Create test files:
   ```bash
   touch ~/test/testfile1.txt
   touch -t 202506010000 ~/test/oldfile.txt
   ```
2. Run the container:
   ```bash
   docker run --rm -v ~/test:/tmp file-cleanup
   ```
3. Verify `oldfile.txt` is deleted and check `file_cleanup.log`.

## Notes
- Use `~/test` to avoid macOS permission issues with `/tmp`. To use `/tmp`, add it to Docker Desktop > Settings > Resources > File Sharing.
- Future enhancements: Add Telegram notifications or multi-directory support.
