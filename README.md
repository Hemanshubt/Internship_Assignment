Here's how the script works:

#The monitor_log_file function takes a log file path as an argument and continuously monitors the file for new entries using a generator function. It yields new lines as they are added to the file. The function handles keyboard interrupts (Ctrl+C) and other exceptions.

#The analyze_log_entries function takes an iterable of log entries and performs basic analysis:

#It counts the occurrences of the word "error" (case-insensitive) using a regular expression pattern.

#It extracts HTTP status codes from log entries using another regular expression pattern and counts their occurrences using a Counter object.

#It logs the number of error messages and the top HTTP status codes with their counts.
      
#The main function is the entry point of the script. It calls the monitor_log_file function with the path to the log file (access.log in this example) and passes the log entries to the analyze_log_entries function for analysis.

#Error handling and logging are implemented using the logging module. The script logs information, debug, and error messages with timestamps.

#To use the script, save it as log_monitor.py and run it with Python. Make sure to replace "access.log" with the path to your log file.

Here's an example of how to run the script:

Run Code Command:-

python log_monitor.py

[2024-04-22 10:00:02] INFO: Processing request for user 123

While the script is running, it will print new log entries as they are added to the file. You can interrupt the monitoring by pressing Ctrl+C.

Please note that this script assumes that the log file is continuously appended with new entries. If the log file is rotated or replaced, the script will need to be restarted.
