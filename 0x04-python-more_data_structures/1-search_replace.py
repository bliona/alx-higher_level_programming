#!/usr/bin/python3
def search_replace(current_list, search, replace):
    new_list = list(map(lambda a: replace if a == search else a, current_list))
    return (new_list)
