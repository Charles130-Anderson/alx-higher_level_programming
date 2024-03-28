#!/usr/bin/python3
"""
Takes URL and email, sends POST request with email as parameter.
and displays the body of the response (decoded in utf-8).
"""

import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Encode the email parameter
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    # Send POST request and decode response body
    with urllib.request.urlopen(url, data) as response:
        print(response.read().decode('utf-8'))
