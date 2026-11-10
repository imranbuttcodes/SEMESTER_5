#UCS Generic Algorithm

import heapq

def ucs(graph, start, goal):
    pq = [(0, start, [start])]
    visited = set()

    while pq:
        cost, node, path = heapq.heappop(pq)

        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            return path, cost

        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(
                    pq,
                    (cost + weight, neighbor, path + [neighbor])
                )

    return None, float("inf")


# graph = {
#     'A': [('B', 1), ('C', 4)],
#     'B': [('D', 2), ('E', 5)],
#     'C': [('G', 3)],
#     'D': [],
#     'E': [],
#     'G': []
# }


graph = {
    'A': [('B', 11), ('C',14) , ('D',7)],
    'B': [('E', 15)],
    'E': [('H', 9)],
    'H': [('G', 10)],
    'C': [('E', 8), ('F', 10)],
    'D': [('F', 25)],
    'F': [('G', 20)],
}


path, cost = ucs(graph, 'A', 'G')

print("Path:", path)
print("Cost:", cost)




