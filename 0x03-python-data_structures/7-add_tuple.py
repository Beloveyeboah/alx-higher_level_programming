#!/usr/bin/python3

# CREATED BY OSEI YEBOAH ISAAC

def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = tuple_a + (0, 0)
    tuple_b = tuple_b + (0, 0)

    c = tuple_a[0] + tuple_b[0]
    s = tuple_a[1] + tuple_b[1]
    return (c, s)
