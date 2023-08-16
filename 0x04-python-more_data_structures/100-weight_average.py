#!/usr/bin/python3

# CREATED BY OSEI YEBOAH ISAAC

def weight_average(my_list=[]):
    """function that returns the weighted average"""

    if len(my_list) == 0:
        return 0
    w = 0
    t = 0
    for i in my_list:
        score, weight = i
        w += score * weight
        t += weight
    if t == 0:
        return 0
    return (w/t)
