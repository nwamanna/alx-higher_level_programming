#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """ prints out x number of elements in my_list """
    i = 0
    try:
        while i < x:
            print("{}".format(my_list[i]), end="")
            i += 1
        print()
        return (x)
    except IndexError:
         print()
         return (i)
