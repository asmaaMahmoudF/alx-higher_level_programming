#!/usr/bin/python3
"""Node Module """


class Node:
    """class Node """

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
        return self.next_node
    
    @next_node.setter
    def next_node(self, value);
        if
             raise TypeError("next_node must be a Node object")
        self.next_node = value



    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node


class SinglyLinkedList:
    """class SinglyLinkedList"""

    def head(self):
    
    def __init__(self):
        self._head = None

    def sorted_insert(self, value):
        new_node = Node(value)
        if not self._head:
            self._head = new_node
            return
        current = self._head
        while current.next:
            current = current.next
        current.next = new_node

