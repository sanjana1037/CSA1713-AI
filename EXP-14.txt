# Define the game tree and terminal node scores
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

pruned = []

def alpha_beta(node, depth, alpha, beta, is_maximizing):
    print(f"{'Max' if is_maximizing else 'Min '} node: {node}, α={alpha}, β={beta}")
    
    if node not in tree:  # Leaf node
        print(f"Leaf node {node} returns {scores[node]}")
        return scores[node]

    if is_maximizing:
        max_eval = float('-inf')
        for child in tree[node]:
            eval = alpha_beta(child, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                print(f"Pruned at {child} in Max node {node}")
                pruned.extend(tree[node][tree[node].index(child)+1:])
                break
        print(f"Max node {node} returns {max_eval}")
        return max_eval
    else:
        min_eval = float('inf')
        for child in tree[node]:
            eval = alpha_beta(child, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                print(f"Pruned at {child} in Min node {node}")
                pruned.extend(tree[node][tree[node].index(child)+1:])
                break
        print(f"Min node {node} returns {min_eval}")
        return min_eval

best_score = alpha_beta('Root', 3, float('-inf'), float('inf'), True)

print("\nBest achievable score (Minimax with Alpha-Beta):", best_score)
print("Pruned nodes:", pruned)
