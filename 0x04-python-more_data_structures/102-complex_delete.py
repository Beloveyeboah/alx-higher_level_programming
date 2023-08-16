#!/usr/bin/python3

# CREATED BY OSEI YEBOAH ISAAC

def complex_delete(a_dictionary, value):
    """deletes from a dictionary"""

    new = {
            key: val for key, val in a_dictionary.items() if val != value
            }
    return (new)
