#!/usr/bin/python3

# CREATED BY OSEI YEBOAH ISAAC

import sys


def safe_function(fct, *args):
    """function that executes a function safely."""

    try:
        ans = fct(*args)
        return (ans)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return (None)
