#!/usr/bin/python3
"""Looks for the biggest number and returns it"""


def max_integer(list=[]):
    """returns biggest number in list

    Args:
        list (list, optional): list with numbers. Defaults to [].

    Returns:
        int: biggest integer in list.
    """
    big1 = list[0]
    if len(list) == 0:
        return None
    if len(list) > 0:
        for i in list:
            if i > big1:
                big1 = i
    return big1
