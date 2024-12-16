def color_graph():
    # Read graph input
    graph = {}
    no_of_edges = int(input("Enter the number of edges: "))
    print("Enter edges as (a b):")
    for _ in range(no_of_edges):
        u, v = input().split()
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)

    # Read available colors
    colors = input("Enter available colors separated by space: ").split()

    # Initialize color assignment dictionary
    color_assignment = {}

    # Helper function to check if a color assignment is valid
    def is_safe(node, color):
        for neighbor in graph.get(node, []):
            if color_assignment.get(neighbor) == color:
                return False
        return True

    # Backtracking function
    def assign_color(node):
        if node is None:
            return True  # Successfully assigned colors to all nodes

        for color in colors:
            if is_safe(node, color):
                color_assignment[node] = color
                next_node = next((n for n in graph if n not in color_assignment), None)
                
                if assign_color(next_node):
                    return True
                color_assignment.pop(node)  # Backtrack

        return False

    # Start coloring from the first node
    start_node = next(iter(graph), None)
    if assign_color(start_node):
        print("Color assignment:")
        for node, color in color_assignment.items():
            print(f"{node}: {color}")
    else:
        print("No valid color assignment possible")

# Call the function to start the program
color_graph()
