# coding=utf-8

import sys


def huffman_encoding(data):
    encoded_data = []
    tree = []



    return encoded_data, tree


def huffman_decoding(data, tree):
    decoded_data = []

    return decoded_data


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))


# print(test1(None))
# # Expected result of the test
#
# print(test2(min_val))
# # Expected result of the test
#
# print(test2_5(some_value))
# # Expected result of the test
#
# print(test2_6(some_value))
# # Expected result of the test
#
# print(test3(max_val))
# # Expected result of the test
