#!/bin/bash
# This script takes sends a GET request to the URL with a custom header and displays the response
curl -sH "X-School-User-Id: 98" "$1"
