#!/usr/bin/python3

# CREATED BY OSEI YEBOAH ISAAC

def complex_delete(a_dictionary, value):
    """deletes from a dictionary"""

    keys_rem = []
    for key in a_dictionary:
        if a_dictionary[key] == value:
            keys_rem.append(key)
    for key in keys_rem:
        del a_dictionary[key]
    return (a_dictionary)
