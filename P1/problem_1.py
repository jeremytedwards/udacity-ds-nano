# coding=utf-8

import collections


class LruCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def get(self, key):
        try:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        except KeyError:
            return -1

    def set(self, key, value):
        try:
            self.cache.pop(key)
        except KeyError:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)
        self.cache[key] = value


our_cache_t1 = LruCache(2)
our_cache_t1.set(1, 1)
our_cache_t1.set(2, 2)

print(our_cache_t1.get(1))
# returns 1
print(our_cache_t1.get(2))
# returns 2
print(our_cache_t1.get(3), "\n")
# return -1


our_cache_t2 = LruCache(2)
our_cache_t2.set(1, 1)
our_cache_t2.set(2, 2)
our_cache_t2.set(3, 3)

print(our_cache_t2.get(1))
# return -1
print(our_cache_t2.get(2))
# return 2
print(our_cache_t2.get(3), "\n")
# return 3

our_cache_t2.set(1, 3)

print(our_cache_t2.get(1))
# returns 3
print(our_cache_t2.get(2))
# returns -1
print(our_cache_t2.get(3), "\n")
# return 3


our_cache_t4 = LruCache(2)
our_cache_t4.set(1, 3)
our_cache_t4.set(2, 4)
our_cache_t4.set(2, 5)
our_cache_t4.set(2, 6)

print(our_cache_t4.get(2))
# returns 6
