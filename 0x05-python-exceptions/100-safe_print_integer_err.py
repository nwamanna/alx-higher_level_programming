#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """ safely prints value even if it is not an integer """
    try:
        print("{:d}".format(value))
        return True
    except ValueError as err:
        sys.stderr.write(f'Exception: {err}\n')
        return False
