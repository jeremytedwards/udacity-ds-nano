# coding=utf-8

from collections import Counter


class Node(object):
    """Create Node class."""

    def __init__(self, alpha=None):
        """Init Node."""
        self._left = None
        self._right = None
        # self._parent = None
        self.data = alpha
        self.code = ""
        self.freq = 0

    def set_left(self, l):
        # self.code = "0" + self.code
        self._left = l
        # self._left.code = "0" + self._left.code

    def set_right(self, r):
        # self.code = "1" + self.code
        self._right = r
        # self._right.code = "1" + self._right.code

    def set_freq(self, f):
        self.freq = f

    def set_data(self, d):
        self.data = d

    def get_freq(self):
        return self.freq

    def get_data(self):
        return self.data

    # def get_code(self):
    #     return self.code

    def pre_order(self):
        """Returns the data and freq of all nodes in pre-order
        (me, all left, all right)"""
        # Return me
        yield self.data, self.freq
        # Return all the _left items
        if self._left:
            for d, f in self._left.pre_order():
                yield d, f
        # Return all the _right
        if self._right:
            for d, f in self._right.pre_order():
                yield d, f

    # def display(self):
    #     """Print the contents of the list"""
    #     print("({})".format(
    #         ", ".join(map(repr, self)) +
    #         ("," if self.length == 1 else "")
    #     ))


class Trie(object):
    def __init__(self, node=Node()):
        self.head = node

    def left_join(self, trie):
        new_head = Node()
        new_head.set_freq(self.head.freq + trie.head.freq)
        new_head.set_left(trie)
        new_head.set_right(self.head)
        self.head = new_head

    def pre_order_items(self):
        result = self.head.pre_order()
        return result




def huffman_encoding(data):
    """
    Takes a string and counts the frequency of the characters, converts those into
    a Trie with weight and combines Trie's smallest to largest.
    :param data:
    :return: a Trie
    """
    ordered_data = Counter(data).most_common()

    hm = Trie()

    while ordered_data:
        top = Node()
        top._left = Node(ordered_data.pop())
        top._right = Node(ordered_data.pop())
        top._left.code = "0" + top._left.code
        top._right.code = "1" + top._right.code
        top.freq = top._left.data[1] + top._right.data[1]
        left_trie = Trie(top)
        hm.left_join(left_trie)

    return hm


def huffman_decoding(tree):
    decoded_data = [(d, f) for d, f in tree.pre_order_items()]

    return decoded_data


tree = huffman_encoding("The bird is the word")

print(tree)

# if __name__ == "__main__":
#     codes = {}
#
#     a_great_sentence = "The bird is the word"
#
#     print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
#     print("The content of the data is: {}\n".format(a_great_sentence))
#
#     encoded_data, tree = huffman_encoding(a_great_sentence)
#
#     print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
#     print("The content of the encoded data is: {}\n".format(encoded_data))
#
#     decoded_data = huffman_decoding(encoded_data, tree)
#
#     print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
#     print("The content of the encoded data is: {}\n".format(decoded_data))


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
