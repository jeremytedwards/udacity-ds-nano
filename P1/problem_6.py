# coding=utf-8

import random


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, items=()):
        self.head = None
        for item in items:
            self.append(item)

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def __iter__(self):
        """
        Iterate over the values of the elements in the list
        in pop-order (first to last)
        """
        n = self.head
        while n is not None:
            yield n.value
            n = n.next

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


def union(a, b):
    """
    The union of two sets A and B is the set of elements which are in A, in B, or in both A and B
    :param a:
    :param b:
    :return: LinkedList
    """

    union_result = LinkedList()

    a = LinkedList(sorted(set(a)))
    b = LinkedList(sorted(set(b)))


    union_a_walker = a.head
    union_b_walker = b.head

    # Lists of 1 or fewer
    if union_a_walker is None:
        union_result = b.head

    if union_b_walker is None:
        union_result = a.head

    while union_a_walker.next is not None and union_b_walker.next is not None:
        # add to union
        if union_a_walker.value < union_b_walker.value:
            union_result.append(union_a_walker.value)
            union_a_walker = union_a_walker.next
        elif union_b_walker.value < union_a_walker.value:
            union_result.append(union_b_walker.value)
            union_b_walker = union_b_walker.next
        else:
            union_result.append(union_a_walker.value)
            union_a_walker = union_a_walker.next
            union_b_walker = union_b_walker.next

        # handle empty list(s)
        if union_a_walker.next is None:
            union_result.append(union_a_walker.value)  # last item
            while union_b_walker.next is not None:
                union_result.append(union_b_walker.value)
                union_b_walker = union_b_walker.next
            union_result.append(union_b_walker.value)  # last item
        if union_b_walker.next is None:
            union_result.append(union_b_walker.value)  # last item
            while union_a_walker.next is not None:
                union_result.append(union_a_walker.value)
                union_a_walker = union_a_walker.next
            union_result.append(union_a_walker.value)  # last item

    return union_result


def intersection(a, b):
    """
    The intersection of two sets A and B, denoted by A ∩ B, is the set of all objects that are members of both
    the sets A and B.
    :param a:
    :param b:
    :return:
    """
    intersection_result = LinkedList()

    a = LinkedList(sorted(set(a)))
    b = LinkedList(sorted(set(b)))

    inter_a_walker = a.head
    inter_b_walker = b.head

    while inter_a_walker.next is not None and inter_b_walker.next is not None:
        # add to intersection
        if inter_a_walker.value < inter_b_walker.value:
            inter_a_walker = inter_a_walker.next
        elif inter_b_walker.value < inter_a_walker.value:
            inter_b_walker = inter_b_walker.next
        else:
            intersection_result.append(inter_a_walker.value)
            inter_a_walker = inter_a_walker.next
            inter_b_walker = inter_b_walker.next

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
# 1 -> 2 -> 3 -> 4 -> 6 -> 7 -> 8 -> 9 -> 11 -> 21 -> 23 -> 35 -> 65 ->

print("intersection:")
print(intersection(linked_list_3, linked_list_4))
# no items intersect


# Test case 3

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_5 = [101] + [i + 1 for i in range(random.randint(1, 100))]
# element_5.append(101)

element_6 = [101]

for i in element_5:
    linked_list_5.append(i)

for i in element_6:
    linked_list_6.append(i)

print("union:")
hold = union(linked_list_5, linked_list_6)
print(union(linked_list_5, linked_list_6))
# 33 ...

print("intersection:")
print(intersection(linked_list_5, linked_list_6))
# 33

