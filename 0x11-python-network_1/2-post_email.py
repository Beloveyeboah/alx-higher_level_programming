#!/usr/bin/python3
""" python script that takes in a URL and an email,
sends a POST request to the passed URL with
the email as a parameter, and displays the
body of the response (decoded in utf-8)
"""
from sys import argv
import urllib.parse
import urllib.request
import urllib.error


if __name__ == "__main__":
    try:
        url = argv[1]
        value = {"email": argv[2]}
        data = urllib.parse.urlencode(value).encode("ascii")

        request = urllib.request.Request(url, data)
        with urllib.request.urlopen(request) as response:
            content = response.read()
            content = content.decode('utf-8')
            print(content)
    except urllib.error.URLError as e:
        print(f"url Error: {e.reason}")
