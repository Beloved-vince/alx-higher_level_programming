#!/usr/bin/python3
"""
    Module: fucnction to read a text file
"""
def read_file(filename=''):
    with open(filename, 'r', encoding='utf-8') as f:
        f.readlines()
