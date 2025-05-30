def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

graph = {}
num_nodes = int(input("Enter number of nodes: "))

for i in range(num_nodes):
    node = input(f"Enter name of node {i+1}: ")
    neighbors = input(f"Enter neighbors of {node} (space-separated): ").split()
    graph[node] = neighbors

start_node = input("Enter starting node for DFS: ")

print("DFS Traversal:")
dfs(graph, start_node)
