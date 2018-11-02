#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import apache_log_parser
import time
from os import SEEK_END
from src.entry import Entry
from src.monitor import Monitor

class Reader:
    def __init__(self):
        self.parser = apache_log_parser.make_parser("%h %l %u %t \"%r\" %>s %b")

    def read_lines(self, file_read):
        try:
            f = open(file_read, "r")
            monitor = Monitor()
            f.seek(0, SEEK_END)
        except:
            print("Cannot open file")
        while True:
            end_of_file = False
            while not end_of_file:
                line = f.readline()
                if not line:
                    end_of_file = True
                else:
                    monitor.add_entry(self.parse_line(line))
                    time.sleep(1)

    def parse_line(self, line):
        parsed_line = self.parser(line)
        e = Entry(parsed_line.get('remote_host'),
                  parsed_line.get('remote_user'),
                  parsed_line.get('time_received_tz_datetimeobj'),
                  parsed_line.get('request_method'),
                  parsed_line.get('request_url'),
                  parsed_line.get('status'),
                  parsed_line.get('response_bytes_clf'))
        e.log()
        return e
