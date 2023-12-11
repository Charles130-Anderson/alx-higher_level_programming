#!/usr/bin/python3

"""Defines the  base model class."""
import json
import csv


class Base:
    """
    Base class for other classes in the project.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a Base instance.

        Parameters:
        - id (int): The id of the instance (default is None).
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON-formatted string.

        Args:
            list_dictionaries (list): A list of dictionaries to be converted.

        Returns:
            str: A JSON-formatted string representing the list of dictionaries.
                 If the input list is None or empty, returns "[]".
        """
        if list_dictionaries is None or len(list_dictionaries) == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): A list of instances that inherit from Base.

        Returns:
            None
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                dictionaries = [obj.to_dictionary() for obj in list_objs]
                json_string = cls.to_json_string(dictionaries)
                file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        Convert a JSON-formatted string to a list of dictionaries.

        Args:
            json_string (str): A JSON-formatted string.

        Returns:
            list: A list of dictionaries.
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Creates a new instance using a dictionary of attributes.

        Parameters:
        - **dictionary: Double pointer to a dictionary containing attributes.
        Returns:
        Base: An instance of the class with attributes set.
        """
        dummy_instance = cls(1, 1)  # Create a dummy instance with defaults
        dummy_instance.update(**dictionary)  # Update with real values
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """
        Loads instances from a file in JSON format.

        Returns:
        list: List of instances loaded from the file.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_string = file.read()
                dictionaries = cls.from_json_string(json_string)
                instances = [cls.create(**d) for d in dictionaries]
                return instances
        except FileNotFoundError:
            return []
