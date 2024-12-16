import heapq

# Function to read the graph as a tree structure
def read_graph():
    graph = {}
    no_of_edges = int(input("Enter the number of edges: "))
    
    print("Enter edges as (parent child):")
    for _ in range(no_of_edges):
        u, v = input().split()
        
        if u not in graph:
            graph[u] = []
        
        graph[u].append(v)  # Only add one direction for a directed tree structure
    
    return graph

def read_leaf_values():
    leaf_values = {}
    no_of_leaf_nodes = int(input("enter the no of leaf nodes:"))

    print("enter leaf values as (leaf_node value)")
    for i in range(no_of_leaf_nodes):
        u,v = input().split()
        leaf_values[u] = int(v)
    
    return leaf_values

def minimax(node,graph,leaf_values,is_maximising = True):
    if node not in graph:
        return leaf_values[node], [node]
    
    if is_maximising:
        best_value = float('-inf')
        best_path = []

        for child in graph.get(node,[]):
            value, path = minimax(child,graph,leaf_values,False)
            if best_value < value:
                best_value = value
                best_path = [node] + path
            
        return best_value, best_path
    else:
        best_value = float('inf')
        best_path = []

        for child in graph.get(node,[]):
            value, path = minimax(child,graph,leaf_values,True)
            if value < best_value:
                best_value = value
                best_path = [node] + path

        return best_value,best_path
    

# Read the graph and leaf values
graph = read_graph()
leaf_values = read_leaf_values()

# Input the root of the tree
root = input("Enter the root node: ")

# Execute the minimax algorithm
optimal_value, optimal_path = minimax(root, graph, leaf_values, True)  # Assuming the root is a maximizing player
print("Optimal value for the root node:", optimal_value)
print("Path to optimal value:", " -> ".join(optimal_path))