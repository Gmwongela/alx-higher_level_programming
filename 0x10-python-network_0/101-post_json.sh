#!/bin/bash
# Bash script that sends a JSON POST request to a URL passed as the first argument
curl -s -d "@$2" -H "Content-Type: application/json" -X POST "$1"
