#!/usr/bin/python3
def element_at(my_list, abc):
    if abc < 0 or abc > len(my_list) - 1:
        return 'None'
    else:
        return my_list[abc]
