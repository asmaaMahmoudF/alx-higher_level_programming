#!/usr/bin/python3
"""Node Module """


class Node:
    """class Node """

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.data = value

    @property
    def next_node(self):
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self._next_node = value

class SinglyLinkedList:
    """class SinglyLinkedList"""

    def __init__(self):
        self.head = None

    def sorted_insert(self, value):
        new_node = Node(value)
        if not self._head or self.head.data >= value:
            new_node.next_node = self.head
            self._head = new_node
        else:
            current = self._head
            while current.next and current.next.data < value:
                current = current.next
            new_node.next = current.next
            current.next = new_node
