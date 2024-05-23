#!/usr/bin/python3
"""defines a check-instance function for subclasses."""


def inherits_from(obj, a_class):
    """This function checks if the object is a subclass of the class.

    Args:
        obj: value to be checked
        a_class (_type_): class to be used for check

    Returns:
        Bool: returns True if is a subclass and not part of class
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
