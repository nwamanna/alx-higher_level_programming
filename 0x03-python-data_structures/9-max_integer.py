#!/usr/bin/python3
def max_integer(my_list=[]):
    """ returns maximum value """
    maxi = 0
    if len(my_list) == 0:
        return None
    else:
        for i in my_list:
            if i > maxi:
                maxi = i
        return maxi
