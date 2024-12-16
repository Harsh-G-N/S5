from itertools import permutations

def tsp(adj_list,n):
    min_dist = float('inf')
    optimal_path = []
    cities = list(range(1,n))

    for perm in permutations(cities):
        current_path = [0] + list(perm) + [0]
        current_dist = 0

        for i in range(len(current_path) - 1):
            city_from = current_path[i]
            city_to = current_path[i+1]
            current_dist += adj_list[city_from].get(city_to,float('inf'))

        if current_dist < min_dist:
            min_dist = current_dist
            optimal_path = current_path

    return min_dist, optimal_path

n = int(input("Enter the number of cities: "))

# Initialize adjacency list
adj_list = {i: {} for i in range(n)}

print("Enter the distances between each pair of cities:")
for i in range(n):
    for j in range(i + 1, n):
        distance = int(input(f"Distance from city {i} to city {j}: "))
        adj_list[i][j] = distance
        adj_list[j][i] = distance  # Since it's an undirected graph, distance is symmetric

min_dist, optimal_path = tsp(adj_list,n)
print(f"min_dist : {min_dist}\nopt_path : {optimal_path}")