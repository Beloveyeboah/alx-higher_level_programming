#!/usr/bin/python3

"""
Python script that takes in a URL, sends a request
to the URL and displays the body
of the response (decoded in utf-8).
"""

import urllib.error
import urllib.request
from sys import argv

if __name__ == "__main__":
    try:
        url = argv[1]
        request = urllib.request.Request(url)
        with urllib.request.urlopen(request) as response:
            content = response.read()
            content = content.decode('utf-8')
            print(content)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
