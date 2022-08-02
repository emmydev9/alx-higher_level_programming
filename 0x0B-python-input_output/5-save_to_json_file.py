#!/usr/bin/python3
"""A module that contains a function that writes
 an Object to a text file, using a JSON representation"""

import json


def save_to_json_file(my_obj, filename):
    """a function that writes
    an Object to a text file, using a JSON representation"""
    s_my_obj = json.dumps(my_obj)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(s_my_obj)
