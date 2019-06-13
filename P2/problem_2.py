import math


def rotated_array_search(input_list, number, lowBounds=0, highBounds=None):
    if highBounds == None:
        highBounds = len(input_list) - 1
    if highBounds < lowBounds:
        return -1
    middle = math.floor((lowBounds + highBounds) / 2)
    if input_list[middle] == number:
        return middle
    if input_list[highBounds] == number:
        return highBounds
    if input_list[lowBounds] == number:
        return lowBounds

    if input_list[middle] > number:
        return rotated_array_search(input_list, number, middle + 1, highBounds)

    return rotated_array_search(input_list, number, lowBounds, middle - 1)


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

print(rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 1))
# Should print 5

print(rotated_array_search([4], 1))
# Should print -1

print(rotated_array_search([4, 0, 0, 0, 0, 0, 0], 1))
# Should print -1

print(rotated_array_search([], 1))
# Should print -1

print(rotated_array_search([1, 2, 3, 4, 5], 1))
# Should print 0