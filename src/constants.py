#!/usr/bin/python
DEFAULT_OUTPUT_FILE = "./logs/access.log"
RESPONSE_STATUSES = ["200", "404", "500", "301"]
REQUESTS = ["GET", "POST", "DELETE", "PUT"]
CLIENTS = [
    {
        "name": "james",
        "ip": "110.28.77.6"
    },
    {
        "name": "sarah",
        "ip": "212.243.212.247"
    },
    {
        "name": "bob",
        "ip": "169.85.193.81"
    },
    {
        "name": "david",
        "ip": "229.175.141.32"
    },
    {
        "name": "tanya",
        "ip": "59.172.171.151"
    }
]

RESOURCES = ["/pages/create", "/pages/update", "/pages/delete", "/account/update", "/account/create", "/account/delete", "/article/create", "/article/delete", "/article/update"]
