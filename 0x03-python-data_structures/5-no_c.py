#!/usr/bin/python3

# CREATED BY OSEI YEBOAH ISAAC

def no_c(my_string):
    """ delete c found in the strimg"""
    word = ""

    for x in my_string:
        if x != 'c' and x != 'C':
            word += x
    return (word)
