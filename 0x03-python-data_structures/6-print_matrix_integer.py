#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """ prints all integers in a matrix """
    for i in matrix:
        for j in i:
            print(j, end=' ')
        print()
