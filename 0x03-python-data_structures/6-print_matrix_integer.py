#!/usr/bin/python3

# CREATED BY OSEI YEBOAH ISAAC

def print_matrix_integer(matrix=[[]]):
    if matrix:
        for column in range(len(matrix[0])):
            for row in range(len(matrix)):
                print("{:d}".format(matrix[column][row]), end=" ")
            print()
