#!/usr/bin/python3
"""
    Module: fucnction to read a text file

    Contains function that reads and prints contents from file
"""


def read_file(filename=''):
    """ Reading file in utf-8 version """
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read())
