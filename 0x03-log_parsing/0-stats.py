#!/usr/bin/python3
"""
log parsing with python
"""
import re
import sys


def list_ints(lst):
    """check if its list of ints"""
    for item in lst:
        if not item.isdigit():
            return False
    return True


pattern = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6})\] "GET \/projects\/(\d+) HTTP\/1\.1" (\d+) (\d+)$'

# Declare empty lists
all_codes = []
_200, _301, _400, _401, _402 = [], [], [], [], []
_403, _404, _405, _500 = [], [], [], []

# Dictionary mapping code_num to corresponding list
all_status = {
    200: _200,
    301: _301,
    400: _400,
    401: _401,
    402: _402,
    403: _403,
    404: _404,
    405: _405,
    500: _500
}

counter = 0
total_size = 0

try:
    for input_str in sys.stdin:
        input_str = input_str.rstrip()

        match = re.match(pattern, input_str)

        if match:
            status_code = match.group(4)
            file_size = match.group(5)

            all_codes.append(status_code)
            total_size += int(file_size

            counter += 1

            if counter == 10:
                for code in all_codes:
                    for key, value in all_status.items():
                        if int(code) == key:
                            value.append(code)

                print(f"File size: {total_size}")
                for key, value in all_status.items():
                    if len(value) > 0:
                        print(f"{key}: {len(value)}")

except KeyboardInterrupt:
    for code in all_codes:
        for key, value in all_status.items():
            if int(code) == key:
                value.append(code)

    print(f"File size: {total_size}")
    for key, value in all_status.items():
        if len(value) > 0 and list_ints(value):
            print(f"{key}: {len(value)}")
