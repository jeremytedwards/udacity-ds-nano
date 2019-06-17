# coding=utf-8


def rotated_array_search(input_list, number, idx=0):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    mid = len(input_list)//2
    if mid == 0:
        return -1

    if input_list[idx] == number:
        return idx
    elif input_list[idx] > number:
        # go right
        top = input_list[mid::]
        rotated_array_search(input_list[mid::], number)
    else:
        # go left
        bottom = input_list[0:mid:]
        rotated_array_search(input_list[0:mid:], number)



# """ returns a node with the given value."""
#         if self.data == value:
#             return self
#         elif self.data > value:
#             if self._left is None:
#                 return None
#             return self._left._find_node(value)
#         else:
#             if self._right is None:
#                 return None
#             return self._right._find_node(value)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])