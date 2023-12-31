#!/usr/bin/python3

# CREATED BY OSEI YEBOAH ISAAC

import sys


def safe_print_integer_err(value):
    """function that prints an integer."""

    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return (False)
