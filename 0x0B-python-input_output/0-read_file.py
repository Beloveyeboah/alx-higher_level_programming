#!/usr/bin/python3

"""Define a function to read text"""


def read_file(filename=""):
    """ reads from stdin"""

    with open(filename, encoding="utf-8") as _file:
        print(_file.read(), end="")
