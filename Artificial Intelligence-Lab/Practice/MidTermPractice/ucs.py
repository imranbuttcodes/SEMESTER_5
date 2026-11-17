
# import heapq



# import heapq

# def ucs(graph, start, goal):

#     pq = [(0, start, [start])]

#     all_paths = []

#     while pq:

#         cost, node, path = heapq.heappop(pq)

#         if node == goal:
#             all_paths.append((path, cost))
#             continue

#         for neighbor, weight in graph[node]:

#             if neighbor not in path:

#                 heapq.heappush(
#                     pq,
#                     (cost + weight, neighbor, path + [neighbor])
#                 )

#     if all_paths:

#         print("-------- ALL PATHS -------")

#         for path, cost in all_paths:
#             print("PATH:", path, "| COST:", cost)

#         print("\n\nOptimal path")

#         opt_path, opt_cost = min(
#             all_paths,
#             key=lambda x: x[1]
#         )

#         print("PATH:", opt_path, "| COST:", opt_cost)

#         return opt_path, opt_cost

#     return None, float("inf")




# graph = {
#     'A': [('B', 11), ('C',14) , ('D',7)],
#     'B': [('E', 15)],
#     'E': [('H', 9)],
#     'H': [('G', 10)],
#     'C': [('E', 8), ('F', 10)],
#     'D': [('F', 25)],
#     'F': [('G', 20)],
# }

# path, cost = ucs(graph, 'A', 'G')

# # print('path:', path)
# # print('Cost:', cost)



import heapq

def ucs(graph, start, goal):
    pq = [(0, start, [start])]

    all_paths = []
    while pq:
        cost, node, path = heapq.heappop(pq)

        if node == goal:
            all_paths.append((path, cost))
            continue
            
        for neighbour, weight in graph[node]:
            if neighbour not in path:
                heapq.heappush(pq,
                (cost + weight, neighbour, path + [neighbour]))
        

    if all_paths:

        print("------------------ ALL PATHS ------------------")
        
        for p, c in all_paths:
            print(f"PATH: {p} | Cost: {c}")
        
        print()
        print("OPTIMAL PATH")

        opt_path, opt_cost = min(all_paths, key=lambda x:x[1])

        print(f"path: {opt_path} | cost: {opt_cost}")
    
        return opt_path, opt_cost
    
    return None, float('inf')


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