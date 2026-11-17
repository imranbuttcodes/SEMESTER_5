# from collections import deque

# def bfs(graph, start, goal):
#     queue = deque([start])
#     closed = set()           # Start empty; add nodes only when popped
#     parent = {start: None}   # Tracks all discovered nodes

#     while queue:
#         node = queue.popleft()

#         if node not in closed:
#             closed.add(node)     # Add to closed ONLY when actually visited
        
#         print("Visited:", node)
#         print("Closed Set:", closed)

#         if node == goal:
#             print("Goal Found!")
#             path = []
#             while node:
#                 path.append(node)
#                 node = parent[node]
#             path.reverse()
#             return path

#         for neighbor in graph.get(node, []):
#             if neighbor not in parent:  # Check 'parent' instead of 'closed'
#                 queue.append(neighbor)
#                 parent[neighbor] = node

#     print("Goal Not Found!")



# graph = {
#    'A': ['B', 'C' , 'D'],
#     'B': ['E',],
#     'E': ['H'],
#     'H': ['G'],
#     'C': ['E', 'F'],
#     'D': ['F'],
#     'F': ['G'],
# }

# print(bfs(graph, 'A', 'G'))



def greedy_search(graph, heuristic, start, goal):
    
    open_list = [(heuristic[start], start)]

    visited = set()

    parent = {
        start: None
    }

    while open_list:
        h_val, node =  min(open_list, key=lambda x: x[0])

        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            path = []

            while node:
                path.append(node)
                node = parent[node]
            
            path.reverse()
            
            return path

        for neighbour in graph[node]:
            if neighbour not in visited and neighbour not in parent:
                parent[neighbour] = node
                open_list.append((heuristic[neighbour],neighbour))
        
    return None



def greedy_search_with_all_paths(graph, heuristic, start, goal):
    
    open_list = [(heuristic[start], start, [start])]

    all_paths = []

    while open_list:
        h_val, node, path =  min(open_list, key=lambda x: x[0])


        if node == goal:
            all_paths.append((path, h_val))

            continue
           
        for neighbour in graph[node]:
            if neighbour not in path:
                new_path = path + [neighbour]

                open_list.append((heuristic[neighbour],neighbour, new_path))
            
    
    for i, path in enumerate(all_paths, 1):
        print(f"Path {i}:", path)


     



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


path = greedy_search_with_all_paths(graph, heuristic, 'A', 'G')

# print(path)

