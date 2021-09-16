class Node:
    """Object representing a Node in a linked list"""

    def __init__(self, data=None, next=None):
        """Create a new Node"""
        self._data = data
        self._next = next

    def __str___(self):
        """Return string representation of Node"""
        return f"Node({self._data}, {self._next})"

    def get_data(self):
        """Returns Node data"""
        return self._data

    def set_data(self, new_data):
        """Set Node data"""
        self._data = new_data

    data = property(get_data, set_data)

    def get_next(self):
        """Return next node"""
        return self._next

    def set_next(self, next_node):
        """Set next node"""
        self._next = next_node

    next = property(get_next, set_next)
