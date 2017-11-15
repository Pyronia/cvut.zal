class Vertex:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.minDistance = float('Inf')
        self.previousVertex = None
        self.edges = []

    def addEdge(self, edge):
        self.edges.append(edge)


class Edge:
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight


class Node:
    def __init__(self, vertex, prevNode=None, nextNode=None):
        self.prevNode = prevNode
        self.nextNode = nextNode
        self.vertex = vertex


class Fifo:
    def __init__(self):
        self.head = None
        self.tail = None

    # lower distance => higher priority
    def addWithPriority(self, vertex, distance):
        if self.head is None:
            self.head = Node(vertex)
            self.tail = self.head

    def decreasePriority(self):
        pass

    def extractMin(self):
        pass


class Dijkstra:
    def __init__(self):
        self.vertexes = []

    def resetDijkstra(self):
        for vertex in self.vertexes:
            vertex.minDistance = float('Inf')
            vertex.previousVertex = None

    def computePath(self, sourceId):
        self.resetDijkstra()

        # source == target
        for vertex in self.vertexes:
            if vertex.id == sourceId:
                vertex.minDistance = 0
                break



    def getShortestPathTo(self, targetId):
        for vertex in self.vertexes:
            if vertex.id == targetId:
                return vertex.minDistance

        return None

    def createGraph(self, vertexes, edges):
        for vertex in vertexes:
            for edge in edges:
                if vertex.id == edge.source:
                    vertex.addEdge(edge)
                    edges.remove(edge)

        self.vertexes = vertexes

    def getVertexes(self):
        return self.vertexes


def runTests():
    redville = Vertex(0, "Redville")
    blueville = Vertex(1, "Blueville")
    greenville = Vertex(2, "Greenville")
    orangeville = Vertex(3, "Orangeville")
    purpleville = Vertex(4, "Purpleville")
    vertexes = [redville, blueville, greenville, orangeville, purpleville]

    edgesRed = [Edge(0, 1, 5), Edge(0, 2, 10), Edge(0, 3, 8)]
    edgesBlue = [Edge(1, 0, 5), Edge(1, 2, 3), Edge(1, 4, 7)]
    edgesGreen = [Edge(2, 0, 10), Edge(2, 1, 3)]
    edgesOrange = [Edge(3, 0, 8), Edge(3, 4, 2)]
    edgesPurple = [Edge(4, 3, 2), Edge(4, 1, 7)]
    edges = edgesRed + edgesBlue + edgesGreen + edgesOrange + edgesPurple

    dijkstra = Dijkstra()
    dijkstra.createGraph(vertexes, edges)


runTests()
