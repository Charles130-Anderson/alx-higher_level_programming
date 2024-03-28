#!/usr/bin/python3
import requests
import sys

# Command-line arguments: username and personal access token
username = sys.argv[1]
token = sys.argv[2]

# GitHub API endpoint for fetching user information
url = "https://api.github.com/user"

# Using Basic Authentication with the username and personal access token
response = requests.get(url, auth=(username, token))

# Check if the request was successful
if response.status_code == 200:
    # Extract the user ID from the response JSON
    user_id = response.json().get('id')
    print(user_id)
else:
    print("None")
