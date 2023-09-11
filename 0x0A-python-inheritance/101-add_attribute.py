#!/usr/bin/python3

# CREATED: BELOVE YEBOAH ISAAC

""" function that adds a new attribute to an object """


def add_attribute(obj, atr, value):
    """Add a new attribute to an object if possible
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, atr, value)
