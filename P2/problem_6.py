# coding=utf-8

import random


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    result = (None, None)

    if len(ints) >= 1:
        result = (ints[0], ints[0])  # only one item == it's the biggest and smallest
        if len(ints) > 1:
            for item in ints[1::]:
                if result[1] < item:  # check the max
                    result = (result[0], item)
                if result[0] > item:  # check the min
                    result = (item, result[1])

    return result


# Example Test Case of Ten Integers

random_list = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(random_list)

print("Pass" if ((0, 9) == get_min_max(random_list)) else "Fail")
