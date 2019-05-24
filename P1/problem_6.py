# coding=utf-8


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

    while l1.head.value is not None and l2.head.value is not None:
        if l1.head.value < l2.head.value:
            union_result.append(l1.head.value)
            l1 = l1.head.next
        elif l2.head.value < l1.head.value:
            union_result.append(l2.head.value)
            l2 = l2.head.next
        else:
            union_result.append(l1.head.value)
            l1 = l1.head.next
            l2 = l2.head.next

    return union_result


def intersection(l1, l2):
    l1.bubble_sort()
    l2.bubble_sort()
    intersection_result = LinkedList()

    while l1.head.value is not None and l2.head.value is not None:
        if l1.head.value < l2.head.value:
            l1 = l1.head.next
        elif l2.head.value < l1.head.value:
            l2 = l2.head.next
        else:
            intersection_result.append(l1.head.value)
            l1 = l1.head.next
            l2 = l2.head.next

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

print(union(linked_list_1, linked_list_2))
# print(intersection(linked_list_1, linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(union(linked_list_3, linked_list_4))
# print(intersection(linked_list_3, linked_list_4))