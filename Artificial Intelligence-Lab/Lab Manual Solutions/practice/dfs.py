from collections import deque


def dfs(graph, start, goal):

    stack = deque([start])

    closed = set()

    parent = {
        start: (None, 0)
    }

    path = []
    cost = 0

    while stack:

        node = stack.pop()

        if node in closed:
            continue

        closed.add(node)

        if node == goal:

            while node is not None:
                path.append(node)

                node, c = parent[node]

                cost += c


            path.reverse()
            return path, cost



        for neighbour, cst in reversed(graph[node]):
            if neighbour not in parent:
                parent[neighbour] = (node,cst)
                stack.append(neighbour)
                

    return None


graph = {
    'A': [('B', 11), ('C',14) , ('D',7)],
    'B': [('E', 15)],
    'E': [('H', 9)],
    'H': [('G', 10)],
    'C': [('E', 8), ('F', 10)],
    'D': [('F', 25)],
    'F': [('G', 20)],
}

path, cost = dfs(graph, 'A', 'G')

print('path:', path)
print('Cost:', cost)
