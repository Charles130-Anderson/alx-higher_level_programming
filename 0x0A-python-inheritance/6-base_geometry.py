#!/usr/bin/python3
"""This defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """
    This is an empty class that serves as a base for other geometry classes.
    """

    def area(self):
        """
        This method raises an Exception with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")
