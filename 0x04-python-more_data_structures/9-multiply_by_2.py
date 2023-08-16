#!/usr/bin/python3

# CREATED BY OSEI YEBOAH ISAAC

def multiply_by_2(a_dictionary):
    """function that returns a new dictionary"""

    new = {}
    for key, value in a_dictionary.items():
        new[key] = value * 2
    return (new)
