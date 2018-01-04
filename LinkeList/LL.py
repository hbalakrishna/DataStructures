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
