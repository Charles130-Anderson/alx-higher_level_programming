#!/usr/bin/python3
"""Defining  class Square."""


class Square:
    """
    A class that defines a square.

    Attributes:
        size (number): The size of the square.
    """
    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Args:
            size (number, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not a number.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """Getter method for the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute.

        Args:
            value (number): The value to set as the size attribute.

        Raises:
            TypeError: If the value is not a number.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Public instance method to calculate the area of the square."""
        return self.size ** 2

    def __eq__(self, other):
        """Equality comparison based on the square area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Inequality comparison based on the square area."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Less than comparison based on the square area."""
        return self.area() < other.area()

    def __le__(self, other):
        """Less than or equal comparison based on the square area."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Greater than comparison based on the square area."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Greater than or equal comparison based on the square area."""
        return self.area() >= other.area()
