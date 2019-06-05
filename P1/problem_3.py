# coding=utf-8

from collections import Counter
import sys


class Node(object):
    """Create Node class."""

    def __init__(self, alpha=(None, 0)):
        """Init Node."""
        self._left = None
        self._right = None
        self.data = alpha[0]
        self.code = ""
        self.freq = alpha[1]

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

    # def set_data(self, d):
    #     self.data = d
    #
    # def get_freq(self):
    #     return self.freq
    #
    # def get_data(self):
    #     return self.data

    # def get_code(self):
    #     return self.code

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


    # # Recursively walk the tree down to the leaves,
    # # assigning a code value to each symbol
    # def walk_tree(node, prefix="", code={}):
    #     if isinstance(node[1].left[1], HuffmanNode):
    #         walk_tree(node[1].left,prefix+"0", code)
    #     else:
    #         code[node[1].left[1]]=prefix+"0"
    #     if isinstance(node[1].right[1],HuffmanNode):
    #         walk_tree(node[1].right,prefix+"1", code)
    #     else:
    #         code[node[1].right[1]]=prefix+"1"
    #     return(code)


class Trie(object):
    def __init__(self, node=Node()):
        self.head = node

    def left_join(self, trie):
        new_head = Node()
        new_head.set_freq(self.head.freq + trie.head.freq)
        new_head.set_left(trie)
        new_head.set_right(self.head)
        self.head = new_head

    def pre_order(self, code=""):
        result = self.head.pre_order(code)
        return result

    # def gen_trie_from_ord_list(self, ordered_list):
    #     """
    #     Given an ordered list this function will create a tree from those values
    #     :param ordered_list:
    #     :return: a Trie
    #     """
    #     if ordered_list:
    #         half = len(ordered_list) // 2
    #
    #         # yield the middle item round down
    #         yield ordered_list[half]
    #
    #         # yield the middle of the left
    #         for left in self.gen_trie_from_ord_list(ordered_list[:half]):
    #             yield left
    #
    #         # yield the middle of the right
    #         for right in self.gen_trie_from_ord_list(ordered_list[half + 1:]):
    #             yield right


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

    # No nodes
    hm = Trie()

    # One node
    if len(ordered_data) == 1:
        hm.head = Node(ordered_data.pop())

    # More than one node
    while ordered_data:
        sub_node = Node(ordered_data.pop())

        if len(ordered_data) == 0:
            hm.head = huffman_sub(hm.head, sub_node)
            break

        if len(ordered_data) == 1:
            hm.head = huffman_sub(sub_node, Node(ordered_data.pop()))

        if len(ordered_data) > 0:
            sub_right_node = Node(ordered_data.pop())

            if hm.head.freq >= sub_right_node.freq:
                new_right = huffman_sub(sub_right_node, Node(ordered_data.pop()))
                hm.head = huffman_sub(hm.head, new_right)

            else:
                hm.head = huffman_sub(sub_node, sub_right_node)

    return ordered_data, hm

    # def create_tree(frequencies):
    #     p = queue.PriorityQueue()
    #     for value in frequencies:  # 1. Create a leaf node for each symbol
    #         p.put(value)  # and add it to the priority queue
    #     while p.qsize() > 1:  # 2. While there is more than one node
    #         l, r = p.get(), p.get()  # 2a. remove two highest nodes
    #         node = HuffmanNode(l, r)  # 2b. create internal node with children
    #         p.put((l[0] + r[0], node))  # 2c. add new node to queue
    #     return p.get()  # 3. tree is complete - return root node


def huffman_decoding(encoded_data, hm_tree):
    decoded_data = [(d, f, c) for d, f, c in hm_tree.pre_order()]

    return decoded_data


if __name__ == "__main__":
    codes = {}

    # a_great_sentence = "The bird is the word"
    a_great_sentence = "cccabbdddd"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, hm_tree = huffman_encoding(a_great_sentence)

    # print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, hm_tree)

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
