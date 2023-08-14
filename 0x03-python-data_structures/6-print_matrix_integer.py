#!/usr/bin/python3

# CREATED BY OSEI YEBOAH ISAAC

"""prints int in a matrix"""


def print_matrix_integer(matrix=[[]]):

    for col in matrix:
        for row in col:
            print("{:d}".format(row), end=" ")
        print()
