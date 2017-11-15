class Vertex:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.minDistance = -1
        self.previousVertex = None
        self.edges = []

    def addEdge(self, edge):
        self.edges.append(edge)


class Edge:
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight


class Dijkstra:
    def __init__(self, vertexes):
        self.vertexes = vertexes

    def resetDijkstra(self):
        for vertex in self.vertexes:
            vertex.minDistance = float('Inf')
            vertex.previousVertex = None

    def computePath(self, sourceId):
        self.resetDijkstra()

    def getShortestPathTo(self, targetId):
        pass

    def createGraph(self, vertexes, edgesToVertexes):
        pass

    def getVertexes(self):
        return self.vertexes


def runTests():
    pass


runTests()
