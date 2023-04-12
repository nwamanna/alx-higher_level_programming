#!/usr/bin/python3
""" Modules contains a function that appends to a text file
(UTF8)"""


def append_write(filename="", text=""):
    """ append to a text file (UTF8) """
    with open(filename, 'a', encoding="utf-8") as f:
        count = f.write(text)
    return count
