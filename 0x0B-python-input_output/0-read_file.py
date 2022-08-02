#!/usr/bin/python3
""" module that contains function which can read from a file """


def read_file(filename=""):
    """A function that can read from a file"""

    with open(filename, encoding="utf-8") as f:
        read = f.read()
    print(read)
