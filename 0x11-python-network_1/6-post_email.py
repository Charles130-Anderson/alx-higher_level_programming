#!/usr/bin/python3
"""
Takes URL and email, sends POST request with email, displays response.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Define the data to be sent in the POST request
    data = {'email': email}

    # Send the POST request and get the response
    response = requests.post(url, data=data)

    # Display the body of the response
    print(response.text)
