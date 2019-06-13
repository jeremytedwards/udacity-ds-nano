# coding=utf-8

import math

math.sqrt(9)


def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    number = abs(number)
    bit = 1 << 62  # second to top of 16 bit is 14, 32 bit would be 1 << 30
    result = 0

    # Start with the highest power that is less than the number
    while bit > number:
        bit >>= 2

    while bit != 0:
        if number >= result + bit:
            number -= result + bit
            result = (result >> 1) + bit
        else:
            result >>= 1
        bit >>= 2

    return result


# print("\nCase (-99):" + str(math.floor(math.sqrt(99))) + " = " + str(sqrt(-99)))
# print("Pass" if (9 == sqrt(-99)) else "Fail")

print("\nCase (0): " + str(math.floor(math.sqrt(0))) + " = " + str(sqrt(0)))
print("Pass" if (0 == sqrt(0)) else "Fail")

print("\nCase (1):" + str(math.floor(math.sqrt(1))) + " = " + str(sqrt(1)))
print("Pass" if (1 == sqrt(1)) else "Fail")

print("\nCase (2):" + str(math.floor(math.sqrt(2))) + " = " + str(sqrt(2)))
print("Pass" if (1 == sqrt(2)) else "Fail")

print("\nCase (3):" + str(math.floor(math.sqrt(3))) + " = " + str(sqrt(3)))
print("Pass" if (1 == sqrt(3)) else "Fail")

print("\nCase (9):" + str(math.floor(math.sqrt(9))) + " = " + str(sqrt(9)))
print("Pass" if (3 == sqrt(9)) else "Fail")

print("\nCase (16):" + str(math.floor(math.sqrt(16))) + " = " + str(sqrt(16)))
print("Pass" if (4 == sqrt(16)) else "Fail")

print("\nCase (27):" + str(math.floor(math.sqrt(27))) + " = " + str(sqrt(27)))
print("Pass" if (5 == sqrt(27)) else "Fail")

print("\nCase (99):" + str(math.floor(math.sqrt(99))) + " = " + str(sqrt(99)))
print("Pass" if (9 == sqrt(99)) else "Fail")

print("\nCase (999):" + str(math.floor(math.sqrt(999))) + " = " + str(sqrt(999)))
print("Pass" if (31 == sqrt(999)) else "Fail")

print("\nCase (16384):" + str(math.floor(math.sqrt(16384))) + " = " + str(sqrt(16384)))
print("Pass" if (128 == sqrt(16384)) else "Fail")

print("\nCase (268435456):" + str(math.floor(math.sqrt(268435464))) + " = "
      + str(sqrt(268435456)))
print("Pass" if (16384 == sqrt(268435456)) else "Fail")

