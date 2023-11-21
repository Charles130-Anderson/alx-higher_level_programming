#!/usr/bin/python3
"""Defining  class Square."""


class Square:
    """
    A class that defines a square.

    Attributes:
        size (int): The size of the square.
        position (tuple): The position of the square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
            position (tuple, optional): The position of the square.
                Defaults to (0, 0).

        Raises:
            TypeError: If size is not an integer or position is not a tuple
                of 2 integers.
            ValueError: If size is less than 0.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter method for the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute.

        Args:
            value (int): The value to set as the size attribute.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter method for the position attribute."""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method for the position attribute.

        Args:
            value (tuple): The value to set as the position attribute.

        Raises:
            TypeError: If the value is not a tuple of 2 integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(i, int) for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Public instance method to calculate the area of the square."""
        return self.size ** 2

    def my_print(self):
        """Public instance method to print the square with '#' characters."""
        if self.size == 0:
            print()
            return
        for _ in range(self.position[1]):
            print()
        for _ in range(self.size):
            print(" " * self.position[0] + "#" * self.size)

    def __str__(self):
        """Returns a string representation of the square."""
        result = ""
        if self.size == 0:
            return result
        for _ in range(self.position[1]):
            result += "\n"
        for _ in range(self.size):
            result += " " * self.position[0] + "#" * self.size + "\n"
        return result.strip()
