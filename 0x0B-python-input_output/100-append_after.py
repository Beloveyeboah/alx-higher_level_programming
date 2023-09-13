#!/usr/bin/python3

"""defines function that inserts a line of text to a file, after """


def append_after(filename="", search_string="", new_string=""):
    """ searches for strings"""

    text = ""
    with open(filename) as f:
        for line in f:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
