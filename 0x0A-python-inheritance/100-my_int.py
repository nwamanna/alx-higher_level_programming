#!/usr/bin/python3
""" This module contains a class MyInt """


class MyInt(int):
    """ Inherits from int
    MyInt has == and != operators inverted """
    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
