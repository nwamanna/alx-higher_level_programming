#!/usr/bin/python3
""" Module contains a function that returns True
if the object is exactly an instance of the specified class
"""


def is_same_class(obj, a_class):
    """ returns true if object is an instance of class """
    return type(obj) is a_class
