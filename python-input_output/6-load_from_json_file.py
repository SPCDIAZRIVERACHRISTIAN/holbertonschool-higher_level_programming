#!/usr/bin/python3
"""defines a function that creates an object from a JSON file"""
import json


def load_from_json_file(filename):
    """creates an object from a JSON file"""
    with open(filename, 'r') as f:
        return json.load(f)
