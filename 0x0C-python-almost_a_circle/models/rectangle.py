#!/usr/bin/python3
""" This module contains Rectangle Class """
from .base import Base


def validate(name, value):
    if type(value) != int:
        raise TypeError(f'{name} must be an integer')
    if value <= 0:
        raise ValueError(f'{name} must be > 0')


def validate_xy(name, value):
    if type(value) != int:
        raise TypeError(f'{name} must be an integer')
    if value < 0:
        raise ValueError(f'{name} must be >= 0')


class Rectangle(Base):
    """ Subclass of Base """
    def __init__(self, width, height, x=0, y=0, id=None):
        Base.__init__(self, id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        validate("width", width)
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        validate("height", height)
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        validate_xy("x", x)
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        validate_xy("y", y)
        self.__y = y

    def area(self):
        return self.width * self.height

    def display(self):
        height = self.height
        width = self.width
        x = self.x
        y = self.y
        while y:
            print()
            y -= 1
        while height:
            i = 0
            x = self.x
            while x:
                print(" ", end="")
                x -= 1
            while i < width:
                print("#", end="")
                i += 1
            print()
            height -= 1

    def __str__(self):
        return f'[{self.__class__.__name__}] ({self.id}) {self.x}/{self.y} -  {self.width}/{self.height}'

    def update(self, *args, **kwargs):
        if args and type(args) is not dict:
            self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        else:
            keys = list(kwargs.keys())
            if "id" in keys:
                self.id = kwargs['id']
            if "width" in keys:
                self.width = kwargs['width']
            if "height" in keys:
                self.height = kwargs['height']
            if "x" in keys:
                self.x = kwargs['x']
            if "y" in keys:
                self.y = kwargs['y']

    def to_dictionary(self):
        rec_dict = {}
        rec_dict['x'] = self.x
        rec_dict['y'] = self.y
        rec_dict['id'] = self.id
        rec_dict['height'] = self.height
        rec_dict['width'] = self.width
        return rec_dict
