#!/usr/bin/python3
"""
Module 2: get the area of a rectangle
By multiplying width and height
"""


class Rectangle:
    """
    Args: two private args
    one public attribute
        width: width(int)
        height: height(int)
    Function: Methods of operation
        init: __init__(self)
        width: width(self)
        width: width(self, value)
        height: height(self, value)
    """
    def __init__(self, __width, __height):
        self.height = __height
        self.width = __width

    @property
    def width(self):
        """Getter: return width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Check for error value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """return height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Check for value error"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Returns the area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns perimeter of rectangle"""
        if self.__width == 0:
            return 0
        if self.__height == 0:
            return 0
        else:
            res = self.__width + self.__height
            return res*2
