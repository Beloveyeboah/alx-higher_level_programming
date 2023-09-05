#!/usr/bin/python3

# CREATED BY OSEI YEBPAH ISAAC

"""return sum of int"""


def add_integer(a, b=98):
    """ return addition of integers"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
