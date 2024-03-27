#!/bin/bash
# For checking if the argument is not equal to 2
curl -s -X POST -H "Content-Type: application/json" -d "@$2" "$1"
