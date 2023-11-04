#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    _total_a = len(tuple_a)
    _total_b = len(tuple_b)
    if _total_a < 1:
        tuple_a = (0, 0)
    elif _total_a < 2:
        tuple_a = (tuple_a[0], 0)

    if _total_b < 1:
        tuple_b = (0, 0)
    elif _total_b < 2:
        tuple_b = (tuple_b[0], 0)
    addition = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return addition
