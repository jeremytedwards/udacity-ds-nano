# coding=utf-8


class LruCache(object):
    def __init__(self, capacity=1024):
        self._size = capacity
        self._storage = [[] for _ in range(capacity)]

    def get(self, key):
        """returns the value stored with the given key"""
        bucket = self._storage[self._hash(key)]
        for item in bucket:
            if item[0] == key:
                # if the item is already in the bucket do nothing
                return item[1]
            else:
                return -1

    def set(self, key, val):
        """stores the given val using the given key"""
        bucket = self._storage[self._hash(key)]
        key_found = False
        for index, (t_key, t_val) in enumerate(bucket):
            if key == t_key:
                # if the key is already in the bucket update
                self._storage[self._hash(key)][index] = (key, val)
                key_found = True
                break
        if key_found is False:
            self._storage[self._hash(key)].append((key, val))

    def _hash(self, key):
        """
        ::Additive Hash::
        Hashes the key provided (note that this is an internal api)
        This method prefers a string or integer.
        """
        return sum([ord(c) for c in str(key)]) % self._size


our_cache = LruCache(2)

our_cache.set(1, 1)
our_cache.set(2, 2)

print(our_cache.get(1))
# returns 1

print(our_cache.get(2))
# returns 2

print(our_cache.get(3))
# return -1
