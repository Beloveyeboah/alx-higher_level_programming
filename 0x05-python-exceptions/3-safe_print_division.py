#!/usr/bin/python3

# CREATED BY OSEI YEBOAH ISAAC

def safe_print_division(a, b):
    """function that divides 2 integers"""

    try:
        c = a / b
    except (TypeError, ZeroDivisionError):
        c = None
    finally:
        print("Inside result: {}".format(c))
    return (c)
