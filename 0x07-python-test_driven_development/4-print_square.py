#!/usr/bin/python3
"""
This function is used for drawing the shape of a square
Return square with same width and height
"""


def print_square(size):
    """
    Args: size must be integer or float and must not be \
            less than zero. \
            size is the length of the square.
    """
    
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if type(size) is float and size < 0:
        raise TypeError('size must be an integer')
    if size  < 0:
        raise ValueError('size must be >= 0')
    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()
