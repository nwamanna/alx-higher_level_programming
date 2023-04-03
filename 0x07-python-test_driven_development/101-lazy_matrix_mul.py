#!/usr/bin/python3
""" Module performs calculation on 2 matrices """
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ Returns a new matrix that is a product of 2 matrices """
    if type(m_a) is not list:
        raise TypeError("m_a must always be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must always be a list")
    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError("m_a cannot be empty")
    if len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_b cannot be empty")
    if len(m_a) < 1 or not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must always be a list of lists")
    if len(m_b) < 1 or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must always be a list of lists")
    length = len(m_a[0])
    for row in m_a:
        if type(row) is not list:
            raise TypeError("m_a must always be a list of lists")
        if len(row) != length:
            raise TypeError("each row of m_a must always be of the same size")
        for i in row:
            if type(i) is not int and type(i) is not float:
                raise TypeError("m_a list should contain only integers or floats")
    length_b = len(m_b[0])
    for row in m_b:
        if type(row) is not list:
            raise TypeError("m_b must always be a list of lists")
        if len(row) != length_b:
            raise TypeError("each row of m_b must always  be of the same size")
        for i in row:
            if type(i) is not int and type(i) is not float:
                raise TypeError("m_b list should contain only integers or floats")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied, check number of rows and columns")
    A = np.array(m_a)
    B = np.array(m_b)
    m_c = np.dot(A, B)
    return m_c
