#!/usr/bin/python3
"""
    Setting and getting a private attribute
    Retrieving privates attribute
"""


class Rectangle:
    """
    Args: width and height
    func: width, height
    """
    def __init__(self, __width=0, __height=0):
        self.width = __width
        self.height = __height

    @property
    def width(self):
        """
        Return the private __width as public
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter: set private width to value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        get the private attr hieght
        """
        return self.height

    @height.setter
    def height(self, value):
        """
        Setter: Check for Error and return height to be value
        """
        if not isinstance(value, int):
            raise TypeError("height must be integer")
        if value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value
