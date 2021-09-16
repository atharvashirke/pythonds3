from node import Node

class OrderedList:

    def __init__(self):
        self.head = None

    def __str__(self):
        output = []
        curr = self.head
        while curr.next != None:
            output.append(curr.data)
            curr = curr.next
        output.append(curr.data)
        return str(output)

    def is_empty(self):
        return self.head == None

    def add(self, item):
        if self.is_empty():
            self.head = Node(item, self.head)
        else:
            curr = self.head
            prev = None
            while item > curr.data:
                prev = curr
                curr = curr.next
                if curr == None:
                    break
            if prev == None:
                self.head = Node(item, self.head)
            else:
                prev.next = Node(item, curr)

    def remove(self, item):
        if self.is_empty():
            raise RuntimeError("List is empty")
        curr = self.head
        prev = None
        while curr.data != item:
            prev = curr
            curr = curr.next
            if curr == None or curr.data > item:
                raise RuntimeError("List does not contain element")
        if prev == None:
            self.head = curr.next
        else:
            prev.next = curr.next

    def search(self, item):
        if self.is_empty():
            raise RuntimeError("List is empty")
        curr = self.head
        while curr is not None:
            if curr.data == item:
                return True
            elif curr.data < item:
                curr = curr.next
            else:
                return False
        return False

    def size(self):
        if self.is_empty():
            return 0
        else:
            curr, count = self.head, 0
            while curr != None:
                curr = curr.next
                count = count + 1
            return count

    def index(self, item):
        if self.is_empty():
            raise RuntimeError("List is empty")
        curr = self.head
        index = 0
        while curr.data < item:
            curr = curr.next
            index = index + 1
        if curr.data == item:
            return index
        else:
            raise RuntimeError("Item not in list")

    def pop(self, pos=None):
        if self.is_empty():
            raise RuntimeError("List is empty")
        curr = self.head
        prev = None
        if pos == None:
            while curr.next != None:
                prev = curr
                curr = curr.next
            prev.next = None
            return curr.data
        else:
            while pos != 0:
                prev = curr
                curr = curr.next
                pos = pos - 1
            if prev == None:
                self.head = curr.next
            else:
                prev.next = curr.next
            return curr.data

def main():
    l1 = OrderedList()
    l1.add(1)
    l1.add(5)
    l1.add(3)
    l1.add(8)
    l1.add(10)
    l1.add(99)
    l1.add(0)
    print(l1.search(99))
    print(l1)

main()
