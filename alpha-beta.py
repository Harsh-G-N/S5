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
    no_of_leaf_nodes = int(input("Enter the number of leaf nodes:"))

    print("Enter leaf values as (leaf_node value):")
    for i in range(no_of_leaf_nodes):
        u, v = input().split()
        leaf_values[u] = int(v)
    
    return leaf_values

def minimax(node, graph, leaf_values, is_maximising=True, alpha=float('-inf'), beta=float('inf'), pruned_nodes=None):
    if pruned_nodes is None:
        pruned_nodes = []

    # Leaf node: return its value and path
    if node not in graph:
        return leaf_values[node], [node]
    
    if is_maximising:
        best_value = float('-inf')
        best_path = []

        for child in graph.get(node, []):
            value, path = minimax(child, graph, leaf_values, False, alpha, beta, pruned_nodes)
            if value > best_value:
                best_value = value
                best_path = [node] + path
            alpha = max(alpha, best_value)
            if beta <= alpha:
                pruned_nodes.append(node)  # Track pruned node
                break  # Beta cut-off
            
        return best_value, best_path
    else:
        best_value = float('inf')
        best_path = []

        for child in graph.get(node, []):
            value, path = minimax(child, graph, leaf_values, True, alpha, beta, pruned_nodes)
            if value < best_value:
                best_value = value
                best_path = [node] + path
            beta = min(beta, best_value)
            if beta <= alpha:
                pruned_nodes.append(node)  # Track pruned node
                break  # Alpha cut-off

        return best_value, best_path

# Read the graph and leaf values
graph = read_graph()
leaf_values = read_leaf_values()

# Input the root of the tree
root = input("Enter the root node: ")

# Initialize list to track pruned nodes
pruned_nodes = []

# Execute the minimax algorithm with alpha-beta pruning
optimal_value, optimal_path = minimax(root, graph, leaf_values, True, float('-inf'), float('inf'), pruned_nodes)

# Display results
print("Optimal value for the root node:", optimal_value)
print("Path to optimal value:", " -> ".join(optimal_path))
print("Pruning occurs at nodes:", pruned_nodes)
