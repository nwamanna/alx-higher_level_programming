#!/usr/bin/python3
""" This module prints text with 2 new_line based on conditions """


def text_indentation(text):
    """ prints 2 new line after any '.', '?' or ':'
    Args:
        text - letters to be printed
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    specialCase = [".", "?", ":"]
    for i in range(len(text)):
        if text[i] == " " and text[i - 1] in specialCase:
            continue
        if text[i] in specialCase:
            print("{}".format(text[i]))
            print()
            continue
        print("{}".format(text[i]), end="")
