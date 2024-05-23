#!/usr/bin/python3
"""defines a function for checking instances."""


def is_same_class(obj, a_class):
    """Check if object belongs to class.

    Args:
        obj: value to be verified.
        a_class: type of class

    Returns:
        Bool: True if object is part of the class.
    """
    if type(obj) is a_class:
        return True
    else:
        return False
