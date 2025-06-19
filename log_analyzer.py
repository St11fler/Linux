#!/usr/bin/env python3

# Script to analyze server log files and generate a report
# Author: Stivan F
# Usage: python3 log_analyzer.py /path/to/logfile

import sys
import re
from collections import Counter
from datetime import datetime

def analyze_log(file_path):
    """Analyze log file and print error counts and usage patterns."""
    error_count = Counter()
    ip_requests = Counter()
    error_pattern = re.compile(r'ERROR|FAIL|CRITICAL')
    
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Count errors
                if error_pattern.search(line):
                    error_count[line.split()[0]] += 1
                # Count requests by IP
                ip = line.split()[0]
                ip_requests[ip] += 1
                
        # Generate report
        print(f"Log Analysis Report - {datetime.now()}")
        print("\nTop 5 Errors:")
        for error, count in error_count.most_common(5):
            print(f"{error}: {count} occurrences")
            
        print("\nTop 5 IPs by Request Count:")
        for ip, count in ip_requests.most_common(5):
            print(f"{ip}: {count} requests")
            
    except FileNotFoundError:
        print(f"Error: File {file_path} not found")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 log_analyzer.py /path/to/logfile")
        sys.exit(1)
    analyze_log(sys.argv[1])