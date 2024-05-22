#!/usr/bin/python3
"""This returns a list of available attributes and methods of an object"""


def lookup(obj):
    """returns a list of available attributes"""
    return dir(obj)
