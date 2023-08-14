#!/usr/bin/python3

# CREATED BY OSEI YEBOAH ISAAC

def delete_at(my_list=[], idx=0):

    lenx = len(my_list)
    if my_list is None:
        my_list = []
    if 0 <= idx < lenx:
        del my_list[idx]
    return (my_list)
