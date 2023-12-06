#!/usr/bin/python3""
"Defines a class-checking function."""


def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of a specified class.

    Parameters:
    obj (object): The object to check.
    a_class (class): The class to check against.

    Returns:
    bool: True if the object is exactly an instance of the specified class.
    False otherwise.
    """
    return type(obj) is a_class
