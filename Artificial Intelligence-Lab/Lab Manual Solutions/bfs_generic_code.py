#BFS Generic Algorithm

from collections import deque

def bfs(graph, start, goal):
    queue = deque([start])
    closed = set()

    parent = {
        start: None
    }

    while queue:
        node = queue.popleft()

        if node in closed:
            continue

        closed.add(node)
        print("Visited:", node)
        print("Closed Set:", closed)



        if node == goal:
            path = []
            print("Goal Found!")


            while node:
                path.append(node)
                node = parent[node]
            
            path.reverse()

            print("PATH: ", path)

            return

        for neighbor in graph[node]:
            if neighbor not in closed:
                queue.append(neighbor)
                parent[neighbor] = node


    print("Goal Not Found!")


graph = {
    'S': ['A', 'B'],
    'A': ['C', 'D'],
    'B': ['E', 'G'],
    'C': [],
    'D': [],
    'E': [],
    'G': []
}

bfs(graph, 'S', 'G')