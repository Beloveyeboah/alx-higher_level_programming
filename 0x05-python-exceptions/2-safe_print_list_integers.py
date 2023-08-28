#!/usr/bin/python3

# CREATED BY OSEI YEBOAH ISAAC

def safe_print_list_integers(my_list=[], x=0):
    """ function that prints the first x"""
    tot = 0
    for num in range(0, x):
        try:
            print("{:d}".format
