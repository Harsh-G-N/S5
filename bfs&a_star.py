import heapq

def read_graph():
    graph = {}
    no_of_edges = int(input("Enter the number of edges: "))
    
    print("Enter edges as (a b cost):")
    for _ in range(no_of_edges):
        u, v, cost = input().split()
        cost = int(cost)
        
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        
        graph[u].append((v,cost))
        graph[v].append((u,cost))
    
    return graph

def read_heuristic():
    heuristic = {}
    no_of_nodes = int(input("Enter the number of nodes: "))

    print("Enter heuristic as (node heuristic):")
    for _ in range(no_of_nodes):
        u, v = input().split()
        heuristic[u] = int(v)

    return heuristic

def best_first_search(graph, start, goal, heuristic):
    visited = set()
    pq = [(heuristic[start], start)]  # Priority Queue stores (heuristic, node)
    path = []

    while pq:
        current = heapq.heappop(pq)  # Get the node with the lowest heuristic value
        node = current[1]  # Extract node from the tuple
        
        path.append(node)

        if node == goal:
            return path
        
        if node not in visited:
            visited.add(node)

            for neighbour in graph.get(node, []):
                if neighbour not in visited:
                    # Push neighbour with its heuristic value
                    heapq.heappush(pq, (heuristic[neighbour], neighbour))

    return []  # Return empty path if goal is not found

def a_star_search(graph,start,goal,heuristic):
    pq = []
    heapq.heappush(pq,(heuristic[start],start))
    g_cost = {start:0}
    came_from = {}

    while pq:
        current_f_cost, current_node = heapq.heappop(pq)

        if current_node == goal:
            path = []
            while current_node in came_from:
                path.append(current_node)
                current_node = came_from[current_node]
            path.append(start)
            return path[::-1]
        
        for neighbours, edge_cost in graph.get(current_node,[]):
            tenative_g_cost = g_cost[current_node] + edge_cost

            if neighbours not in g_cost or tenative_g_cost < g_cost[neighbours]:
                g_cost[neighbours] = tenative_g_cost
                f_cost = g_cost[neighbours] + heuristic[neighbours]
                heapq.heappush(pq,(f_cost,neighbours))
                came_from[neighbours] = current_node
            
    return []

# Read graph and heuristics
graph = read_graph()
heuristics = read_heuristic()

# Get the start and goal nodes
start_node = input("Enter the start node: ")
goal_node = input("Enter the goal node: ")

# Perform Best-First Search
path = a_star_search(graph, start_node, goal_node, heuristics)

# Print the path from start to goal
print("Path from", start_node, "to", goal_node, ":", path)
