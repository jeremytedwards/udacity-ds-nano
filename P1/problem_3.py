# coding=utf-8

import sys
from collections import Counter


class Node(object):
    """Create Node class."""

    def __init__(self, tup=(None, 0)):
        """Init Node."""
        self._left = None
        self._right = None
        self.data = tup[0]
        self.code = ""
        self.freq = tup[1]

    def __repr__(self):
        """Return a string which when eval'ed will rebuild tree"""
        return '{}({}:{}:{}, {}, {})'.format(
            self.__class__.__name__,
            repr(self.data),
            repr(self.freq),
            repr(self.code),
            repr(self._left) if self._left else None,
            repr(self._right) if self._right else None) \
            .replace(', None, None)', ')') \
            .replace(', None)', ')')

    def set_left(self, l):
        self._left = l

    def set_right(self, r):
        self._right = r

    def set_freq(self, f):
        self.freq = f

    def pre_order(self, code=""):
        """Returns the data and freq of all nodes in pre-order
        (me, all left, all right)"""
        # Return me
        self.code = code
        yield self.data, self.freq, self.code
        # Return all the _left items
        if self._left:
            code += "0"
            for d, f, c in self._left.pre_order(code):
                yield d, f, c
        # Return all the _right
        if self._right:
            code += "1"
            for d, f, c in self._right.pre_order(code):
                yield d, f, c


def huffman_sub(left_node, right_node):
    top = Node()
    top._left = left_node
    top._right = right_node
    top.freq = top._left.freq + top._right.freq
    return top


def huffman_encoding(data):
    """
    Takes a string and counts the frequency of the characters, converts those into
    a Trie with weight and combines Trie's smallest to largest.
    :param data:
    :return: a Trie
    """
    ordered_data = Counter(data).most_common()
    hm = []

    # First pass create the leaves
    while ordered_data:
        sub_left_node = Node(ordered_data.pop())
        if ordered_data:
            sub_right_node = Node(ordered_data.pop())
            hm.append(huffman_sub(sub_left_node, sub_right_node))
        else:
            hm.append(sub_left_node)

    # compare the frequencies and combine the leaves
    while len(hm) > 1:
        sorted(hm, key=lambda item: item.freq)
        if hm[0].freq <= hm[1].freq:
            hm.append(huffman_sub(hm.pop(), hm.pop()))
        else:
            hm.append(huffman_sub(hm.pop(1), hm.pop()))

    od = [c for d, f, c in hm[0].pre_order() if c is not ""]

    return od, hm[0]


def huffman_decoding(hm_tree):
    decoded = ""
    decoded_list = [d*int(f) for d, f, c in hm_tree.pre_order() if d is not None]
    for i in decoded_list:
        decoded += i
    return decoded


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"
    # a_great_sentence = "cccabbdddd"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    ed_list, hm_tree = huffman_encoding(a_great_sentence)

    encoded_data = ""
    for i in ed_list:
        encoded_data += i

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    # used for testing
    # print(ed_list)
    # print(hm_tree)
    # print("\n")

    decoded_data = huffman_decoding(hm_tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))
