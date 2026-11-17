from collections import deque

def bfs(graph, start, goal):
    queue = deque([start])
    closed = set()           # Start empty; add nodes only when popped
    parent = {start: None}   # Tracks all discovered nodes

    while queue:
        node = queue.popleft()

        if node not in closed:
            closed.add(node)     # Add to closed ONLY when actually visited
        
        print("Visited:", node)
        print("Closed Set:", closed)

        if node == goal:
            print("Goal Found!")
            path = []
            while node:
                path.append(node)
                node = parent[node]
            path.reverse()
            return path

        for neighbor in graph.get(node, []):
            if neighbor not in parent:  # Check 'parent' instead of 'closed'
                queue.append(neighbor)
                parent[neighbor] = node

    print("Goal Not Found!")



graph = {
   'A': ['B', 'C' , 'D'],
    'B': ['E',],
    'E': ['H'],
    'H': ['G'],
    'C': ['E', 'F'],
    'D': ['F'],
    'F': ['G'],
}

print(bfs(graph, 'A', 'G'))
