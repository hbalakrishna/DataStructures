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


class OrderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while current!=None:
            count += 1
            current = current.getNext()

        return count


    def search(self, item):
        current = self.head
        stop = False
        found = False

        # while current != None and not found and not stop:
        while current != None and not stop and not found:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()
        return found

    def add(self, item):
        current = self.head
        previous = None
        stop = False

        while current!=None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        #Create a node
        node = Node(item)
        if previous == None:
            node.setNext(self.head)
            self.head = node

        else:
            previous.setNext(node)
            node.setNext(current)



mylist = OrderedList()
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print(mylist.size())
print(mylist.search(93))
print(mylist.search(100))



