#!/usr/bin/python3
"""
Function that finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    finds num that's greater than both left and right
    """
    if len(list_of_integers) == 0:
        return None

    int_list = list_of_integers
    beg = 0
    end = len(int_list)-1

    if int_list[beg] > int_list[beg+1]:
        return int_list[beg]
    if int_list[end] > int_list[end-1]:
        return int_list[end]

    mid = (beg+end)//2
    if int_list[mid-1] < int_list[mid] and int_list[mid+1] < int_list[mid]:
        return int_list[mid]
    if int_list[mid] < int_list[mid-1]:
        return find_peak(int_list[beg:mid+1])
    elif int_list[mid] < int_list[mid+1]:
        return find_peak(int_list[mid:end+1])
    else:
        return int_list[beg]
