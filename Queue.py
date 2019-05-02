# coding=utf-8


class Queue:
    def __init__(self):
        self._list = []
        self._len = 0

    def size(self):
        return self._len

    def enqueue(self, item):
        self._len += 1
        self._list.append(item)

    def dequeue(self):
        self._len -= 1
        return self._list.pop(0)
