#!/usr/bin/python3

# CREATED BY OSEI YEBOAH ISAAC

def divisible_by_2(my_list=[]):

    new = []

    for i in my_list:
        if i % 2 == 0:
            new.append(True)
        else:
            new.append(False)
    return (new)
