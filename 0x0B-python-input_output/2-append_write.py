#!/usr/bin/python3
"""A module that contains a function that
can append a string to a file"""


def append_write(filename="", text=""):
    """A function that appends to a file"""
    n_append = 0
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
        for i in text:
            n_append += 1
    return n_append
