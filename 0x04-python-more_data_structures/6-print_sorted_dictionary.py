#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """ prints sorted key and value of a dictionary """
    a = dict(sorted(a_dictionary.items()))
    for key, val in a.items():
        print("{:s}: {}".format(key, val))
