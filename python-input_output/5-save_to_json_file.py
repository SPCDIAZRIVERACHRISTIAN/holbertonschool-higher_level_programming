#!/usr/bin/python3
"""Defines a function that writes an object """
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a JSON file"""
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
        return None
