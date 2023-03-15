#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """ deletes key in dictionary """
    if type(key) != str:
        return a_dictionary
    if key not in a_dictionary:
        return a_dictionary
    a_dictionary.pop(key)
    return a_dictionary
