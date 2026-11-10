
import heapq

def a_star(start, goal, graph, heuristic):

    # Priority queue: (f_score, node)
    open_list = []
    heapq.heappush(open_list, (0, start))

    # Track the shortest known cost
    g_score = {start: 0}

    # Track parent nodes
    came_from = {}

    while open_list:

        # Get node with lowest f_score
        current_f, current = heapq.heappop(open_list)

        # Goal reached
        if current == goal:
            path = []

            while current in came_from:
                path.append(current)
                current = came_from[current]

            path.append(start)
            path.reverse()

            return path, g_score[goal]

        # Explore neighbors
        for neighbor, cost in graph[current]:

            tentative_g = g_score[current] + cost

            if neighbor not in g_score or tentative_g < g_score[neighbor]:

                came_from[neighbor] = current
                g_score[neighbor] = tentative_g

                f_score = tentative_g + heuristic(neighbor, goal)

                heapq.heappush(
                    open_list,
                    (f_score, neighbor)
                )

    return None, float('inf')


# Example graph
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

# Heuristic function
def heuristic(node, goal):
    h = {
        'A': 3,
        'B': 2,
        'C': 1,
        'D': 0
    }
    return h[node]


# Run A*
start = 'A'
goal = 'D'

path, cost = a_star(start, goal, graph, heuristic)

print("Shortest Path:", path)
print("Total Cost:", cost)