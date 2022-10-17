#!/usr/bin/python3
"""
Module class of rectangle
with private attribute
"""


class Rectangle:
    """
    Private class attributes width and height
    Args:
        width(int): width
        height(int): height
    Functions: width and height(setter)
            width and height(getter)
    """

    def __init__(self, __width=0, __height=0):
        """Initializing"""
        self.width = __width
        self.height = __height

    @property
    def width(self):
        """getter: return width(int)"""
        return self.__width

    @width.setter
    def width(self, value):
        """return: value of type int"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter: return height value of type int"""
        return self.__height

    @height.setter
    def height(self, value):
        """Returns value of type int"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__height = value
