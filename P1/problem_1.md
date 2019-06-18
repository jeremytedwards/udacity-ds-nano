Problem 1: LRU Cache
------------
An LRU cache is a type of cache in which we remove the least recently used entry when the cache memory reaches its 
limit. In order to accomplish this I took advantage of the properties of and ordered dictionary help track the order. 
If during a set operation we reach a key outside of our capacity we drop the oldest(first) item with popitem(last=False),
maintaining a FIFO ordering.


**OrderedDict** 
https://docs.python.org/2/library/collections.html#collections.OrderedDict

The popitem() method for ordered dictionaries returns and removes a (key, value) pair. The pairs are returned in LIFO order if last is true or FIFO order if false. 



