#!/usr/bin/python3

from src.reader import Reader
import _thread
import argparse
from generate_logs import generate_logs
from src.constants import DEFAULT_OUTPUT_FILE
import sys
sys.path.append("./src")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(__file__, description="Log Generator")
    parser.add_argument("--generate", "-g", dest="file_generate", help="Output file path", type=str)
    parser.add_argument("--file", "-f", dest="file_read", help="read file path", type=str)
    parser.add_argument("--threshold", "-t", dest="threshold", help="alerting thresholds", type=str)

    args = parser.parse_args()
    file_read = DEFAULT_OUTPUT_FILE if not args.file_read else args.file_read
    file_generate = args.file_generate
    threshold = args.threshold
    r = Reader()

    try:
        _thread.start_new_thread(generate_logs, (file_generate,))
        _thread.start_new_thread(r.read_lines, (file_read,))
    except:
       print("Error: unable to start thread")

    while 1:
       pass
