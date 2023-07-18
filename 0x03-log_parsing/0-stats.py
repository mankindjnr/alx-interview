import sys
import re

pattern = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] "GET \/projects\/260 HTTP\/1\.1" (\d{3}) (\d+)$'

# Read input from stdin line by line
for line in sys.stdin:
    line = line.strip()  # Strips leading/trailing whitespaces
    
    # Match the line against the pattern
    match = re.match(pattern, line)
    
    if match:
        ip_address = match.group(1)
        date = match.group(2)
        status_code = match.group(3)
        file_size = match.group(4)
        
        # Process the matched values (replace with your desired logic)
        print(f"IP Address: {ip_address}")
        print(f"Date: {date}")
        print(f"Status Code: {status_code}")
        print(f"File Size: {file_size}")
    else:
        print("Line does not match the specified format.")
