#BFS Generic Algorithm


from collections import deque

def bfs(graph, start, goal):
    queue = deque([start])
    closed = set()

    while queue:
        node = queue.popleft()

        if node in closed:
            continue

        closed.add(node)
        print("Visited:", node)
        print("Closed Set:", closed)

        if node == goal:
            print("Goal Found!")
            return

        for neighbor in graph[node]:
            if neighbor not in closed:
                queue.append(neighbor)

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