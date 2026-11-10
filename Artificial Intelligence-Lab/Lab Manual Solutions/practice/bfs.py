from collections import deque


def bfs(graph, start, goal):

    queue = deque([start])
    
    closed = set()
    
    parent = {
        start: None
    }
            
    path = []

    while queue:

        node = queue.popleft()

        if node in closed:
            continue

        closed.add(node)

        if node == goal:
            
            while node is not None:
                path.append(node)

                node = parent[node]

            path.reverse()
            return path
        

        for neighbour in graph[node]:
            if neighbour not in parent:
                parent[neighbour] = node
                queue.append(neighbour)


    return None


graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E'],
    'E': ['H'],
    'H': ['G'],
    'C': ['E', 'F'],
    'D': ['F'],
    'F': ['G'],
    'G': []
}

path = bfs(graph, 'A', 'G')

print('path:', path)