#!/usr/bin/python3
""" This module contains a function that
prints a square
"""


def print_square(size):
    """ prints a square of size size
    Args:
        size - size of the square
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    square = size
    while size:
        i = 0
        while i < square:
            print("#", end="")
            i += 1
        print()
        size -= 1
