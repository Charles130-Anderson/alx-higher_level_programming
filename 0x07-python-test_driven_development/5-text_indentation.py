#!/usr/bin/python3
"""Defining  a function."""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?' and ':'

    Args:
        text (str): The input text.

    Raises:
        TypeError: If `text` is not a string.

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    separators = ['.', '?', ':']
    start = 0

    for i in range(len(text)):
        if text[i] in separators:
            print(text[start:i + 1].strip())
            print()
            start = i + 1

    if start < len(text):
        print(text[start:].strip())
