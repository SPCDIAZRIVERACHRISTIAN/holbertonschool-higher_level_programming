#!/usr/bin/python3
"""Defines a function that writes text to a file."""


def write_file(filename="", text=""):
    """Returns number of characters written

    Args:
        filename (str, optional): name of file. Defaults to "".
        text (str, optional): text to be written. Defaults to "".

    Returns:
        str: number of characters
    """
    with open(filename, 'w') as file:
        content = file.write(text)
        return len(text)
