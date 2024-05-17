#!/usr/bin/python3

"""Class named Square that defines a square."""


class Square:
    """Represents a square."""
    def __init__(self, size=0):
        """initiates the size of a square.

        Args:
            size (int): size of the new square.
        """
        self.__size = size

    @property
    def size(self):
        """Gets the size of a square.

        Returns:
            int: Returns the size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of a square.

        Args:
            value (int): the new size

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """returns the current square area."""
        return self.__size ** 2
    def my_print(self):