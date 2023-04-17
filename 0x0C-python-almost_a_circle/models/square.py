#!/usr/bin/python3
""" This module contains Square Class """
from .rectangle import Rectangle


class Square(Rectangle):
    """ This class inherits from Rectangle that inherits from Square """
    def __init__(self, size, x=0, y=0, id=None):
        Rectangle.__init__(self, size, size, x, y, id)

    def __str__(self):
        return f'[{self.__class__.__name__}] ({self.id}) {self.x}/{self.y} -  {self.width}'

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        if args and type(args) is not dict:
            self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            keys = list(kwargs.keys())
            if "id" in keys:
                self.id = kwargs['id']
            if "size" in keys:
                self.size = kwargs['size']
            if "x" in keys:
                self.x = kwargs['x']
            if "y" in keys:
                self.y = kwargs['y']

    def to_dictionary(self):
        sqr_dict = {}
        sqr_dict['x'] = self.x
        sqr_dict['y'] = self.y
        sqr_dict['id'] = self.id
        sqr_dict['size'] = self.size
        return sqr_dict
