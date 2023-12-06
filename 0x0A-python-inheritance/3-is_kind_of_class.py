#!/usr/bin/python3
"""This defines a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """
    This function checks if an object is an instance of, or if the object is
    an instance of a class that inherited from, the specified class.

    Parameters:
    obj (object): The object to check.
    a_class (class): The class to check against.

    Returns:
    bool: True if the object is an instance of, or if the object is an instance
    of a class that inherited from, the specified class. False otherwise.
    """
    return isinstance(obj, a_class)
