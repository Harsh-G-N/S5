import random

def get_user_graph():
    # Input number of nodes
    num_nodes = int(input("Enter the number of regions (nodes): "))
    graph = {i: [] for i in range(num_nodes)}

    # Input edges
    print("Enter the neighboring regions as pairs (e.g., '0 1' for an edge between 0 and 1). Type 'done' when finished:")
    while True:
        edge = input()
        if edge.lower() == 'done':
            break
        node1, node2 = map(int, edge.split())
        graph[node1].append(node2)
        graph[node2].append(node1)  # Since it's an undirected graph

    return graph

def hill_climbing(graph,colors):

    def count_conflict(solution):
        conflict = 0
        for node in graph:
            for neighbours in graph[node]:
                if solution[node] == solution[neighbours]:
                    conflict+=1
        return conflict
    
    current_solution = {node:random.choice(colors) for node in graph}

    while True:
        conflict = count_conflict(current_solution)
        if conflict == 0:
            break

        best_solution = current_solution
        best_conflict = conflict

        for node in graph:
            original_color = current_solution[node]
            for color in colors:
                if color != original_color:
                    current_solution[node] = color
                    new_conflict = count_conflict(current_solution)

                    if new_conflict < best_conflict:
                        best_conflict = new_conflict
                        best_solution = current_solution.copy()

            current_solution[node] = original_color

        if best_conflict < conflict:
            current_solution = best_solution
        else:
            print("no solution")
            break

    return current_solution

# Input colors and graph
colors = input("Enter the colors separated by spaces (e.g., 'Red Green Blue'): ").split()
graph = get_user_graph()

# Solve the map coloring problem
solution = hill_climbing(graph, colors)
print("Coloring solution:", solution)
    
