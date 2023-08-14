#!/usr/bin/python3

# CREATED BY OSEI YEBOAH ISAAC

"""Write a function that finds the biggest integer of a list."""


def max_integer(my_list=[]):

    if my_list is None:
        return None
    if len(my_list) == 0:
        return None
    comp = my_list[0]
    for i in my_list:
        if i > comp:
            comp = i
    return (comp)
