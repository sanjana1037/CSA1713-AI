def minimax(position, depth, is_maximizing, scores, tree):
    if depth == 0 or position not in tree:
        return scores.get(position, 0)

    if is_maximizing:
        best = float('-inf')
        for child in tree.get(position, []):
            val = minimax(child, depth - 1, False, scores, tree)
            best = max(best, val)
        return best
    else:
        best = float('inf')
        for child in tree.get(position, []):
            val = minimax(child, depth - 1, True, scores, tree)
            best = min(best, val)
        return best


tree = {
    'Root': ['A', 'B'],
    'A': ['A1', 'A2'],
    'B': ['B1', 'B2']
}

scores = {
    'A1': 3,
    'A2': 5,
    'B1': 2,
    'B2': 9
}

best_score = minimax('Root', 3, True, scores, tree)
print("Best achievable score for Maximizer:", best_score)
