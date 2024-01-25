#!/bin/bash
# This script takes a URL, sends a request, and displays the size
curl -s "$1" | wc -c
