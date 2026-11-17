# #Greedy Search Generic Algorithm

# import heapq
# def greedy_search(graph, heuristic, start, goal):
#     open_list = [(heuristic[start], start)]
#     visited = set()
#     parent = {start: None}

#     while open_list:
#         # Lowest heuristic value wala node select karo
#         open_list.sort()
#         h_value, current = open_list.pop(0)

#         if current in visited:
#             continue

#         visited.add(current)
#         print("Visiting:", current, "h =", heuristic[current])

#         # Goal check
#         if current == goal:
#             path = []
#             node = goal

#             while node is not None:
#                 path.append(node)
#                 node = parent[node]

#             path.reverse()
#             print("Goal Found!")
#             print("Path:", path)
#             return path

#         # Neighbours explore karo
#         for neighbor in graph[current]:
#             if neighbor not in visited and neighbor not in parent:
#                 parent[neighbor] = current
#                 open_list.append((heuristic[neighbor], neighbor))

#     print("Goal not found")
#     return None


# # Example graph
# graph = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E'],
#     'C': ['F', 'G'],
#     'D': [],
#     'E': [],
#     'F': [],
#     'G': []
# }

# # Heuristic values
# heuristic = {
#     'A': 6,
#     'B': 4,
#     'C': 2,
#     'D': 5,
#     'E': 3,
#     'F': 1,
#     'G': 0
# }

# greedy_search(graph, heuristic, 'A', 'G')





def greedy_search(graph, heuristic, start, goal):

    open_list = [(heuristic[start], start, [start])]
    all_paths = []

    while open_list:

        # Select node with lowest heuristic
        open_list.sort()
        h_value, current, path = open_list.pop(0)

        print("Visiting:", current, "h =", h_value)

        # Goal check
        if current == goal:
            all_paths.append(path)
            print("Goal Found:", path)
            continue

        # Explore neighbours
        for neighbor in graph[current]:

            # Avoid cycles in the current path
            if neighbor not in path:

                new_path = path + [neighbor]

                open_list.append(
                    (heuristic[neighbor], neighbor, new_path)
                )

    # Print all paths
    print("\nAll Possible Paths:")

    for i, path in enumerate(all_paths, 1):
        print(f"Path {i}:", path)

    return all_paths


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

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
