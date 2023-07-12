def TopologicalSort(graph):
    TopologicalSortedList = []  
    ZeroInDegreeVertexList = []
    inDegree = { u : 0 for u in graph }

    for u in graph:
        for v in graph[u]:
            inDegree[v] += 1

    for k in inDegree:
        if (inDegree[k] == 0):
            ZeroInDegreeVertexList.append(k)    

    while ZeroInDegreeVertexList:
        v = ZeroInDegreeVertexList.pop(0)
        TopologicalSortedList.append(v)
       
        for neighbour in graph[v]:
            inDegree[neighbour] -= 1
            if (inDegree[neighbour] == 0):
                ZeroInDegreeVertexList.append(neighbour)

    return TopologicalSortedList
