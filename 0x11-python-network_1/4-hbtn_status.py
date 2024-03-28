#!/usr/bin/python3

"""  Python script that fetches https://alx-intranet.hbtn.io/status """

import requests


if __name__ == "__main__":
    content = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(content.text)))
    print("\t- content: {}".format(content.text))
