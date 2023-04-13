#!/usr/bin/python3
""" contains a function that adds attribute """


def add_attribute(obj, attr, value):
    """ adds attribute to an object
    else raises a error """
    if  not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        obj.__dict__[attr] = value
