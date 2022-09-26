#!/usr/bin/python3
def no_c(my_string):
    new_string = list(my_string)
    for i in new_string:
        if i == 'c':
            new_string.remove('c')
        if i == 'C':
            new_string.remove('C')
    my_string = ''.join(new_string)
    return my_string
