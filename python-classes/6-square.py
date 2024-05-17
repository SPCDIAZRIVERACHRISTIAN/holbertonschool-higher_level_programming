#!/usr/bin/python3

"""Class named Square that defines a square."""


class Square:
    """Represents a square."""
    def __init__(self, size=0, position=(0, 0)):
        """Instantiates posistion and size

        Args:
            size (int, optional): Size of the new square. Defaults to 0.
            position (int, optional): Position of the new square.
            Defaults to (0, 0).
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Gets position of square

        Returns:
            int: Position of square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the value in position.

        Args:
            value (tuple): Must be a tuple of 2 positive int.

        Raises:
            TypeError: If not 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """returns the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Prints # for the size of the square with position."""
        if self.__size == 0:
            print("")

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
