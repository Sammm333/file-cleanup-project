import argparse
import logging
import os
from pathlib import Path
from datetime import datetime, timedelta

# Configure logging
logging.basicConfig(
    filename='file_cleanup.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def cleanup_files(directory, days=30):
    try:
        # Check if directory exists
        if not os.path.isdir(directory):
            raise ValueError(f"Directory {directory} does not exist")

        # Calculate cutoff date
        cutoff_date = datetime.now() - timedelta(days=days)
        logging.info(f"Starting cleanup of files in {directory}, older than {days} days")
        print(f"Starting cleanup in {directory}")

        # Scan directory
        for file_path in Path(directory).glob('*'):
            if file_path.is_file():
                # Get file modification time
                mtime = datetime.fromtimestamp(file_path.stat().st_mtime)
                if mtime < cutoff_date:
                    try:
                        file_path.unlink()
                        logging.info(f"Deleted file: {file_path}")
                        print(f"Deleted file: {file_path}")
                    except Exception as e:
                        logging.error(f"Error deleting {file_path}: {str(e)}")
                        print(f"Error deleting {file_path}: {str(e)}")

        logging.info("Cleanup completed")
        print("Cleanup completed")

    except Exception as e:
        logging.error(f"Error during cleanup of {directory}: {str(e)}")
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Delete files older than specified days")
    parser.add_argument(
        "--dir", default="/tmp", help="Directory to clean (default: /tmp)"
    )
    parser.add_argument(
        "--days", type=int, default=30, help="Delete files older than N days (default: 30)"
    )
    args = parser.parse_args()

    cleanup_files(args.dir, args.days)