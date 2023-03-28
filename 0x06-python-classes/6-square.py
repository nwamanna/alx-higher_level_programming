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
    def __init__(self, size=0, position=(0, 0)):
        self.__set_size(size)
        self.position = position

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) != tuple and len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

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
        h = self.__position[0]
        if n == 0:
            print()
        while (n):
            h = self.__position[0]
            while (h):
                if self.__position[1] > 0:
                    print("_", end="")
                else:
                    print(" ", end="")
                h -= 1
            j = self.__size
            while (j):
                print("#", end="")
                j -= 1
            print()
            n -= 1
