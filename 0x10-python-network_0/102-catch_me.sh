#!/bin/bash
# This script makes a request to 0.0.0.0:5000/catch_me
curl -s -LX PUT 0.0.0.0:5000/catch_me -d "user_id=98" -H "Origin: HolbertonSchool"
