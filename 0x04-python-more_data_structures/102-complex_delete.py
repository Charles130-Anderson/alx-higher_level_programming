#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    tmp = a_dictionary.copy()
    return {k: v for k, v in a_dictionary.items() if v != value}
