#!/usr/bin/python3
"""MagicClass with docstrings:"""


class MagicClass:
    """
    A class that represents a magic circle.

    Attributes:
        __radius (float): The radius of the magic circle.
    """

    def __init__(self, radius=0):
        """
        Initializes a new instance of the MagicClass.

        Args:
            radius (float, optional): The radius of the magic circle to 0.
        """
        if type(radius) not in [int, float]:
            raise TypeError("radius must be a number")
        if radius < 0:
            raise ValueError("radius must be >= 0")

        self.__radius = radius

    def area(self):
        """
        Calculates and returns the area of the magic circle.

        Returns:
            float: The area of the magic circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculates and returns the circumference of the magic circle.

        Returns:
            float: The circumference of the magic circle.
        """
        return 2 * math.pi * self.__radius
