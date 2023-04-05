#!/usr/bin/python3
""" This module divides a matrix by a number div """


def matrix_divided(matrix, div):
    """ Returns a new matrix """
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len(matrix) <= 1 or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    length = len(matrix[0])
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(row) != length:
            raise TypeError("Each row of the matrix must have the same size")
        for i in row:
            if type(i) is not int and type(i) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return list(map((lambda row: list(map(lambda x: round(x / div, 2), row))), matrix))
