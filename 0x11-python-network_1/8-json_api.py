#!/usr/bin/python3
"""
Takes letter, sends POST request, displays id and name if JSON is valid.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]

    # Define the data to be sent in the POST request
    data = {'q': q}

    # Send the POST request and get the response
    response = requests.post("http://0.0.0.0:5000/search_user", data=data)

    try:
        # Parse response JSON
        json_response = response.json()

        if json_response:
            # Display id and name if JSON is not empty
            print("[{}] {}".format(json_response.get('id'),
                                   json_response.get('name')))
        else:
            print("No result")
    except ValueError:
        # Handle invalid JSON
        print("Not a valid JSON")
