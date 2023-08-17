#!/usr/bin/python3

# CREATED BY OSEI YEBOAH ISAAC


def square_matrix_map(matrix=[]):
    """prints the matrix"""

    return list(map(lambda row: list(map(lambda x: x**2, row)), matrix))
