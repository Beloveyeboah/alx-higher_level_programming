#!/usr/bin/python3

# CREATED BY OSEI YEBOAH ISAAC

def print_sorted_dictionary(a_dictionary):
    """function sorts a dictionary"""

    for key in sorted(a_dictionary.keys()):
        print(f"{key}: {a_dictionary[key]}")
