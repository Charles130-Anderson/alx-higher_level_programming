#!/usr/bin/python3
"""Defines the  square class."""
import csv
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class inherits from Rectangle class.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square instance.

        Parameters:
        - size (int): The size of the square.
        - x (int): The x-coordinate of the square (default is 0).
        - y (int): The y-coordinate of the square (default is 0).
        - id (int): The id of the square (default is None).
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Getter for the size attribute.

        Returns:
        int: The size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute.

        Parameters:
        - value (int): The value to set for size.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Updates attributes of the Square.

        Parameters:
        - *args: List of arguments (no-keyworded).
        - **kwargs: Dictionary of keyworded arguments.
        """
        if args:
            attributes = ["id", "size", "x", "y"]
            for i, value in enumerate(args):
                setattr(self, attributes[i], value)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """
        String representation of the Square instance.

        Returns:
        str: Formatted string representing the Square.
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )

    def to_dictionary(self):
        """
        Returns the dictionary representation of the Square.

        Returns:
        dict: Dictionary containing id, size, x, and y.
        """
        return {
            "id": self.id,
            "size": self.width,  # width and height are the same for a square
            "x": self.x,
            "y": self.y
        }

    def to_csv_row(self):
        """
        Returns a list representing the CSV row for Square serialization.

        Returns:
        list: List containing id, size, x, and y.
        """
        return [str(getattr(self, key)) for key in ["id", "size", "x", "y"]]

    @classmethod
    def create_from_csv_row(cls, row):
        """
        Creates a Square instance from a CSV row.

        Parameters:
        - row (list): List containing id, size, x, and y.

        Returns:
        Square: Created Square instance.
        """
        return cls(*map(int, row))
