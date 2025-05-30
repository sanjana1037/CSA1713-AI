board = [" "]*9
def show(): print("\n".join(["|".join(board[i:i+3]) for i in range(0,9,3)]))
def win(p): return any(all(board[j]==p for j in line) for line in [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]])
turn = "X"
for _ in range(9):
    show()
    move = int(input(f"Player {turn}, choose 0-8: "))
    if board[move] == " ": board[move] = turn
    if win(turn): show(); print(f"{turn} wins!"); break
    turn = "O" if turn == "X" else "X"
else: show(); print("It's a draw!")
