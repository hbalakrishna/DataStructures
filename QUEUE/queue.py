class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, itm):
        self.items.insert(0, itm)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


q = Queue()

q.enqueue(1)
q.enqueue(2)
print("Size of the queue is {0}".format(q.size()))
print("Dequeue is {0}".format(q.dequeue()))
print("Dequeue is {0}".format(q.dequeue()))