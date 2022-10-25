#!/usr/bin/python3
"""
    Module writes string to a text file

    version: utf-8 type
"""


def write_file(filename="", text=""):
    """Return filename by appending text to the end of filename
        Args:
            filename: file
            text: text to be appended
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
