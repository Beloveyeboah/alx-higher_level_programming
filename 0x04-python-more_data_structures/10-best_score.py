#!/usr/bin/python3

# CREATED BY OSEI YEBOAH ISAAC

def best_score(a_dictionary):
    """function that returns a biggest key"""

    if not a_dictionary:
        return None
    best = max(a_dictionary.values())
    for key, value in a_dictionary.items():
        if value == best:
            return (key)
