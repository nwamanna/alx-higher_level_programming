#!/usr/bin/python3
def multiple_returns(sentence):
    """ returns length and first letter of sentence """
    a = len(sentence)
    if len(sentence) == 0:
        b = None
    else:
        b = sentence[0]
    return a, b
