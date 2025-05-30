def tsp_nearest_neighbour(distance_matrix):
    n = len(distance_matrix)
    visited = [False] * n
    path = [0]  # start from city 0
    visited[0] = True
    total_cost = 0
    current = 0

    for _ in range(n - 1):
        next_city = -1
        min_dist = float('inf')
        for j in range(n):
            if not visited[j] and 0 < distance_matrix[current][j] < min_dist:
                min_dist = distance_matrix[current][j]
                next_city = j
        visited[next_city] = True
        path.append(next_city)
        total_cost += min_dist
        current = next_city

    total_cost += distance_matrix[current][0]  # return to start
    path.append(0)

    return path, total_cost

n = int(input("Enter number of cities: "))
distance_matrix = []

print("Enter the distance matrix row by row:")
for i in range(n):
    row = list(map(int, input(f"Row {i + 1}: ").split()))
    distance_matrix.append(row)

path, cost = tsp_nearest_neighbour(distance_matrix)

print("\nShortest Path (Approx.):", ' -> '.join(map(str, path)))
print("Total Cost:", cost)
