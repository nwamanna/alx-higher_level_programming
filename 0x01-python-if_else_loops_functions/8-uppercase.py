#!/usr/bin/python3
def uppercase(str):
    """ prints all letters in uppercase"""
    for i in str:
        if (ord(i) >= 97) and (ord(i) <= 122):
            i = chr(ord(i) - 32)
        print("{:c}".format(i), end="")
    print()
