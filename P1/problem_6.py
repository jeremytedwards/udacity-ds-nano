# coding=utf-8

import random


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    def bubble_sort(self):
        end = None
        while end != self.head:
            p = self.head
            while p.next != end:
                q = p.next
                if p.value > q.value:
                    p.value, q.value = q.value, p.value
                p = p.next
            end = p


def union(l1, l2):
    l1.bubble_sort()
    l2.bubble_sort()
    union_result = LinkedList()
    l1_walker = l1.head
    l2_walker = l2.head

    while l1_walker.next is not None and l2_walker.next is not None:
        # skip duplicates
        while l1_walker.value == l1_walker.next.value:
            l1_walker = l1_walker.next
        while l2_walker.value == l2_walker.next.value:
            l2_walker = l2_walker.next

        # add to union
        if l1_walker.value < l2_walker.value:
            union_result.append(l1_walker.value)
            l1_walker = l1_walker.next
        elif l2_walker.value < l1_walker.value:
            union_result.append(l2_walker.value)
            l2_walker = l2_walker.next
        else:
            union_result.append(l1_walker.value)
            l1_walker = l1_walker.next
            l2_walker = l2_walker.next

        # handle empty list(s)
        if l1_walker.next is None:
            union_result.append(l1_walker.value)  # last item
            while l2_walker.next is not None:
                union_result.append(l2_walker.value)
                l2_walker = l2_walker.next
            union_result.append(l2_walker.value)  # last item
        if l2_walker.next is None:
            union_result.append(l2_walker.value)  # last item
            while l1_walker.next is not None:
                union_result.append(l1_walker.value)
                l1_walker = l1_walker.next
            union_result.append(l1_walker.value)  # last item

    return union_result


def intersection(l1, l2):
    l1.bubble_sort()
    l2.bubble_sort()
    intersection_result = LinkedList()
    l1_walker = l1.head
    l2_walker = l2.head

    while l1_walker.next is not None and l2_walker.next is not None:
        # skip duplicates
        while l1_walker.value == l1_walker.next.value:
            l1_walker = l1_walker.next
        while l2_walker.value == l2_walker.next.value:
            l2_walker = l2_walker.next

        # add to intersection
        if l1_walker.value < l2_walker.value:
            l1_walker = l1_walker.next
        elif l2_walker.value < l1_walker.value:
            l2_walker = l2_walker.next
        else:
            intersection_result.append(l1_walker.value)
            l1_walker= l1_walker.next
            l2_walker = l2_walker.next

    return intersection_result


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print("union:")
print(union(linked_list_1, linked_list_2))
# 1 -> 2 -> 3 -> 4 -> 6 -> 9 -> 11 -> 21 -> 32 -> 35 -> 65 ->

print("intersection:")
print(intersection(linked_list_1, linked_list_2))
# 4 -> 6 -> 21 ->


# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_3 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_4 = [1, 7, 8, 9, 11, 21, 1]

for i in element_3:
    linked_list_3.append(i)

for i in element_4:
    linked_list_4.append(i)

print("union:")
print(union(linked_list_3, linked_list_4))
# 1 -> 2 -> 3 -> 4 -> 6 -> 9 -> 11 -> 21 -> 32 -> 35 -> 65 ->

print("intersection:")
print(intersection(linked_list_3, linked_list_4))
# no items intersect


# # Test case 3
#
# linked_list_5 = LinkedList()
# linked_list_6 = LinkedList()
#
# element_5 = [i + 1 for i in range(random.randint(1, 10000))]
# element_5.append(33)
#
# element_6 = [33]
#
# for i in element_5:
#     linked_list_5.append(i)
#
# for i in element_6:
#     linked_list_6.append(i)
#
# print("union:")
# print(union(linked_list_5, linked_list_6))
# # 33 ...
#
# print("intersection:")
# print(intersection(linked_list_5, linked_list_6))
# # 33

