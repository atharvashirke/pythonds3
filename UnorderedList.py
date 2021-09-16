from node import Node

class UnorderedList:
    """An unordered list represented with Nodes"""

    def __init__(self):
        self.head = None

    def add(self, item):
        self.head = Node(item, self.head)

    def size(self, item):
        current = self.head
        count = 0
        while current.next != None:
            current = current.next
            count = count + 1
        return count

    def remove(self, item):
        current = self.head
        while current.data != item and current.next != None:
            prev = current
            current = current.next
        if current.data == item:
            prev.next = current.next
        else:
            raise RuntimeError(f"Item {item} not in list")

    def search(self, item):
        current = self.head
        while current.data != item and current.next != None:
            current = current.next
        return curent.data == item

    def is_empty(self):
        return self.head == None

    def append(self, item):
        current = self.head
        while current.next != None:
            current = current.next
        current.next = Node(item)

    def index(self, item):
        current = self.head
        index = 0
        while current.data != item and current.next != None:
            current = current.next
            index = index + 1
        if current.data == item:
            return index
        else:
            raise RuntimeError(f"Item {item} not in list")

    def insert(self, pos, item):
        current = self.head
        index = 0
        while index != pos:
            if current.next != None:
                prev = current
                current = current.next
                index = index + 1
            else:
                raise RuntimeError("Index beyond list length")
        prev.next = Node(item, current)

    def pop(self):
        current = self.head
        while current.next != None:
            current = current.next
        return current.data

    def pop(self, pos):
        current = self.head
        index = 0
        while index != pos:
            if current.next != None:
                prev = current
                current = current.next
                index = index + 1
            else:
                raise RuntimeError("Index beyond list length")
        prev.next = current.next
        return current.data
