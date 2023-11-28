#!/usr/bin/python3
"""
This module provides a function for printing a square with the character #.
"""


def print_square(size):
    """
    Prints a square with the character #.

    Args:
        size (int): The size length of the square.

    Raises:
        TypeError: If size is not an integer or if size is a float.
        ValueError: If size is less than 0.

    Example:
        >>> print_square(4)
        ####
        ####
        ####
        ####

        >>> print_square(10)
        ##########
        ##########
        ##########
        ##########
        ##########
        ##########
        ##########
        ##########
        ##########
        ##########

        >>> print_square(0)
        <empty line>

        >>> print_square(1)
        #

        >>> print_square(-1)
        Traceback (most recent call last):
            ...
        ValueError: size must be >= 0
    """
    # Validate input type
    if not isinstance(size, int) or isinstance(size, bool):
        raise TypeError("size must be an integer")
    
    # Validate input value
    if size < 0:
        raise ValueError("size must be >= 0")

    # Print the square
    for _ in range(size):
        print("#" * size)
    if size == 0:
        print()
