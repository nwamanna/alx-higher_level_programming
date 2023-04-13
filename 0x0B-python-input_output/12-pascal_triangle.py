#!/usr/bin/python3
""" contains a pascal triangle function """


def pascal_triangle(n):
    """ returns a list of lists containing
    values of pascal triangle numbers """
    if n <= 0:
        return []
    matrix = [[1]]
    for i in range(1, n):
        prev_list = matrix[i - 1]
        new_list = [1]
        for j in range(1, i):
            new_list.append(prev_list[j - 1] + prev_list[j])
        new_list.append(1)
        matrix.append(new_list)
    return matrix
