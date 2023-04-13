#!/usr/bin/python3
""" This module contain a Square class """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ subclass of Rectangle class """
    def __init__(self, size):
        self.integer_validator("size", size)
        Rectangle.__init__(self, size, size)
