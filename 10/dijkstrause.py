# #New Dijkstra created
# dijkstra = Dijkstra()
# #Graph created
# dijkstra.createGraph(vertexes,edges)
# #Getting all vertexes
# dijkstraVertexes = dijkstra.getVertexes()
# #Computing min distance for each vertex in graph
# for vertexToCompute in dijkstraVertexes:
#     dijkstra.computePath(vertexToCompute.id)
#     print('Printing min distance from vertex:'+str(vertexToCompute.name))
#     #Print minDitance from current vertex to each other
#     for vertex in dijkstraVertexes:
#         print('Min distance to:'+str(vertex.name)+' is: '+str(vertex.minDistance))
#     #Reset Dijkstra between counting
#     dijkstra.resetDijkstra()
# #Distance with path
# for vertexToCompute in dijkstraVertexes:
#     dijkstra.computePath(vertexToCompute.id)
#     print('Printing min distance from vertex:'+str(vertexToCompute.name))
#     #Print minDitance and path from current vertex to each other
#     for vertex in dijkstraVertexes:
#         print('Min distance to:'+str(vertex.name)+' is: '+str(vertex.minDistance))
#         print('Path is:',end=" ")
#         #Get shortest path to target vertex
#         path = dijkstra.getShortestPathTo(vertex.id)
#         for vertexInPath in path:
#             print(str(vertexInPath.name),end=" ")
#         print()
#     #Reset Dijkstra between counting
#     dijkstra.resetDijkstra()
