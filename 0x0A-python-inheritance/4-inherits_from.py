#!/usr/bin/python3
"""This defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    """
    This function checks if an object is an instance of a class that inherited
    (directly or indirectly) from the specified class.

    Parameters:
    obj (object): The object to check.
    a_class (class): The class to check against.

    Returns:
    bool: True if the object is an instance of a class that inherited (directly
    or indirectly) from the specified class. False otherwise.
    """
    return issubclass(type(obj), a_class)
