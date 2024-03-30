#!/usr/bin/python3
"""
Write a Python script that takes 2 arguments in order to solve this challenge.

The first argument will be the repository name
The second argument will be the owner name
You must use the packages requests and sys
You are not allowed to import packages other than requests and sys
You don’t need to check arguments passed to the script (number or type)
"""

from sys import argv
import requests

if __name__ == "__main__":
    repo = argv[1]
    user = argv[2]
    url = f"https://api.github.com/repos/{repo}/{user}/commits"
    num_of_commit = {'per_page': 10}
    response = requests.get(url, num_of_commit)
    if response.status_code == 200:
        commits = response.json()
        for i in commits:
            sha = i['sha']
            author = i['commit']['author']['name']
            print("{}: {}".format(sha, author))
