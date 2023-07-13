def isCyclicDisconnected(graph, V):
    def isCyclicConnected(graph, s, V, visited):
        parent = [-1] * V
        q = deque()
        visited[s] = True
        q.append(s)
      
        while q != []:
            u = q.pop()
            for v in graph[u]:
                if not visited[v]:
                    visited[v] = True
                    q.append(v)
                    parent[v] = u
                elif parent[u] != v:
                    return True
        return False
  
    visited = [False] * V
    for i in range(V):
        if not visited[i] and isCyclicConnected(graph, i, V, visited):
            return True
    return False
