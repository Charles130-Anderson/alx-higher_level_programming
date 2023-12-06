#!/usr/bin/python3
"""Defining the object attribute lookup function."""


def lookup(obj):
    """
    This function returns a list of the attributes and methods.

    Parameters:
    obj (object): The object whose attributes and methods you want to list.

    Returns:
    list: A list of the object's attributes and methods.
    """
    return dir(obj)
