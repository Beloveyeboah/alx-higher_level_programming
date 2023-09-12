#!/usr/bin/python3

"""define append function"""


def append_write(filename="", text=""):
    """ sppend a text """

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
