#!/bin/bash

# Sends a JSON POST request to a URL and displays the body of the response

# Check if the file exists
if [ ! -f "$2" ]; then
    echo "File '$2' does not exist."
    exit 1
fi

# Check if the file contains valid JSON
if ! jq . "$2" >/dev/null 2>&1; then
    echo "Not a valid JSON file."
    exit 1
fi

# Send the JSON POST request and display the response body
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
