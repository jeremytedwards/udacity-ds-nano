# coding=utf-8

import sys
from collections import Counter


def build_tree(tuple_list):
    while len(tuple_list) > 1:
        tuple_list.sort(key=lambda tup: tup[0])  # https://docs.python.org/3/howto/sorting.html
        lowest_two = tuple_list[0:2]
        remaining_tuples = tuple_list[2:]
        freq_total = lowest_two[0][0] + lowest_two[1][0]
        tuple_list = remaining_tuples + [(freq_total, lowest_two)]

    return tuple_list[0]   # Return the single tree inside the list


def trim_tree(tree):
    # Trim the freq counters off, leaving just the letters
    p = tree[1]
    if isinstance(p, str):
        return p   # if it's a leaf return it
    else:
        return trim_tree(p[0]), trim_tree(p[1])


def assign_codes(node, pat=''):
    global codes
    hm_codes = ""
    if isinstance(node, str):
        codes[node] = pat   # A leaf. Set its code
        hm_codes += pat
    else:
        assign_codes(node[0], pat+"0")   # do left branch...
        assign_codes(node[1], pat+"1")   # then do the right branch
    return hm_codes


def build_huffman_tree(data):
    """
    Takes a string and counts the frequency of the characters, converts those into
    a Trie with weight and combines Trie's smallest to largest. Finally is sets
    the codes in the GLOBAL variable 'codes' in __main__
    :param data:
    :return: a Trie
    """
    frequency_data = Counter(data).items()

    # Reverse the (k, v) mapping
    frequency_data = [(v, k) for k, v in frequency_data]

    # build the tree for encoding
    huffman_tree = build_tree(frequency_data)
    huffman_tree = trim_tree(huffman_tree)

    # Set the codes in global variable "codes"
    hm_codes = assign_codes(huffman_tree)

    return hm_codes, huffman_tree


def huffman_encoding(data):
    tree = build_huffman_tree(data)

    global codes
    output = ""
    for ch in data:
        output += codes[ch]

    return output, tree


def huffman_decoding(data, tree):
    output = ""
    p = tree[1]
    for bit in data:
        if bit == '0':
            p = p[0]   # Go left
        else:
            p = p[1]   # Go right
        if isinstance(p, str):
            output += p   # found character, add to output
            p = tree[1]   # back to top
    return output


if __name__ == "__main__":
    codes = {}

    # a_great_sentence = "cccabbdddd"
    # a_great_sentence = "THE BIRD IS THE WORD"
    # a_great_sentence = "The bird is the word"
    # a_great_sentence = "3332114444"
    a_great_sentence = "A_DEAD_DAD_CEDED_A_BAD_BABE_A_BEADED_ABACA_BED"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, hm_tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, hm_tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the decoded data is: {}\n".format(decoded_data))
