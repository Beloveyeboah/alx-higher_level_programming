#!/usr/bin/python3
"""
Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""

from sys import argv
import requests

if __name__ == "__main__":
    username = argv[1]
    token = argv[2]
    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(username, token))
    res_id = response.json()
    res_id = res_id.get('id')
    print(res_id)
