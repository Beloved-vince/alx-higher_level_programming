:set paste
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

    @property
    def size(self):
        """Gets size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets size
        :param value: value that should be set
        Args:
            value: Value that should be set
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
