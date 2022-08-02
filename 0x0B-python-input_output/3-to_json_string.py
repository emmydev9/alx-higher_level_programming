#!/usr/bin/python3
"""A module that contains a function that serialize object"""


import json


def to_json_string(my_obj):
    """ function that return as a json dumps of an obj
    Args:
        my_obj: obj

    """
    return json.dumps(my_obj)
