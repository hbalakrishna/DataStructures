class Node:
    def __init__(self, data):
        self.initData = data
        self.next = None

    def getData(self):
        return self.initData

    def getNext(self):
        return self.next

    def setData(self, newData):
        self.data = newData

    def setNext(self, newnxt):
        self.next = newnxt

class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, data):
        temp = Node(data)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current!=None:
            count += 1
            current = current.getNext()
        return count


    def search(self, item):
        current = self.head
        found = False
        while current!=None and not found:
            if current.getData() == item:
                found = True
            else:
                current.getNext()

        return found

    def remove(self, item):
        current = self.head
        previous = head
        found = False

        while not found and current!=None:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())




