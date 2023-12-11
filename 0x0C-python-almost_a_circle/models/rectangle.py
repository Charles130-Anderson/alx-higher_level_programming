#!/usr/bin/python3
"""Defines the rectangle class."""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class inherits from Base class.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle instance.

        Parameters:
        - width (int): The width of the rectangle.
        - height (int): The height of the rectangle.
        - x (int): The x-coordinate of the rectangle (default is 0).
        - y (int): The y-coordinate of the rectangle (default is 0).
        - id (int): The id of the rectangle (default is None).
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter for the width attribute.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width attribute.

        Parameters:
        - value (int): The value to set for width.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for the height attribute.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height attribute.

        Parameters:
        - value (int): The value to set for height.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Getter for the x attribute.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for the x attribute.

        Parameters:
        - value (int): The value to set for x.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Getter for the y attribute.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for the y attribute.

        Parameters:
        - value (int): The value to set for y.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
        int: The area of the rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """
        Prints the Rectangle instance using '#' characters,
        taking into account the x and y coordinates.
        """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(' ' * self.__x + '#' * self.__width)

    def __str__(self):
        """
        Returns a string representation of the Rectangle.

        Returns:
        str: The string representation of the Rectangle.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height
        )

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the Rectangle instance.

        Parameters:
        - args (tuple): A variable number of arguments in the order
                       id, width, height, x, and y.
        - kwargs (dict): Key-worded arguments representing attributes
                        to be updated.
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns the dictionary representation of the Rectangle.

        Returns:
        dict: Dictionary containing id, width, height, x, and y.
        """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """
        String representation of the Rectangle instance.

        Returns:
        str: Formatted string representing the Rectangle.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height
        )

    def to_csv_row(self):
        """
        Returns a list representing the CSV row for Rectangle serialization.

        Returns:
        list: List containing id, width, height, x, and y.
        """
        return [
            str(getattr(self, key))
            for key in ["id", "width", "height", "x", "y"]
        ]

    @classmethod
    def create_from_csv_row(cls, row):
        """
        Creates a Rectangle instance from a CSV row.

        Parameters:
        - row (list): List containing id, width, height, x, and y.

        Returns:
        Rectangle: Created Rectangle instance.
        """
        return cls(*map(int, row))
