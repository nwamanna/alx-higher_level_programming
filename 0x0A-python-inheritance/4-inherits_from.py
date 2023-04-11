#!/usr/bin/python3
""" Module contains a function that returns True
if the object is a subclass of the specified class
"""


def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a class that inherited
    from a_class; otherwise False.
    """
    if issubclass(type(obj), a_class):
        return True
    if type(obj) == a_class:
        return False

