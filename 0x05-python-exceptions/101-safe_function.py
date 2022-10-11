#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as error_msg: 
        sys.stderr.write("Exception: " + str(error_msg) + "\n")
        return None
