#!/usr/bin/python3
""" This module contain a BaseGeometry class """


class BaseGeometry:
    """ Empty class """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError(f"{value} must be an integer")
        if value <= 0:
            raise ValueError(f"{value} must be greater than 0")

