import heapq

def a_star(graph, heuristics, start, goal):
    open_list = []
    heapq.heappush(open_list, (heuristics[start], 0, start, [start]))  # (f = g + h, g, current, path)

    visited = set()

    while open_list:
        f, g, current, path = heapq.heappop(open_list)

        if current == goal:
            print("Path found:", " -> ".join(path))
            print("Total cost:", g)
            return

        visited.add(current)

        for neighbor, cost in graph[current]:
            if neighbor not in visited:
                g_new = g + cost
                f_new = g_new + heuristics[neighbor]
                heapq.heappush(open_list, (f_new, g_new, neighbor, path + [neighbor]))

    print("No path found.")

def get_user_input():
    graph = {}
    heuristics = {}

    n = int(input("Enter number of nodes: "))
    print("Enter node names:")
    nodes = [input(f"Node {i+1}: ") for i in range(n)]

    for node in nodes:
        neighbors = input(f"Enter neighbors and costs from {node} (format: neighbor1:cost1 neighbor2:cost2 ...): ").split()
        graph[node] = []
        for item in neighbors:
            neighbor, cost = item.split(":")
            graph[node].append((neighbor, int(cost)))

    print("Enter heuristic value for each node:")
    for node in nodes:
        heuristics[node] = int(input(f"Heuristic for {node}: "))

    start = input("Enter start node: ")
    goal = input("Enter goal node: ")

    return graph, heuristics, start, goal

if __name__ == "__main__":
    graph, heuristics, start, goal = get_user_input()
    print("\nRunning A* algorithm...")
    a_star(graph, heuristics, start, goal)
