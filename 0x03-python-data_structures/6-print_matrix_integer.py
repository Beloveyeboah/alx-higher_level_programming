#!/usr/bin/python3

# CREATED BY OSEI YEBOAH ISAAC

"""prints int in a matrix"""


def print_matrix_integer(matrix=[[]]):
    love = len(matrix)
    for x in range(love):
        for y in range(len(matrix[x])):
            print('{:d}'.format(matrix[x][y]), end='')
            if y is not (len(matrix[x]) - 1):
                print(end=" ")
        print("")
