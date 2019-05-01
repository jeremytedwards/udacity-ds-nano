# coding=utf-8
def smallest_positive_generator(in_list):
    # TODO: Define a control structure that finds the smallest positive
    # number in in_list and returns the correct smallest number.

    return min(i for i in in_list if i > 0)


# Test cases

print(smallest_positive_generator([4, -6, 7, 2, -4, 10]))
# Correct output: 2

print(smallest_positive_generator([.2, 5, 3, -.1, 7, 7, 6]))
# Correct output: 0.2


def smallest_positive(in_list):
    # TODO: Define a control structure that finds the smallest positive
    # number in in_list and returns the correct smallest number.
    for i in in_list:
        if i < 0:
            in_list.remove(i)
    return min(in_list)



# Test cases

print(smallest_positive([4, -6, 7, 2, -4, 10]))
# Correct output: 2

print(smallest_positive([.2, 5, 3, -.1, 7, 7, 6]))
# Correct output: 0.2

def smallest_positive_2(in_list):
    # TODO: Define a control structure that finds the smallest positive
    # number in in_list and returns the correct smallest number.
    lowest = None
    for i in in_list:
        if i > 0:
            if lowest is None or i < lowest:
                lowest = i

    return lowest



# Test cases

print(smallest_positive_2([4, -6, 7, 2, -4, 10]))
# Correct output: 2

print(smallest_positive_2([.2, 5, 3, -.1, 7, 7, 6]))
# Correct output: 0.2