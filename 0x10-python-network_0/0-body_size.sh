#!/bin/bash

# This script that displays the size of the body of the response in bytes
#
curl -sI "$1" | grep "Content-Length:" | cut -d " " -f 2
