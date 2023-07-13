def detectCycle(graph):
    visited = [False] * len(graph)
    def DFS_Traversal(graph, v, visited, parent_node=-1):
        visited[v] = True
    
        for u in graph[v]:
            if not visited[u]:
                if DFS_Traversal(graph, u, visited, v):
                    return True
    
            elif u != parent_node:
                # found a back-edge 
                return True
    
        return False
    if DFS_Traversal(graph, 0, visited):
        print('Cycle detected')
    else:
        print('Cycle not detected')
