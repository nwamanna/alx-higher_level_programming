#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """ prints out x number of elements in my_list """
    i = 0
    count = 0
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except IndexError:
            raise
        except ValueError:
            pass
        except TypeError:
            pass
        i += 1
    print()
    return (count)
