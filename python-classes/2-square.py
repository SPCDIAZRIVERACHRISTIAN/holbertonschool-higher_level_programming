#!/usr/bin/python3

"""Class named Square that defines a square."""


class Square:
    """Represents a square"""
    def __init__(self, size):
        """initiates the size of a square.

        Args:
            size (int): size of the new square.

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
