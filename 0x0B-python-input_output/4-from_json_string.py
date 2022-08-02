#!/usr/bin/python3
"""A module that contains a function that converts a string to obj"""


import json


def from_json_string(my_str):
    """A function that converts a string to obj

    Args:
        my_str: my_str
    """
    return json.loads(my_str)
