#!/usr/bin/python3
""" Modules contains a function that writes to a text file
(UTF8)"""


def write_file(filename="", text=""):
    """ write to a text file (UTF8) """
    with open(filename, 'w', encoding="utf-8") as f:
        count = f.write(text)
    return count
