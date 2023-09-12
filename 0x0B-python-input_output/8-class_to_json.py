#!/usr/bin/python3

""" function that returns the dictionary description with"""


def class_to_json(obj):
    """ obj is an instance of a Class"""

    return obj.__dict__
