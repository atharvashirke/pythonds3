class Deque:
    """List implementation of Deque data structure"""

    def __init__(self):
        """Create new deque"""
        self.items = []

    def __str__(self):
        """Return String representation of deque"""
        return str(self.items)

    def add_front(self, item):
        """Add item to front of deque"""
        self.items.insert(0, item)

    def add_rear(self, item):
        """Add item to rear of deque"""
        self.items.append(item)

    def remove_front(self):
        """Remove item from front of deque"""
        return self.items.pop(0)

    def remove_rear(self):
        """Remove item from rear of deque"""
        return self.items.pop()

    def is_empty(self):
        """Check if deque is empty. Return Boolean"""
        return len(self.items) == 0

    def size(self):
        """Return number of items in deque"""
        return len(self.items)
