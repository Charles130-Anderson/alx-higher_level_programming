#!/bin/bash

# This script takes in a URL, sends a request to that URL, and displays the size of the body of the response in bytes
# It uses curl to send the request and retrieves the content length from the response headers

# Usage: ./0-body_size.sh URL

curl -sI "$1" | grep "Content-Length:" | cut -d " " -f 2
