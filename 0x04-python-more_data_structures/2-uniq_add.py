#!/usr/bin/python3
def uniq_add(my_list=[]):
    """ adds unique elements in a list """
    if my_list is None:
        return
    total = 0
    new = set(my_list)
    for i in new:
        total += i
    return total
