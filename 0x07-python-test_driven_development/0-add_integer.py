#!/usr/bin/python3
"""function that adds 2 integers."""


def add_integer(x, y=98):
    """Return the integer addition of x and y.

    Float arguments are typecasted to ints before addition is performed.

    Raises:
        TypeError: If either of x or y is a non-integer and non-float.
    """
    if ((not isinstance(x, int) and not isinstance(x, float))):
        raise TypeError("x must be an integer")
    if ((not isinstance(y, int) and not isinstance(y, float))):
        raise TypeError("y must be an integer")
    return (int(x) + int(y))
