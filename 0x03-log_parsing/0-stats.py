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


def valid_log(line):
    """Ensures that a line matches to a valid log line.

       e.g A valid log line should look like this:
       <IP> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
    """
    import re

    log_regex = r'^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'
    log_regex += r' - \[.*?\] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)'
    match = re.match(log_regex, line)
    if match:
        return (True, match)
    return (False, None)


signal.signal(signal.SIGINT, handler)
valid_status_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
count = 0


for line in sys.stdin:
    if count == 10:
        count = 1
        display_stats()
    else:
        count += 1

    res = valid_log(line)
    if res[0]:
        status_code, file_size = res[1].groups()
        if status_code in valid_status_codes:
            try:
                total_size += int(file_size)
                if status_code not in result:
                    result[status_code] = 1
                else:
                    result[status_code] += 1
            except Exception as e:
                pass
