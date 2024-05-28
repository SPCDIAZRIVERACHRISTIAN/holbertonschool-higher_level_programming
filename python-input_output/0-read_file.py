#!/usr/bin/python3
"""This function reads a file and prints it content"""


def read_file(filename=""):
    """reads a file and prints it

    Args:
        filename (str, optional): name of file to be read. Defaults to "".

    Returns:
        string: text written in file
    """
    with open(filename, 'r') as file:
        content = file.read()
        print(content, end='')
        return content
