#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_item = []
    if search in my_list:
        for i in range(len(my_list)):
            if my_list[i-1] == search:
                my_list.insert(i-1, replace)
                my_list.remove(search)
            new_item.append(my_list[i])
    return new_item
