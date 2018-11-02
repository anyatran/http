#!/usr/bin/python3
import time
import random
from datetime import datetime, timezone, timedelta
from src.constants import CLIENTS, DEFAULT_OUTPUT_FILE, REQUESTS, RESOURCES, RESPONSE_STATUSES


def generate_logs(file_output=None):
    output_time = datetime.now()
    output_file_name = DEFAULT_OUTPUT_FILE if not file_output else file_output

    f = open(output_file_name, "w")
    while True:
        wait_time = float(random.randint(1, 10))
        increment = timedelta(seconds=wait_time)
        output_time += increment

        client = random.choice(CLIENTS)
        date = datetime.now(timezone.utc).strftime("%d/%b/%Y:%H:%M:%S %z")
        req = random.choice(REQUESTS)

        resourse = random.choice(RESOURCES)

        status = random.choice(RESPONSE_STATUSES)
        size = int(random.gauss(5000, 50))
        f.write('%s - %s [%s] "%s %s HTTP/1.0" %s %s\n' % (client["ip"], client["name"], date, req, resourse, status, size))
        f.flush()
        time.sleep(wait_time)
