#!/usr/bin/python3
def remove_char_at(str, n):
    """ removes character at the nth position of the string"""
    if n < 0:
        return str
    return str[0:n] + str[n + 1:]
