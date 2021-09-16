class Stack:

    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def push(self, new_item):
        self.items.append(new_item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

def rev_string(my_str):
    c1 = Stack()
    output = []
    for char in my_str:
        c1.push(char)
    while not c1.is_empty():
        output.append(c1.pop())
    return ''.join(output)

def main():
    message = "atharva"
    print(rev_string(message))

if __name__ == "__main__":
    main()
