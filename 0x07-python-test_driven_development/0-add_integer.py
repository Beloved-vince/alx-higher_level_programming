#/usr/bin/python3
"""
    A function that add two integer and return the sum
    Also check the value if they are ValueError free
    Also accept two values of types int or float and cast them into int

"""


def add_integer(a, b=98):
    """
        Get the value of both a and b
        returns a + b as integer
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
