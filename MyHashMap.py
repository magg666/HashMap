class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value

        self.next = None
        self.prev = None


class NodeLinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    def clear(self):
        self.first = self.last = None

    def append(self, node):
        if self.last:
            self.last.next = node
            node.prev = self.last
            self.last = node
        else:
            self.first = self.last = node

    def remove(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.first = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            self.last = node.prev

    def __iter__(self):
        """
        Iterate over all nodes. The __iter__ method allows you to just use a for-loop:

        for node in linked_list:
            ...
        """

        node = self.first
        while node:
            yield node
            node = node.next


class MyHashMap:
    def __init__(self):
        self.bucket_size = 16

        # List of NodeLinkedLists.
        self.elements = NodeLinkedList()

    def get_position_by_hash(self, key):
        """
        Hash means key. Find position(index) of node by key.
        If there isn't key in self.elements - position should be None.
        """
        raise NotImplementedError

    def put(self, key, value):
        """
        If the key already exists, replace the old value with the new.
        If key doesn't exist - make a new Node with the key, value parameters, then add it to the list.
        Ask yourself if adding new nodes doesn't change other attributes?
        """

        raise NotImplementedError

    def get(self, key):
        """
        Find in the list the Node element that has this key, then return its value.
        If none of the items in the list has this key, raise proper exception.
        """

        raise NotImplementedError

    def clear(self):
        """
        Make the elements array empty.
        """

        raise NotImplementedError

    def remove(self, key):
        """
        Remove node from elements by its key. Return removed value.
        If key not found - raise proper exception.
        """

        raise NotImplementedError


