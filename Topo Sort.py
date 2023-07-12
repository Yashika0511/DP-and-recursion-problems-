def topologicalSortHelper(graph, v, visited, stack):
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            topologicalSortHelper(i, visited, stack)
    stack.append(v)

def topologicalSort(graph, V):
    visited = [False]*V
    stack = []
    for i in range(V):
        if visited[i] == False:
            topologicalSortHelper(graph, i, visited, stack)
    print(stack[::-1]) 
