#!/usr/bin/python3
"""
Takes URL input, sends a request , and displays the variable.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    request_id = response.headers.get('X-Request-Id')
    print(request_id)
