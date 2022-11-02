#!/usr/bin/python3
"""
This function get name and last name in string format only
first_name in string litera
Also last_name in string literal
"""


def say_my_name(first_name, last_name=""):
    """
    return func in string literal
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    else:
        print(f"My name is {first_name} {last_name}")
