#!/usr/bin/python3
import re
import sys

def list_ints(lst):
    for item in lst:
        if not item.isdigit():
            return False
    return True

def patterns(input_string):
    pattern = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6})\] "GET \/projects\/(\d+) HTTP\/1\.1" (\d+) (\d+)$'

    # Declare empty lists
    all_codes = []
    _200, _301, _400, _401, _402, _403, _404, _405, _500 = [], [], [], [], [], [], [], [], []

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
        for input_str in input_string:
            input_str = input_str.rstrip()
            time.sleep(1)

            match = re.match(pattern, input_str)

            if match:
                ip_addrress = match.group(1)
                status_code = match.group(4)
                file_size = match.group(5)

                all_codes.append(status_code)
                total_size += int(file_size)
            
            counter += 1

            if counter == 10:
                break
    except KeyboardInterrupt:
        pass

    for code in all_codes:
        for key, value in all_status.items():
            if int(code) == key:
                value.append(code)
    
    print(f"File size: {total_size}")
    for key, value in all_status.items():
        if len(value) > 0 and list_ints(value):
            print(f"{key}: {len(value)}")
        

            


string = [
    "65.48.94.213 - [2023-07-18 01:55:48.977695] \"GET /projects/260 HTTP/1.1\" 400 55",
    "240.188.222.143 - [2023-07-18 01:55:49.440411] \"GET /projects/260 HTTP/1.1\" 500 69",
    "241.35.167.81 - [2023-07-18 01:55:49.762648] \"GET /projects/260 HTTP/1.1\" 500 919",
    "9.148.65.124 - [2023-07-18 01:55:50.614253] \"GET /projects/260 HTTP/1.1\" 403 133",
    "86.251.96.37 - [2023-07-18 01:55:51.314834] \"GET /projects/260 HTTP/1.1\" 500 804",
    "109.252.130.169 - [2023-07-18 01:55:51.958007] \"GET /projects/260 HTTP/1.1\" 403 372",
    "145.130.145.175 - [2023-07-18 01:55:52.803336] \"GET /projects/260 HTTP/1.1\" 405 55",
    "163.233.90.143 - [2023-07-18 01:55:52.830048] \"GET /projects/260 HTTP/1.1\" 404 1021",
    "156.130.102.196 - [2023-07-18 01:55:53.366055] \"GET /projects/260 HTTP/1.1\" 403 281",
    "74.200.44.134 - [2023-07-18 01:55:53.876357] \"GET /projects/260 HTTP/1.1\" 301 374",
    "231.79.250.124 - [2023-07-18 01:55:54.010747] \"GET /projects/260 HTTP/1.1\" 403 505",
    "13.138.233.224 - [2023-07-18 01:55:54.274467] \"GET /projects/260 HTTP/1.1\" 500 590",
    "1.170.158.94 - [2023-07-18 01:55:55.043937] \"GET /projects/260 HTTP/1.1\" 200 688",
    "165.43.62.187 - [2023-07-18 01:55:55.825357] \"GET /projects/260 HTTP/1.1\" 404 451",
    "52.214.204.30 - [2023-07-18 01:55:55.845966] \"GET /projects/260 HTTP/1.1\" 400 3",
    "137.217.226.153 - [2023-07-18 01:55:56.607366] \"GET /projects/260 HTTP/1.1\" 405 221",
    "28.114.97.46 - [2023-07-18 01:55:56.891033] \"GET /projects/260 HTTP/1.1\" 400 765",
    "66.115.70.168 - [2023-07-18 01:55:57.601192] \"GET /projects/260 HTTP/1.1\" 401 803",
    "222.211.69.167 - [2023-07-18 01:55:58.390581] \"GET /projects/260 HTTP/1.1\" 301 764",
    "178.103.204.231 - [2023-07-18 01:55:59.078468] \"GET /projects/260 HTTP/1.1\" 301 247",
    "91.75.198.55 - [2023-07-18 01:55:59.802701] \"GET /projects/260 HTTP/1.1\" 401 998",
    "46.225.48.246 - [2023-07-18 01:56:00.014428] \"GET /projects/260 HTTP/1.1\" 500 546"
]

patterns(string)