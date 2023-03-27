#!/usr/bin/python3
def safe_print_integer(value):
    """ safely prints value even if it is not an integer """
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        print("{}".format(value))
        return False
