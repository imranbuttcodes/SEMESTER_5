#DFS Generic Algorithm


def dfs(graph, start, goal):
    stack = [start]
    closed = set()

    while stack:
        node = stack.pop()

        if node in closed:
            continue

        closed.add(node)

        print("Node Explored:", node)
        print("Closed Set:", closed)

        if node == goal:
            print("Goal Found!")
            return

        for neighbor in reversed(graph[node]):
            if neighbor not in closed:
                stack.append(neighbor)

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

dfs(graph, 'S', 'G')