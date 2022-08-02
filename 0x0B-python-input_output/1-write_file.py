#!/usr/bin/python3
"""A module that contains a function that can write to a file"""


def write_file(filename="", text=""):
    """A function that writes to a file

    Args:
        filename: filename
        text : string
    """
    with open(filename, "r+", encoding="utf-8") as f:
        f.write(text)
        n_lines = len(f.readlines())
    return n_lines
