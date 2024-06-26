#!/usr/bin/python3
""" python script that takes in a URL and an email,
sends a POST request to the passed URL with
the email as a parameter, and displays the
body of the response (decoded in utf-8)
"""
from sys import argv
import requests


if __name__ == "__main__":
    url = argv[1]
    value = {"email": argv[2]}
    req = requests.post(url, data=value)
    print(req.text)
