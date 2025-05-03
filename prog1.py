from collections import deque

# Possible moves with their index offset and move description
moves = {
    'up': (-3, '|^'),
    'down': (3, '|v'),
    'left': (-1, '->'),
    'right': (1, '<-')
}

# Check if a move is valid based on the zero (blank) tile position
def is_valid(pos, move):
    if move == 'left' and pos % 3 == 0:
        return False
    if move == 'right' and pos % 3 == 2:
        return False
    if move == 'up' and pos < 3:
        return False
    if move == 'down' and pos > 5:
        return False
    return True

# Generate next possible states from the current state
def get_next_states(state):
    next_states = []
    zero_pos = state.index(0)
    for move in moves:
        offset, symbol = moves[move]
        if is_valid(zero_pos, move):
            new_state = state[:]
            swap_pos = zero_pos + offset
            tile_moved = new_state[swap_pos]
            new_state[zero_pos], new_state[swap_pos] = new_state[swap_pos], new_state[zero_pos]
            next_states.append((new_state, f"move {tile_moved} {symbol}"))
    return next_states

# Print the 3x3 puzzle matrix
def print_matrix(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()

# Breadth-First Search to find the shortest solution path
def bfs(start, goal):
    visited = set()
    queue = deque([(start, [], 0)])

    while queue:
        current, path, cost = queue.popleft()
        if current == goal:
            return path, cost
        visited.add(tuple(current))

        for next_state, move_desc in get_next_states(current):
            if tuple(next_state) not in visited:
                visited.add(tuple(next_state))  # Prevent duplicate queueing
                queue.append((next_state, path + [(move_desc, next_state)], cost + 1))
    return None, -1

# Take user input for the puzzle matrix
def take_matrix_input(name):
    print(f"Enter {name} 3x3 matrix row by row (0 is blank):")
    matrix = []
    for _ in range(3):
        row = list(map(int, input().split()))
        matrix.extend(row)
    return matrix

# Entry point
if __name__ == "__main__":
    start_state = take_matrix_input("initial")
    goal_state = take_matrix_input("goal")

    if sorted(start_state) != list(range(9)) or sorted(goal_state) != list(range(9)):
        print("Invalid input. Use numbers 0 to 8 without duplicates.")
    else:
        path, cost = bfs(start_state, goal_state)
        if path:
            print(f"\nSolution found in {cost} moves:\n")
            current_state = start_state
            print_matrix(current_state)
            for i, (move, state) in enumerate(path, 1):
                print(f"Step {i}: {move}")
                print_matrix(state)
            print(f"Total cost: {cost}")
        else:
            print("No solution found.")
