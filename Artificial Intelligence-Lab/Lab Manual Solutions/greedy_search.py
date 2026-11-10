#Greedy Search Generic Algorithm

import heapq
def greedy_search(graph, heuristic, start, goal):
    open_list = [(heuristic[start], start)]
    visited = set()
    parent = {start: None}

    while open_list:
        # Lowest heuristic value wala node select karo
        open_list.sort()
        h_value, current = open_list.pop(0)

        if current in visited:
            continue

        visited.add(current)
        print("Visiting:", current, "h =", heuristic[current])

        # Goal check
        if current == goal:
            path = []
            node = goal

            while node is not None:
                path.append(node)
                node = parent[node]

            path.reverse()
            print("Goal Found!")
            print("Path:", path)
            return path

        # Neighbours explore karo
        for neighbor in graph[current]:
            if neighbor not in visited and neighbor not in parent:
                parent[neighbor] = current
                open_list.append((heuristic[neighbor], neighbor))

    print("Goal not found")
    return None


# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

# Heuristic values
heuristic = {
    'A': 6,
    'B': 4,
    'C': 2,
    'D': 5,
    'E': 3,
    'F': 1,
    'G': 0
}

greedy_search(graph, heuristic, 'A', 'G')