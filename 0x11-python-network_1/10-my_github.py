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
    url = f"https://api.github.com/users/{username}"

    # Set up Basic Authentication with the personal access token
    auth = (username, password)

    # Send a GET request to the GitHub API
    response = requests.get(url, auth=auth)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response JSON
        user_info = response.json()
        # Display the user's id
        print(user_info['id'])
    else:
        print(None)
