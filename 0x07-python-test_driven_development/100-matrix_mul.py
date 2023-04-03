#!/usr/bin/python3
""" Module performs calculation on 2 matrices """


def matrix_mul(m_a, m_b):
    """ Returns a new matrix that is a product of 2 matrices """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")
    if len(m_a) < 1 or not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if len(m_b) < 1 or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    length = len(m_a[0])
    for row in m_a:
        if type(row) is not list:
            raise TypeError("m_a must be a list of lists")
        if len(row) != length:
            raise TypeError("each row of m_a must be of the same size")
        for i in row:
            if type(i) is not int and type(i) is not float:
                raise TypeError("m_a should contain only integers or floats")
    length_b = len(m_b[0])
    for row in m_b:
        if type(row) is not list:
            raise TypeError("m_b must be a list of lists")
        if len(row) != length_b:
            raise TypeError("each row of m_b must be of the same size")
        for i in row:
            if type(i) is not int and type(i) is not float:
                raise TypeError("m_b should contain only integers or floats")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    m_c = [[0 for j in range(len(m_b[0]))] for i in range(len(m_a))]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                m_c[i][j] += m_a[i][k] * m_b[k][j]
    return m_c
