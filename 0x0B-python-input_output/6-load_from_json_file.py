#!/usr/bin/python3

"""define and create json file """

import json


def load_from_json_file(filename):
    """function that creates an Object from a “JSON file”"""

    with open(filename, "r") as f:
        inf = json.load(f)
    return (inf)
