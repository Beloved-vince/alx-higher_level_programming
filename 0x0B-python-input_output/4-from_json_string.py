#!/usr/bin//python3
"""
    Module return object represented by JSON strin

    return type and format
"""


import json


def from_json_string(my_str):
    """ Modules get the decoded file

        Return: json format
        
        Args: my_str data object
    """
    return json.loads(my_str)