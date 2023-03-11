#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """ prints elements of a list in reverse """
    if len(my_list) == 1:
        print("{:d}".format(my_list[0]))
    else:
        for i in reversed(my_list):
            print("{:d}".format(i))
