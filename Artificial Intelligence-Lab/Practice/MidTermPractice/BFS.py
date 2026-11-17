from collections import deque

def bfs(graph, start, goal):
    queue = deque([start])

    visited = {start}

    parent = {
        start: (None, 0)
    }

    while queue:

        node = queue.popleft()

       
        print("CLOSED:", visited)
        if node == goal:
            path = []

            cost = 0
            while node:
                path.append(node)
                node, c_ = parent[node]
                cost += c_
            path.reverse()
            
            return path, cost

        for neighbor, c in graph[node]:
            if neighbor not in visited:
                parent[neighbor] = node, c
                visited.add(neighbor)
                queue.append(neighbor)
        
    return None, 0
        
   

graph = {
    'A': [('B', 11), ('C',14) , ('D',7)],
    'B': [('E', 15)],
    'E': [('H', 9)],
    'H': [('G', 10)],
    'C': [('E', 8), ('F', 10)],
    'D': [('F', 25)],
    'F': [('G', 20)],
}

path, cost = bfs(graph, 'A', 'G')

print("path", path)
print("path", cost)



