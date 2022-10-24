#!/usr/bin/python3
"""
    Module 0-lookup

    contain method that return list of object attribute and methods
"""
def lookup(obj):
    """Return the dictionary of an object"""
    return dir(obj)
