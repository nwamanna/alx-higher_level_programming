#!/usr/bin/python3
def best_score(a_dictionary):
    """ returns key with highest value """
    if a_dictionary is None:
        return
    my_list = list(a_dictionary.values())
    maxi = my_list[0]
    for i in my_list:
        if i > maxi:
            maxi = i
    key = list(filter(lambda x: a_dictionary[x] == maxi, a_dictionary))
    return key[0]
