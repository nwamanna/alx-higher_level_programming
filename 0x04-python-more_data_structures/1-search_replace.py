#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """ replaces element in a list """
    if my_list is None:
        return
    if my_list.count(search) == 0:
        return my_list
    new_list = my_list[:]
    while new_list.count(search) > 0:
        idx = new_list.index(search)
        new_list[idx] = replace
    return new_list
