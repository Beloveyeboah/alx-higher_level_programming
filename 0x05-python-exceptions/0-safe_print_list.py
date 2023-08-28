#!/usr/bin/python3

# CREATED BY OSEI YEBOAH ISAAC

def safe_print_list(my_list=[], x=0):
    tot = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            tot += 1
    except IndexError:
        pass
    print("")
    return (tot)
