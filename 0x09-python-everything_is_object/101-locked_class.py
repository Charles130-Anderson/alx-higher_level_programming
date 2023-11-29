#!/usr/bin/python3
"""Defines the locked class."""


class LockedClass:
    """
    Class with a single attribute 'first_name' and no dynamic creation
    of other attributes.

    Attributes:
        first_name (str): The first name attribute.

    Raises:
        AttributeError: If an attempt is made to dynamically create an
        attribute other than 'first_name'.
    """
    __slots__ = ['first_name']
