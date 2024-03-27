#!/bin/bash
# This script sends a DELETE request to the URL and displays the body of the response
curl -s "$1" -X DELETE
