import heapq


class Vertex:
    def __init__(self, identification, name):
        self.id = identification
        self.name = name
        self.minDistance = float('Inf')
        self.previousVertex = None
        self.edges = []

    def addEdge(self, edge):
        self.edges.append(edge)

    def __str__(self):
        return "id = " + str(self.id) + ", name = " + str(self.name) + ", minDistance = " + str(self.minDistance)

    def __repr__(self):
        return "id = " + str(self.id) + ", name = " + str(self.name) + ", minDistance = " + str(self.minDistance)

    def __lt__(self, other):
        return self.minDistance < other.minDistance

    def __gt__(self, other):
        return self.minDistance > other.minDistance


class Edge:
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight

    def __repr__(self):
        return "(" + str(self.source) + ", " + str(self.target) + ", " + str(self.weight) + ")"


class Dijkstra:
    def __init__(self):
        self.vertexes = []

    def createGraph(self, vertexes, edges):
        for vertex in vertexes:
            for edge in edges:
                if vertex.id == edge.source:
                    vertex.addEdge(edge)

        self.vertexes = vertexes

    def getVertexes(self):
        return self.vertexes

    def getVertexById(self, vertexId):
        for vertex in self.vertexes:
            if vertex.id == vertexId:
                return vertex

    def computePath(self, sourceId):
        self.resetDijkstra()

        # source == target
        for vertex in self.vertexes:
            if vertex.id == sourceId:
                vertex.minDistance = 0
                break

        heap = []
        for vertex in self.vertexes:
            heapq.heappush(heap, (vertex.minDistance, vertex))

        while heap:
            priority, vertex = heapq.heappop(heap)
            for edge in vertex.edges:
                alt = priority + edge.weight
                neighbour = self.getVertexById(edge.target)
                if alt < neighbour.minDistance:
                    neighbour.minDistance = alt
                    neighbour.previousVertex = vertex
                    heapq.heappush(heap, (alt, neighbour))

    def getShortestPathTo(self, targetId):
        path = []
        vertex = self.getVertexById(targetId)
        path.append(vertex)
        while vertex.previousVertex:
            path.append(vertex.previousVertex)
            vertex = vertex.previousVertex

        path.reverse()
        return path


    def resetDijkstra(self):
        for vertex in self.vertexes:
            vertex.minDistance = float('Inf')
            vertex.previousVertex = None


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
    dijkstra.computePath(1)
    vertexes = dijkstra.getVertexes()

    for vertex in vertexes:
        print("Vertex: " + str(vertex.id))
        print(vertex.minDistance)
        print()

    print(dijkstra.getShortestPathTo(4))




runTests()
