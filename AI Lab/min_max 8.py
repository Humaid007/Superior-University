def minimax(piles, depth, maximizing_player):
    if depth == 0 or is_terminal(piles):
        return evaluate(piles)

    if maximizing_player:
        max_eval = float('-inf')
        for i in range(len(piles)):
            for j in range(1, piles[i] + 1):
                new_piles = piles[:]
                new_piles[i] -= j
                eval = minimax(new_piles, depth - 1, False)
                max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(len(piles)):
            for j in range(1, piles[i] + 1):
                new_piles = piles[:]
                new_piles[i] -= j
                eval = minimax(new_piles, depth - 1, True)
                min_eval = min(min_eval, eval)
        return min_eval

def is_terminal(piles):
    return all(pile == 0 for pile in piles)

def evaluate(piles):
    if is_terminal(piles):
        return 1 if len(piles) % 2 == 0 else -1
    else:
        return 0
    
    

piles = [3, 4, 5]
depth = 5  

best_move = None
best_eval = float('-inf')

for i in range(len(piles)):
    for j in range(1, piles[i] + 1):
        new_piles = piles[:]
        new_piles[i] -= j
        eval = minimax(new_piles, depth, False)
        if eval > best_eval:
            best_eval = eval
            best_move = (i, j)  

print("Best move:", best_move)