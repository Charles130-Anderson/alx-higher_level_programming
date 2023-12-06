#!/usr/bin/python3
"""Defining the MyList class."""


class MyList(list):
    """
    A custom list class with additional functionality.
    """

    def __init__(self, *args):
        """
        Constructor for MyList.

        Parameters:
        *args: Variable number of arguments to initialize the list.
        """
        super().__init__(*args)

    def print_sorted(self):
        """
        Sorts and prints the elements of the list.
        """
        self.sort()
        print(self)
