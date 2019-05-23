# coding=utf-8

import hashlib


class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()


def calc_hash(self):
      sha = hashlib.sha256()

      hash_str = "We are going to encode this string of data!".encode('utf-8')

      sha.update(hash_str)

      return sha.hexdigest()







print(test1(None))
# Expected result of the test

print(test2(min_val))
# Expected result of the test

print(test2_5(some_value))
# Expected result of the test

print(test2_6(some_value))
# Expected result of the test

print(test3(max_val))
# Expected result of the test
