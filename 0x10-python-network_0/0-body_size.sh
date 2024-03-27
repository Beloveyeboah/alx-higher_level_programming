#!/bin/bash
#  Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
if [ $# -eq 0 ]; then
	echo "Usage: $0 <url>"
else
	curl -s "$1" | wc -c
fi
