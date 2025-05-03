from collections import deque

def get_successors(state, a, b):
    x, y = state
    return [
        (a, y),                           # Fill Jug A
        (x, b),                           # Fill Jug B
        (0, y),                           # Empty Jug A
        (x, 0),                           # Empty Jug B
        (x - min(x, b - y), y + min(x, b - y)),  # Pour A -> B
        (x + min(y, a - x), y - min(y, a - x))   # Pour B -> A
    ]

def bfs(a, b):
    visited = set()
    queue = deque()
    queue.append(((0, 0), []))  # ((jugA, jugB), path)

    while queue:
        (x, y), path = queue.popleft()
        if (x, y) in visited:
            continue
        visited.add((x, y))

        # Goal condition: 2 gallons in 3-gallon jug and 0 in 4-gallon jug
        if x == 2 and y == 0:
            return path + [(x, y)]

        for next_state in get_successors((x, y), a, b):
            if next_state not in visited:
                queue.append((next_state, path + [(x, y)]))
    return None

# --------- Run the specific problem ----------
a = 3  # Jug A capacity
b = 4  # Jug B capacity

result = bfs(a, b)

if result:
    print("\n✅ Steps to get 2 gallons in 3-gallon jug and 0 in 4-gallon jug:")
    for step in result:
        print(f"Jug A: {step[0]}  |  Jug B: {step[1]}")
else:
    print("❌ No solution found.")
