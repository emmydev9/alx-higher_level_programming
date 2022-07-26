#!/usr/bin/python3
def add_integer(a, b=98):
    """Return the sum of two integers"""
    if a not isinstance(a, int) and a not isinstance(a, float):
        raise TypeError("a must be an integer")
    if b not isinstance(b, int) and b not isinstance(b, float):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return (a + b)
