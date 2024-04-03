#!/usr/bin/python3

""" Define classes for a singly-linked list """


Class Node:
    """ Represent a node in a singly-linked list """

    def __init__(self, data, next_node=None):
        """Initialize a new Node.

        Args:
            data (int): The data of the new Node.
            next_node (Node): The next node of the new Node.
        """
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self._data = data

        if not isinstance(next_node, Node) and next_node is not None:
            raise TypeError("next_node must be a Node object")
        self.next_node = next_node

    @property
    def data(self):
        """Get/set the data of the Node"""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def data(self):
        """Get/set the data of the Node"""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get/set the next_node of the Node."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represent a singly-linked list."""

    linked_list = []
    def __init__(self):
        pass

    def sorted_insert(self, value):
        new_node = Node(value)
        self.linked_list.append(Node.data)
        sorted_list = self.linked_list.sort()

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList"""
        for i in self.sorted_list:
            print(i)
