#!/usr/bin/python3

"""defines writes an Object to a text file, using a JSON"""

import json


def save_to_json_file(my_obj, filename):
    """function that writes an Object to a text file, using a"""

    with open(filename, "w") as f:
        json.dump(my_obj, f)
