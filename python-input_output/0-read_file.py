#!/usr/bin/python3
def read_file(filename=""):
    """reads a file and prints it

    Args:
        filename (str, optional): name or path of file to be read. Defaults to "".

    Returns:
        string: text written in file
    """
    with open(filename, 'r') as file:
        content = file.read()
        print(content, end='')
        return content
