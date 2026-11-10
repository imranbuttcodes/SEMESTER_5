	

def ida_star(start, goal, neighbors, heuristic):
    threshold = heuristic(start)
    path = [start]

    def search(g, threshold):
        node = path[-1]
        f = g + heuristic(node)

        if f > threshold:
            return f

        if node == goal:
            return "FOUND"

        minimum = float("inf")

        for neighbor, cost in neighbors(node):

            if neighbor not in path:
                path.append(neighbor)

                result = search(g + cost, threshold)

                if result == "FOUND":
                    return "FOUND"

                minimum = min(minimum, result)
                path.pop()

        return minimum

    while True:
        result = search(0, threshold)

        if result == "FOUND":
            return path

        if result == float("inf"):
            return None

        threshold = result


# Example graph
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 2)],
    'D': [('G', 3)],
    'E': [('G', 2)],
    'F': [('G', 3)],
    'G': []
}

# Heuristic values
h = {
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 3,
    'E': 2,
    'F': 2,
    'G': 0
}

def neighbors(node):
    return graph[node]

def heuristic(node):
    return h[node]


# Run IDA*
result = ida_star('A', 'G', neighbors, heuristic)

print("Path:", result)