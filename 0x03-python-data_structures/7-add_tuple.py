#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """ add two tuples """
    if len(tuple_a) > 2:
        tuple_a_slice = tuple_a[:2]
        a1, a2 = tuple_a_slice
    elif len(tuple_a) == 1:
        a1 = tuple_a[0]
        a2 = 0
    elif len(tuple_a) == 0:
        a1 = 0
        a2 = 0
    else:
        a1, a2 = tuple_a
    if len(tuple_b) > 2:
        tuple_b_slice = tuple_b[:2]
        b1, b2 = tuple_b_slice
    elif len(tuple_b) == 1:
        b1 = tuple_b[0]
        b2 = 0
    elif len(tuple_b) == 0:
        b1 = 0
        b2 = 0
    else:
        b1, b2 = tuple_b
    c1 = a1 + b1
    c2 = a2 + b2
    tuple_c = (c1, c2)
    return tuple_c
