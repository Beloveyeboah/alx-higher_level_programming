#!/usr/bin/python3

# CREATED BY OSEI YEBOAH ISAAC

def only_diff_elements(set_1, set_2):
    """function that returns a union of a set"""

    set_3 = set_1.union(set_2)
    for i in set_2:
        if i in set_1:
            set_3.remove(i)
    return (set_3)
