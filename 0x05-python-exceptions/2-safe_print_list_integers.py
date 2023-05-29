#!/usr/bin/python3

def safe_print_list_integers(my_list=[], a=0):
    """Print the first a elements of a list that are integers.

    Args:
        my_list (list): The list to print elements from.
        a (int): The number of elements of my_list to print.

    Returns:
        The number of elements printed.
    """
    ret = 0
    for x in range(0, a):
        try:
            print("{:d}".format(my_list[x]), end="")
            ret += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (ret)
