#!/usr/bin/python3
"""
function that returns the dictionary
description with simple data structure (list, dictionary,
string, integer and boolean) for JSON serialization of an object
"""


def class_to_json(obj):
    """A function that returns a dictionary description of obj"""

    r = {}
    if hasattr(obj, "__dict__"):
        r = obj.__dict__.copy()
    return r
