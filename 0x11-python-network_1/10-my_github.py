#!/usr/bin/python3
"""
Takes GitHub credentials and display the user's id.
"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    # Define the URL for the GitHub API to get user information
    url = "https://api.github.com/user"

    # Send a GET request to the GitHub API with Basic Authentication
    response = requests.get(url, auth=(username, password))

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response JSON
        user_info = response.json()
        # Display the user's id
        print(user_info.get("id"))
    else:
        print(None)
