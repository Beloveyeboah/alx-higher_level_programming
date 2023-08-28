#!/usr/bin/python3

# CREATED BY OSEI YEBOAH ISAAC

def safe_print_list_integers(my_list=[], x=0):
    """ function that prints the first x"""
    tot = 0
    try:

        for num in range(x):
            if type(my_list[num]) == int:
                print("{:d}".format(my_list[num]), end="")
                tot = tot + 1
    except IndexError:
        pass
    print("")
    return tot
