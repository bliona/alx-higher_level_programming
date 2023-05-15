#!/usr/bin/python3
def new_in_list(my_list, abc, element):
    copy = my_list.copy()
    if abc < 0 or abc > len(my_list) - 1:
        return my_list.copy()
    else:
        copy[abc] = element
        return copy
