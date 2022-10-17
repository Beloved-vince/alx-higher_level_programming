#!/usr/bin/python3
"""
Module 3 get rectangle by ##
Get the arguement base on the previous 
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
    perimeter: add width(int) + height(int)
    """
    def __init__(self, __width, __height):
        self.width = __width
        self.height = __height

    @property
    def width(self):
        """Returns width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Check value error"""
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
        """Check value error"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return the area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns he perimeter of a triangle"""
        if self.__width == 0:
            return 0
        elif self.__height == 0:
            return 0
        else:
            res = self.__width + self.__height
            return res * 2

        def __str__(self):
            """print rec with ##"""
            if self.__width == 0 or self.__height == 0:
                return ''
            res = "\n".join(["#" * self.width for rows in range(self.__height)])
            return res
