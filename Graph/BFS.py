class Vertex:
    def __init__(self,vertex):
        self.id = vertex
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

    def __str__(self):
        return str(self.id)+ 'is connected to ' +str([x for x in self.connectedTo])

class Graph:

    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex

        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def addEdge(self,frm,to,weight=0):
        if frm not in self.vertList:
            nv = self.addVertex(frm)
        if to not in self.vertList:
            nv = self.addVertex(to)

        #Add an edge from the source vertex to the destinatio vertex
        self.vertList[frm].addNeighbor(to,weight)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())


    def __contains__(self, n):
        return n in self.vertList

g = Graph()
for i in range(6):
    g.addVertex(i)

g.addEdge(0,2,4)

for vtx in g:
    print(vtx)
    print(vtx.getConnections())


