#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """ returns the square value of all elements in a matrix """
    if matrix == None:
        return
    if len(matrix) <= 0:
        return
    new_list = []
    for i in matrix:
        new_list.append(list(map(lambda x: (x ** 2),i)))
    return new_list
