# coding=utf-8

import hashlib
from datetime import datetime


class Block:
    def __init__(self, data, timestamp, previous_hash=0, previous_node=None):
        self.data = data
        self.timestamp = str(timestamp)
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(data)
        self._next = previous_node

    @staticmethod
    def calc_hash(data):
        sha = hashlib.sha256()
        hash_str = data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()


class BlockChain:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += '''
             |
             v
            =========================================================================== 
            | Timestamp: {0}        
            | Data:\t\t {1}        
            | Current:\t {2}        
            | Previous:\t {3}        
            ===========================================================================
            '''.format(
                cur_head.timestamp,
                str(cur_head.data),
                str(cur_head.hash),
                str(cur_head.previous_hash)
            )
            cur_head = cur_head._next
        return out_string

    def append(self, value, timestamp):
        if self.head is None:
            self.head = Block(value, timestamp)
            return
        else:
            self.head = Block(value, timestamp, self.head.hash, self.head)
            return

    def build_blockchain_from_list(self, a_list):
        for item in a_list:
            self.append(item, datetime.now())


# Test: Chain of 6
print("Test: Chain of 6")
block_chain = BlockChain()
chain = ["Bobs Burgers", "Big Burgers", "Boy Burgers", "Turkey Burgers",
           "Vegi Burgers", "Nan Burgers"]
block_chain.build_blockchain_from_list(chain)

print(block_chain)
# Should print a formatted version of the existing blockchain


# Test: Chain of 1
print("Test: Chain of 1")
block_chain_1 = BlockChain()
chain_1 = ["Bobs Burgers"]
block_chain_1.build_blockchain_from_list(chain_1)

print(block_chain_1)
# Should print a formatted version of the existing blockchain, one item


# Test: Empty Chain
print("Test: Empty Chain")
block_chain_0 = BlockChain()
chain_0 = []
block_chain_0.build_blockchain_from_list(chain_0)

print(block_chain_0)
# Should print a formatted version of the existing blockchain, an empty link
