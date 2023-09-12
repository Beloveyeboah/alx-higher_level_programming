#!/usr/bin/python3

""" defines a func that retuens json obj"""

import json


def from_json_string(my_str):
    """ function that returns an object (Python data structure) """

    return json.loads(my_str)
