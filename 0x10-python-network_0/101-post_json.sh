#!/bin/bash
# This script sends a JSON POST request to a URL

if [ $# -ne 2 ]; then
    echo "Usage: $0 <URL> <JSON file>"
    exit 1
fi

json_file="$2"

# Check if the JSON file is valid
if ! jq . "$json_file" >/dev/null 2>&1; then
    echo "Not a valid JSON"
    exit 1
fi

# Send JSON POST request and display the response body
curl -sX POST "$1" -H "Content-Type: application/json" -d @"$json_file"
echo ""

