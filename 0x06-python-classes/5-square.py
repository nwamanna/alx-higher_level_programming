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
        self.__set_size(size)

    def area(self):
        """ Square method that calcuates the area of a square
        Returns:
            The current square area
        """
        self.a = self.__size ** 2
        return (self.a)

    def __set_size(self, size=0):
        """ Sets the value of size of a square """
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def __get_size(self):
        """ retrives the size of a square
        Returns:
            The size of square
        """
        return (self.__size)

    size = property(__get_size, __set_size)

    def my_print(self):
        """ prints the square on standard output """
        n = self.__size
        if n == 0:
            print()
        while (n):
            j = self.__size
            while (j):
                print("#", end="")
                j -= 1
            print()
            n -= 1
