#!/usr/bin/python3
""" This module contains a class called Rectangle """


class Rectangle:
    """ Rectangle class that has all the properties of a rectangle """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        w = self.width
        h = self.height
        return w * h

    def perimeter(self):
        w = self.width
        h = self.height
        if w == 0 or h == 0:
            p = 0
        else:
            p = 2 * (w + h)
        return p

    def __str__(self):
        rec = []
        w = self.width
        h = self.height
        if w == 0 or h == 0:
            return ""
        while h:
            i = 0
            while i < w:
                rec.append(str(self.print_symbol))
                i += 1
            if h == 1:
                break
            rec.append("\n")
            h -= 1
        return "".join(rec)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.width}, {self.height})"

    def __del__(self):
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
