#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = sorted(a_dictionary)
    for i in new_dict:
        print("{}: {}".format(i, a_dictionary[i] * 2))