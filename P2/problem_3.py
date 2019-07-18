# coding=utf-8


# def _rearrange_digits(input_list):
#     """
#     Rearrange Array Elements so as to form two number such that their sum is maximum.
#     (with sorted)
#
#     Args:
#        input_list(list): Input List
#     Returns:
#        (int),(int): Two maximum sums
#     """
#     items = sorted(input_list, reverse=True)
#     big_1, big_2 = "", ""
#
#     for idx, item in enumerate(items):
#         if idx % 2 == 0:
#             big_2 += str(item)
#         else:
#             big_1 += str(item)
#
#     return int(big_2), int(big_1)


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.
    (no sorted)

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    c_il = input_list.copy()  # copy of input_list
    big_1, big_2 = "", ""

    while c_il:
        # find the max item in the list and pop it off
        item = c_il.pop(c_il.index(max(c_il)))
        if len(c_il) % 2 == 0:
            big_2 += str(item)
        else:
            big_1 += str(item)

    return int(big_2), int(big_1)


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2], [2, 1]])
test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[1, 9, 2, 8, 3, 7, 4, 6, 5], [97531, 8642]])
test_function([[1, 2, 3, 4, 5, 6, 7, 8, 9], [97531, 8642]])
