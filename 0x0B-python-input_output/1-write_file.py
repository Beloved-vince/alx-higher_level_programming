#!/usr/bin/python3
"""
    Module writes string to a text file

    version: utf-8 type
"""


def write_file(filename="", text=""):
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
