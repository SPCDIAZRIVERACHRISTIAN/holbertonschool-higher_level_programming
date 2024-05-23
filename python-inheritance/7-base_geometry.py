#!/usr/bin/python3
"""Is a class named basegeometry."""


class BaseGeometry:
    """Represents BaseGeometry."""

    def area(self):
        """raises an exception

        Raises:
            Exception: if function not used.
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """validates if value is an integer

        Args:
            name (str): name of the value
            value (int): It is supposed to be an integer

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is not grater than 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
