#!/usr/bin/python3
"""
    Module append a string at the end of a text file

    version utf-8 type
"""


def append_write(filename='', text=''):
    """appending to the end of file"""
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)