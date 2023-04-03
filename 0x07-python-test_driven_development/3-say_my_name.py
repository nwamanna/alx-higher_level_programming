#!/usr/bin/python
""" This module prints first and last name """


def say_my_name(first_name, last_name=""):
    """ Print first_name and last_name
    Args:
        first_name
        last_name
    if no last_name is passed, it prints only first_name
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
