"""
A linked list is a linear data structure where elements are stored in nodes.
Each node contains a data field and a reference (link) to the next node in the sequence.
Here's a simple implementation of a singly linked list in Python:
"""


# pylint: disable=too-few-public-methods
class Node:
    """
    Represents a node in a linked list
    """

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """
    Represents a linked list
    """

    def __init__(self, value):
        """
        Initialize the LinkedList with a value.
        Args:
            value: The value to be stored in the first node.
        Returns:
            None
        """
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        """
        Print all the values in the linked list.
        Args:
            None
        Returns:
            None
        """
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        """
        Add a node to the end of the linked list.
        Args:
            value: The value to be stored in the new node.
        Returns:
            True if the operation is successful.
        """
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        """
        Remove the last node from the linked list.
        Args:
            None
        Returns:
            Node: The removed node, or None if the list is empty.
        """
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        """
        Add a node to the beginning of the linked list.
        Args:
            value: The value to be stored in the new node.
        Returns:
            True if the operation is successful.
        """
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        """
        Remove the first node from the linked list.
        Args:
            None
        Returns:
            Node: The removed node, or None if the list is empty.
        """
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        """
        Get the node at a specific index.
        Args:
            index: The index of the node to retrieve.
        Returns:
            Node: The node at the specified index, or None if the index is out of bounds.
        """
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        """
        Set the value of a node at a specific index.
        Args:
            index: The index of the node to update.
            value: The new value to set.
        Returns:
            True if the operation is successful, False otherwise.
        """
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        """
        Insert a new node with the given value at the specified index.
        Args:
            index: The index at which to insert the new node.
            value: The value to be stored in the new node.
        Returns:
            True if the operation is successful, False otherwise.
        """
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        """
        Remove the node at a specific index.
        Args:
            index: The index of the node to remove.
        Returns:
            Node: The removed node, or None if the index is out of bounds.
        """
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        """
        Reverse the linked list.
        Args:
            None
        Returns:
            Self: The reversed linked list.
        """
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        return self
