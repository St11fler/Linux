#!/bin/bash

# Script to monitor server resources and send email alerts
# Author: Stivan F
# Usage: ./server_monitor.sh

# Configuration
THRESHOLD_CPU=85
THRESHOLD_MEM=80
THRESHOLD_DISK=90
EMAIL="admin@example.com"
LOG_FILE="/var/log/server_monitor.log"

# Function to send email alert
send_alert() {
    local subject=$1
    local message=$2
    echo "$message" | mail -s "$subject" "$EMAIL"
    echo "$(date): $subject - $message" >> "$LOG_FILE"
}

# Check CPU usage
cpu_usage=$(top -bn1 | grep "Cpu(s)" | awk '{print $2 + $4}')
if (( $(echo "$cpu_usage > $THRESHOLD_CPU" | bc -l) )); then
    send_alert "High CPU Usage Alert" "CPU usage is at ${cpu_usage}%"
fi

# Check Memory usage
mem_usage=$(free | grep Mem | awk '{print $3/$2 * 100.0}')
if (( $(echo "$mem_usage > $THRESHOLD_MEM" | bc -l) )); then
    send_alert "High Memory Usage Alert" "Memory usage is at ${mem_usage}%"
fi

# Check Disk usage
disk_usage=$(df / | grep / | awk '{print $5}' | sed 's/%//g')
if [ "$disk_usage" -gt "$THRESHOLD_DISK" ]; then
    send_alert "High Disk Usage Alert" "Disk usage is at ${disk_usage}%"
fi

# Log successful check
echo "$(date): Monitoring completed successfully" >> "$LOG_FILE"