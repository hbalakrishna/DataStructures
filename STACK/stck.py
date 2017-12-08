class Stack:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return (self.items == [])

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            print("Cant pop out empty list")
        else:
            print("Poped out {0}".format(self.items.pop(0)))

    def peek(self):
        return (self.items[0])

    def size(self):
        return len(self.items)

s = Stack()
s.push(10)
s.push(20)
s.isEmpty()
print("Top element is {0}".format(s.peek()))
print("Size of the Stack is {0}".format(s.size()))
s.pop()
s.pop()
s.pop()