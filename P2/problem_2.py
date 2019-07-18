# coding=utf-8


def array_search(input_list, num):
    if len(input_list) == 0:
        return None

    mid = len(input_list) // 2

    if input_list[mid] == num:
        return mid

    if mid == 0:
        return None

    elif input_list[mid] > num:
        array_search(input_list[0:mid:], num)  # go left

    else:
        array_search(input_list[mid::], num)  # go right


def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array): Input array
       number(int): Target to search for
    Returns:
       int: Index or None
    """
    # find pivot
    pivot = pivot_search(input_list)

    temp_1 = input_list[0:pivot]
    temp_2 = input_list[pivot::]
    # search left
    index = array_search(input_list[0:pivot], number)

    # if not found in left search right
    if index is None:
        index = array_search(input_list[pivot::], number)
        return index if index is None else pivot + index

    return index


def pivot_search(input_list):
    for index, element in enumerate(input_list):
        if index == len(input_list) - 1:
            return index
        if element > input_list[index + 1]:
            return index
    return None


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return None


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 6, 7, 8, 9, 10], 10])
test_function([[10, 1, 2, 3, 4, 6, 7, 8, 9], 10])

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
