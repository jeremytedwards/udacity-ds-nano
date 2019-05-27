# coding=utf-8

import hashlib
from datetime import datetime


class Block:
    def __init__(self, data, timestamp, previous_hash):
        self.data = data
        self.timestamp = str(timestamp)
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = "We are going to encode this string of data!".encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()


class BlockChain:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.data) + " -> "
            cur_head = cur_head.data
        return out_string

    def append(self, value, timestamp, previous_hash=0):
        if self.head is None:
            self.head = Block(value, timestamp, previous_hash)
            return

        block = self.head
        while block.hash:
            block = block.hash

        block.next = Block(value)

    def size(self):
        size = 0
        block = self.head
        while block:
            size += 1
            block = block.hash

        return size


block_chain_1 = BlockChain()


chain_1 = ["Bobs Burgers", "Big Burgers", "Boy Burgers", "Turkey Burgers",
           "Vegi Burgers", "Nan Burgers"]


for i in chain_1:
    block_chain_1.append(i, datetime.now(), block_chain_1.__hash__())
#
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
