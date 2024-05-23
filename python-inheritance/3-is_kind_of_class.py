#!/usr/bin/python3
"""this returns true if instance of object is from class."""


def is_kind_of_class(obj, a_class):
    """checks class of object

    Args:
        obj: value to be verified
        a_class: type of class

    Returns:
       Bool: Returns true if is that kind of class
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
