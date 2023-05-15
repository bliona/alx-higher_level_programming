#!/usr/bin/python3
def delete_at(my_list=[], abc=0):
    if abc < 0 or abc > len(my_list) - 1:
        return my_list
    else:
        del my_list[abc]
    return my_list
