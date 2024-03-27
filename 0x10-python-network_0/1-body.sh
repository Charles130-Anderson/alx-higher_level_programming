#!/bin/bash

# This script takes in a URL, sends a GET request to the URL, and displays the body of the response
# It only displays the body of a 200 status code response
# It uses curl to send the request

# Shebang line specifies the interpreter to use (Bash)

# Usage: ./1-body.sh URL

# Send a GET request to the URL and display the body of the response for a 200 status code
curl -s -L -X GET "$1"
