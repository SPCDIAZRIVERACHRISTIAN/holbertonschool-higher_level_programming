#!/usr/bin/python3
"""defines a function that returns string in json"""
import json


def to_json_string(my_obj):
    """returns a json string representation of an object"""
    return json.dumps(my_obj)
