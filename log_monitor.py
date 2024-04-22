import os
import time
import re
import logging
from collections import Counter

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to monitor the log file
def monitor_log_file(log_file):
    logging.info(f"Monitoring log file: {log_file}")
    
    try:
        with open(log_file, 'r') as file:
            # Go to the end of the file
            file.seek(0, os.SEEK_END)
            
            while True:
                line = file.readline()
                if not line:
                    time.sleep(0.1)
                    continue
                
                yield line
    except KeyboardInterrupt:
        logging.info("Monitoring interrupted. Exiting.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

# Function to analyze log entries
def analyze_log_entries(log_entries):
    error_pattern = re.compile(r'error', re.IGNORECASE)
    http_pattern = re.compile(r'HTTP/\d\.\d\s+(\d+)')
    
    error_count = 0
    status_codes = Counter()
    
    for entry in log_entries:
        if error_pattern.search(entry):
            error_count += 1
        
        match = http_pattern.search(entry)
        if match:
            status_code = match.group(1)
            status_codes[status_code] += 1
    
    logging.info(f"Number of error messages: {error_count}")
    logging.info("Top HTTP status codes:")
    for code, count in status_codes.most_common():
        logging.info(f"{code}: {count}")

# Main function
def main():
    log_file = "access.log"  # Replace with the path to your log file
    
    try:
        log_entries = monitor_log_file(log_file)
        analyze_log_entries(log_entries)
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()