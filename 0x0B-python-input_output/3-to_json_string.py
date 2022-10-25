#!/usr/bin/python3
import json
"""
    Module: JSON representation of an object

    return json representation of string
"""


def to_json_string(obj):
    """Json format
        Args: 
            obj: json return json string format
            json: string rep format
    """
    return json.dumps(obj)
