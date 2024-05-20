#!/usr/bin/python3

"""Function to add integers"""


def add_integer(a, b=98):
    """Adds to integers can take floats.

    Args:
        a (int, float): First value to be added.
        b (int, float, optional): Second value to be added. Defaults to 98.

    Raises:
        TypeError: if a is not a float or integer.
        TypeError: If b is not a float or integer.

    Returns:
        int: Sum of a + b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
