#!/usr/bin/python3
""" Module contains a function that returns True
if the object is  an instance or subclass of the specified class
"""


def is_kind_of_class(obj, a_class):
    """ returns true if object is an instance or subclass of class """
    if isinstance(obj, a_class):
        return True
