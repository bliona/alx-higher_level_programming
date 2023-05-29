#!/usr/bin/python3

def safe_print_list(my_list=[], a=0):
    """Print a elememts of a list.

    Args:
        my_list (list): The list to print elements from.
        a (int): The number of elements of my_list to print.

    Returns:
        The number of elements printed.
    """
    ret = 0
    for x in range(a):
        try:
            print("{}".format(my_list[x]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return (ret)
