#!/usr/bin/python3
"""
LockedClass
"""


class LockedClass:
    """
    prevent user from creating new instance attribute dynamically
    unless attribute is "first_name"
    AttributeError: 'LockedClass' object has no attribute 'last_name'
    """

    __slots__ = "first_name"
