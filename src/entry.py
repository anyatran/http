import time
from datetime import datetime

class Entry:
    def __init__(self, host, user, timestamp, req_method, req_url, status, bytes):
        self.host = host
        self.user = user
        self.timestamp = timestamp
        self.req_method = req_method
        self.req_url = req_url
        self.status = int(status)
        self.bytes = int(bytes)
        self.section = self.get_section(req_url)

    def get_section(self, url):
        if url == "/":
            return url
        else:
            return ''.join(['/', url.split('/')[1], '/'])

    def log(self):
        print(self.host, self.section, self.timestamp.month)
