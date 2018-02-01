class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, neighbour, weight = 0):
        self.connectedTo[neighbour] = weight

    #Getter for returning all the connections to the neighbour
    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    #Get the weight of the neighbour
    def getWeights(self, neighbour):
        return self.connectedTo[neighbour]


    #For printing out all the vertices connected to the vertex
    def __str__(self):
        return str(self.id) + 'is Connected to' + str([x.id for x in self.connectedTo])



