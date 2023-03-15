#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """ updates a dictionary key with value """
    if type(key) != str:
        return a_dictionary
    a_dictionary[key] = value
    return a_dictionary
