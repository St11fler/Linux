# System Administration Scripts

This repository contains a collection of scripts designed for Linux system administration, showcasing proficiency in Bash and Python for monitoring, log analysis, and backup automation. These projects were developed to demonstrate practical skills in managing Linux servers (Ubuntu, CentOS) and automating system tasks.

## Table of Contents
- [Projects](#projects)
  - [Server Resource Monitoring](#server-resource-monitoring)
  - [Log File Analyzer](#log-file-analyzer)
  - [Automated Backup with Compression and Rotation](#automated-backup-with-compression-and-rotation)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)
- [Contact](#contact)

## Projects

### Server Resource Monitoring
- **File**: `server_monitor.sh`
- **Description**: A Bash script that monitors CPU, memory, and disk usage on Linux servers, sending email alerts when predefined thresholds are exceeded.
- **Features**:
  - Configurable thresholds for CPU, memory, and disk usage.
  - Email notifications for high resource usage.
  - Logging of monitoring events to `/var/log/server_monitor.log`.
- **Usage**:
  ```bash
  chmod +x server_monitor.sh
  ./server_monitor.sh
  ```
- **Configuration**:
  - Edit `THRESHOLD_CPU`, `THRESHOLD_MEM`, `THRESHOLD_DISK` to set desired limits.
  - Update `EMAIL` with a valid email address for alerts.
  - Ensure `mail` utility is installed and configured.

### Log File Analyzer
- **File**: `log_analyzer.py`
- **Description**: A Python script that parses server log files to generate reports on errors and usage patterns, such as top errors and IP request counts.
- **Features**:
  - Identifies errors using regex patterns (ERROR, FAIL, CRITICAL).
  - Summarizes top 5 errors and IP addresses by request count.
  - Handles file not found and general exceptions.
- **Usage**:
  ```bash
  python3 log_analyzer.py /path/to/logfile
  ```
- **Configuration**:
  - Requires Python 3.6+.
  - Provide a valid log file path as a command-line argument.

### Automated Backup with Compression and Rotation
- **File**: `backup_script.py`
- **Description**: A Python script that automates incremental backups of a directory, with tar.gz compression and file rotation to manage storage.
- **Features**:
  - Creates compressed backups with timestamped filenames.
  - Rotates old backups to maintain a specified maximum number.
  - Logs all actions to `/var/log/backup_script.log`.
  - Robust error handling for invalid inputs and file operations.
- **Usage**:
  ```bash
  python3 backup_script.py /path/to/source /path/to/backup 5
  ```
- **Configuration**:
  - Requires Python 3.6+.
  - Ensure write permissions for `/var/log/backup_script.log`.
  - Specify source directory, backup directory, and maximum number of backups.

## Requirements
- **Operating System**: Linux (Ubuntu, CentOS recommended)
- **Software**:
  - Bash (for `server_monitor.sh`)
  - Python 3.6+ (for `log_analyzer.py` and `backup_script.py`)
  - `mail` utility (for `server_monitor.sh` email alerts)
  - Standard Linux utilities: `top`, `free`, `df`, `tar`
- **Permissions**:
  - Execute permissions for scripts (`chmod +x`)
  - Write permissions for log files (`/var/log/server_monitor.log`, `/var/log/backup_script.log`)
  - Read/write permissions for source and backup directories

## Installation
1. Clone or download this repository:
   ```bash
   git clone https://github.com/st11fler/sysadmin-scripts.git
   cd sysadmin-scripts
   ```
2. Ensure dependencies are installed:
   ```bash
   sudo apt update
   sudo apt install python3 mailutils
   ```
3. Set execute permissions for the Bash script:
   ```bash
   chmod +x server_monitor.sh
   ```

## Usage
- **Server Monitoring**:
  ```bash
  ./server_monitor.sh
  ```
- **Log Analysis**:
  ```bash
  python3 log_analyzer.py /path/to/logfile
  ```
- **Backup Automation**:
  ```bash
  python3 backup_script.py /path/to/source /path/to/backup 5
  ```
- Refer to individual project sections for configuration details.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
- **Author**: Stivan F
- **Email**: brixeat@gmail.com
- **GitHub**: [github.com/st11fler](https://github.com/st11fler)