#!/usr/bin/env python3

# Script to automate incremental backups with compression and rotation
# Author: Stivan F
# Usage: python3 backup_script.py <source_dir> <backup_dir> <max_backups>

import os
import sys
import tarfile
import logging
from datetime import datetime
from pathlib import Path
import shutil

# Configure logging
logging.basicConfig(
    filename="/var/log/backup_script.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def setup_backup_dirs(backup_dir):
    """Create backup directory if it doesn't exist."""
    try:
        Path(backup_dir).mkdir(parents=True, exist_ok=True)
        logging.info(f"Backup directory {backup_dir} ensured.")
    except Exception as e:
        logging.error(f"Failed to create backup directory: {e}")
        sys.exit(1)

def create_backup(source_dir, backup_dir, timestamp):
    """Create a compressed tar.gz backup of the source directory."""
    backup_file = Path(backup_dir) / f"backup_{timestamp}.tar.gz"
    try:
        with tarfile.open(backup_file, "w:gz") as tar:
            tar.add(source_dir, arcname=os.path.basename(source_dir))
        logging.info(f"Backup created: {backup_file}")
        return backup_file
    except Exception as e:
        logging.error(f"Backup creation failed: {e}")
        return None

def rotate_backups(backup_dir, max_backups):
    """Remove oldest backups if exceeding max_backups limit."""
    backups = sorted(Path(backup_dir).glob("backup_*.tar.gz"), key=os.path.getmtime)
    while len(backups) > max_backups:
        oldest = backups.pop(0)
        try:
            oldest.unlink()
            logging.info(f"Rotated out old backup: {oldest}")
        except Exception as e:
            logging.error(f"Failed to remove old backup {oldest}: {e}")

def main(source_dir, backup_dir, max_backups):
    """Main function to handle backup process."""
    if not Path(source_dir).exists():
        logging.error(f"Source directory {source_dir} does not exist")
        sys.exit(1)

    setup_backup_dirs(backup_dir)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Create backup
    backup_file = create_backup(source_dir, backup_dir, timestamp)
    if not backup_file:
        sys.exit(1)
    
    # Rotate backups
    rotate_backups(backup_dir, max_backups)
    
    logging.info("Backup process completed successfully")
    print(f"Backup completed: {backup_file}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 backup_script.py <source_dir> <backup_dir> <max_backups>")
        sys.exit(1)
    
    source_dir = sys.argv[1]
    backup_dir = sys.argv[2]
    try:
        max_backups = int(sys.argv[3])
        if max_backups < 1:
            raise ValueError("max_backups must be positive")
    except ValueError as e:
        logging.error(f"Invalid max_backups value: {e}")
        sys.exit(1)
    
    main(source_dir, backup_dir, max_backups)