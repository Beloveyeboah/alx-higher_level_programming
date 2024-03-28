#!/usr/bin/python3

""" Python script that takes in a URL,
sends a request to the URL and displays
the value of the X-Request-Id variable
found in the header of the response.
"""

import urllib.request as ur
from sys import argv
import urllib.error


if __name__ == "__main__":

    try:
        url = argv[1]
        response = ur.Request(url)
        with ur.urlopen(response) as content:
            headers = content.info()
            x_id = headers.get('X-Request-Id')
            print(x_id)
    except urllib.error.URLError as e:
        print(f"URL Error: {e.reason}")
