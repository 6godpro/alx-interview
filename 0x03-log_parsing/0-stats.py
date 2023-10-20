#!/usr/bin/python3
"""
   This script reads from the stdin line by line and computes metrics.
"""
import sys
import signal

result = {}
total_size = 0


def display_stats():
    """Displays statistics"""
    print("File size: {}".format(total_size))
    for key in sorted(result):
        print(f"{key}: {result[key]}")


def handler(signum, frame):
    """Handles a signal gracefully."""
    display_stats()
    exit(1)


signal.signal(signal.SIGINT, handler)
valid_status_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
count = 0


for line in sys.stdin:
    if count == 10:
        count = 1
        display_stats()
    else:
        count += 1

    try:
        line = line.split()
        status_code, file_size = line[-2], int(line[-1])

        if status_code in valid_status_codes:
            total_size += file_size
            result[status_code] = result.get(status_code, 0) + 1
    except (IndexError, ValueError):
        continue

display_stats()