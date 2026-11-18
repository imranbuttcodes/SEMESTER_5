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



import heapq
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


     
from collections import deque     
def bfs(graph, start, goal):
    open_list = deque([start])

    visited = {start}

    parent = {
        start: (None, 0)
    }

    while open_list:
        node = open_list.popleft()

        if node == goal:
            path = []
            cost = 0

            while node:
                path.append(node)

                node , c = parent[node]

                cost += c
            
            path.reverse()


            return path, cost
        
        for neighbour, weight in graph[node]:
            if neighbour not in visited and neighbour not in parent:                
                
                parent[neighbour] = node, weight
                open_list.append(neighbour)
                visited.add(neighbour)
        
    return None, 0
    

def usc(graph, start, goal):
    open_list = [(0, start, [start])]

    all_paths = []
    
    while open_list:
        
        cost, node, path = heapq.heappop(open_list)
        
        if node == goal:
            all_paths.append((path, cost))
            continue
        
        for neighbour, weight in graph[node]:
            if neighbour not in path:
                heapq.heappush(open_list, 
                (cost + weight, neighbour, path + [neighbour]))

    print("---------- All Paths -------------")
    for path, cost in all_paths:
        print("PATH: ", "->".join(path), " | Cost: ", cost)
    print("-"*20)
    print("-"*10, " Optimal Path ", "-"*10)
    opt_path, opt_cost = min(all_paths, key=lambda x:x[1])

    print("PATH: ", " -> ".join(opt_path), " COST| ",  opt_cost)
    print("-"*20)
    return None, 0


# def greedy_search_(graph, heuristic, start, goal):

#     open_list = [(heuristic[start], start, [start])]

#     all_paths = []

#     while open_list:
#         open_list.sort()
        
#         h_val, node, path = open_list.pop(0)

#         if node == goal:
#             all_paths.append((path, h_val))

#             continue
    
#         for neighor in graph[node]:
#             if neighor not in path:
#                 open_list.append((heuristic[neighor], neighor, path + [neighor]))
        
    
#     print("ALL PATHS: ")

#     for path, h_val in all_paths:
#         print("PATH: ", "->".join(path), " |H_VAL: ", h_val)
#     print()

#     print("OPTIMAL")
#     ??



def a_star(graph, heuristic, start, goal):
    # (f, g, node, path)
    open_list = [(heuristic[start], 0, start, [start])]

    all_paths = []

    while open_list:

        f_val, g_val, node, path = open_list.pop(0)

        if node == goal:
            all_paths.append((path, g_val))
            continue

        for neighbor, weight in graph[node]:
            if neighbor not in path:
                hval = heuristic[neighbor]

                new_g_val = g_val + weight

                new_path = path + [neighbor]

                new_fval = hval + new_g_val
                open_list.append((new_fval, new_g_val, neighbor, path + [neighbor]))

    if all_paths:
        print("---------- ALL PATHS -----------")
        for path, cost in all_paths:
            print("PATH: ", " -> ".join(path), " | Cost: ", cost)
        print()
        
        print("-------------- Optimal PATH --------------")
        opt_path, opt_cost = min(all_paths, key=lambda x:x[1])

        print("PATH: ", ' -> '.join(opt_path), " |Cost: ", opt_cost)


    return opt_path, opt_cost


        
        


graph_cost = {
    'A': [('B', 11), ('C',14) , ('D',7)],
    'B': [('E', 15)],
    'E': [('H', 9)],
    'H': [('G', 10)],
    'C': [('E', 8), ('F', 10)],
    'D': [('F', 25)],
    'F': [('G', 20)],
}


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
    'A': 30,
    'B': 25,
    'C': 15,
    'D': 20,
    'E': 18,
    'F': 10,
    'H': 10,
    'G': 0
}



# path, cost = bfs(graph_cost, 'A', 'G')

# print("PATH:", " -> ".join(path))
# print("cost: ", cost)

#usc(graph_cost, 'A' ,'G')
#path = greedy_search_with_all_paths(graph, heuristic, 'A', 'G')


path, cost = a_star(graph_cost, heuristic, 'A', 'G')

# print(path)

