#!/usr/bin/python3
def safe_print_division(a, b):
    """ prints result of division otherwise None """
    try:
        result = a / b
        return (result)
    except ZeroDivisionError:
        result = None
        return (result)
    finally:
        print("Inside result: {}".format(result))
