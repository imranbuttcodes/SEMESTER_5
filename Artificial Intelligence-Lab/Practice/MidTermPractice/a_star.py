def astar(graph, heuristic, start, goal):

    # (f, g, node, path)
    open_list = [(heuristic[start], 0, start, [start])]

    all_paths = []

    while open_list:

        f_val, g_val, node, path = open_list.pop(0)

        h_val = heuristic[node]

        if node == goal:
            all_paths.append((path, g_val))

            continue
    
        for neighbour, weight in graph[node]:
            if neighbour not in path:
                new_hval = heuristic[neighbour]
                new_gval = g_val + weight
                f_val = new_gval + new_hval

                open_list.append((new_hval, new_gval, neighbour, path + [neighbour]))
        
    
    print("\nAll Possible Paths:")

    for i, (path, cost) in enumerate(all_paths, 1):
        print(
            f"Path {i}: {' -> '.join(path)} | Cost: {cost}"
        )

    if all_paths:

        optimal_path, optimal_cost = min(
            all_paths, key=lambda x: x[1]
        )

        print("\nOptimal Path:", " -> ".join(optimal_path))
        print("Optimal Cost:", optimal_cost)

        return optimal_path, optimal_cost

graph = {
    'A': [('B', 11), ('C', 14), ('D', 7)],
    'B': [('E', 15)],
    'E': [('H', 9)],
    'H': [('G', 10)],
    'C': [('E', 8), ('F', 10)],
    'D': [('F', 25)],
    'F': [('G', 20)],
}

# Heuristic values
heuristic = {
    'A': 30,
    'B': 25,
    'C': 15,
    'D': 20,
    'E': 18,
    'F': 10,
    'H': 10,
    'G': 0
}

astar(graph, heuristic, 'A', 'G')