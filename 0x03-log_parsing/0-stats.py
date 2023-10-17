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
        status_code, file_size = line[-2], line[-1]

        if status_code in valid_status_codes:
            try:
                total_size += int(file_size)
            except Exception as e:
                continue
            if status_code not in result:
                    result[status_code] = 1
            else:
                result[status_code] += 1
    except IndexError:
        continue
