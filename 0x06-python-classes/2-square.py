#!/usr/bin/python3
""" This module creates a class called square """


class Square:
    """ This class defines a square.

    The __init__ method instantiates the square with a size

    Args:
        size (int): size of square

    Attributes:
        size (int): size of square

    Raises:
        TypeError: size must be an integer
        ValueError: size must be greater or equal to Zero
    """
    def __init__(self, size=0):
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
