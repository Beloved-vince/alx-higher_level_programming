#/usr/bin/python3
"""
Module 1-rectange
Contains class Rectangle
with private attribute width and height
"""


class Rectangle:
    """
    Defines class Rectangle with private attributes width and height
    Args:
        width (int): width
        height (int): height
    Functions:
        __init__(self, width, height)
        width(self)
        width(self, value)
        height(self)
        height(self, value)
    """
    def __init__(self, width=0, height=0):
        """ Initializes rectangles """
        self.width = width
        self.height = height

    @property
    def width(self):
<<<<<<< HEAD
        """ Getter: returns width """
=======
        """
        Return the private __width as public
        Args: class attr
        """
>>>>>>> c3b680bb27e43996d6285b9b61e9fa42fc6735a4
        return self.__width

    @width.setter
    def width(self, value):
<<<<<<< HEAD
        """ Setter: Sets width to new value """
=======
        """
        Setter: set private width to value
        Args: class attr and return value
        """
>>>>>>> c3b680bb27e43996d6285b9b61e9fa42fc6735a4
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
<<<<<<< HEAD
        """ Getter: returns height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter: Sets height to new value"""
=======
        """
        get the private attr hieght
        Args: class attr
        """
        return self.height

    @height.setter
    def height(self, value):
        """
        Setter: Check for Error and return height to be value
        Args: check value
        """
>>>>>>> c3b680bb27e43996d6285b9b61e9fa42fc6735a4
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
<<<<<<< HEAD
            raise ValueError("height must be >= 0")
=======
            raise TypeError("height must be >= 0")
>>>>>>> c3b680bb27e43996d6285b9b61e9fa42fc6735a4
        self.__height = value
