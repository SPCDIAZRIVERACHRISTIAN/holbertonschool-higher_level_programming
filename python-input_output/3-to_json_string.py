#!/usr/bin/python3
import json
"""defines a function that returns string in json"""


def to_json_string(my_obj):
    """returns a json string representation of an object"""
    return json.dumps(my_obj)
