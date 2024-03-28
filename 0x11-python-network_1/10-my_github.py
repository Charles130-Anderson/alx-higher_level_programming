#!/usr/bin/python3
"""
Takes GitHub credentials and displays the user's id.
"""

import requests
import sys

url = 'http://0.0.0.0:5000/search_user'
q = sys.argv[1] if len(sys.argv) > 1 else ""
response = requests.post(url, data={'q': q})
try:
    data = response.json()
    if data:
        for item in data:
            print("[{}] {}".format(item['id'], item['name']))
    else:
        print("No result")
except ValueError:
    print("Not a valid JSON")
