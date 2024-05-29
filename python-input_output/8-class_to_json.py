#!/usr/bin/python3
"""defines a function that returns the dict description for JSON"""


def class_to_json(obj):
    """returns ductuinary description for JSON

    Args:
        obj: Value to be checked

    Returns:
        arg: checked value
    """
    if isinstance(obj, list):
        return [class_to_json(item) for item in obj]
    elif isinstance(obj, dict):
        return {k: class_to_json(v) for k, v in obj.items()}
    elif isinstance(obj, str):
        return obj
    elif isinstance(obj, int):
        return obj
    elif isinstance(obj, bool):
        return obj
    elif hasattr(obj, '__dict__'):
        return {k: class_to_json(v) for k, v in obj.__dict__.items()}
    else:
        return None
