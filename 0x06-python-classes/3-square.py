#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Square file
"""


class Square:
    """square class"""
    pass

    def __init__(self, size=0):
    """
    init method
    :param size: size of the Square
    Args:
    size: size of the Square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    self.__size = size
                                             
    def area(self):
        """returns the size square"""
        return self.__size ** 2
