#!/usr/bin/python3
# A Python script that takes in a URL

import urllib.request
import sys

url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    x_request_id = response.headers.get('X-Request-Id')
    print(x_request_id)
