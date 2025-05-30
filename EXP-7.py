from collections import deque

def input_graph():
    graph = {}
    print("Enter graph edges (e.g., A B). Type 'done' to stop:")
    while True:
        line = input().strip()
        if line.lower() == 'done':
            break
        src, dest = line.split()
        graph.setdefault(src, []).append(dest)
        graph.setdefault(dest, []).append(src)  
    return graph

def bfs(graph, start, goal):
    visited = set()
    parent = {start: None}  
    queue = deque([start])

    while queue:
        node = queue.popleft()

        if node == goal:
            return parent

        visited.add(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited and neighbor not in parent:
                queue.append(neighbor)
                parent[neighbor] = node

    return None

def get_path(parent, start, goal):
    path = []
    current = goal
    while current != start:
        if current is None:  
            return None
        path.append(current)
        current = parent[current]
    path.append(start)
    path.reverse()
    return path

def main():
    print("Breadth-First Search (BFS) - Path Only")
    graph = input_graph()

    start = input("Enter start node: ").strip()
    goal = input("Enter goal node: ").strip()

    parent = bfs(graph, start, goal)

    if parent:
        path = get_path(parent, start, goal)
        print("\n Path Found:", " → ".join(path))
    else:
        print(" No path found.")

if __name__ == "__main__":
    main()
