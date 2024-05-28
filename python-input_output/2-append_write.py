#!/usr/bin/python3
"""Defines a function that appends text and returns number of characters."""


def append_write(filename="", text=""):
    """Appends text to file it creates a new if it doesnt exist
        and returns length of text

    Args:
        filename (str, optional): name of file. Defaults to "".
        text (str, optional): string to be written. Defaults to "".

    Returns:
        int: number of characters appended
    """
    with open(filename, 'a+') as file:
        file.write(text)
        return len(text)
