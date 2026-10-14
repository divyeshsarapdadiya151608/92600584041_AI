#Implement Two Player Game - Tic-Tac-Toe (Using Heuristic Function).
def display(board):
    print()
    print(board[0], "|",board[1], "|",board[2])
    print("--+---+--")
    print(board[3], "|",board[4], "|",board[5])
    print("--+---+--")
    print(board[6], "|",board[7], "|",board[8])
    print()

def heuristic(board):
    win = [
        (0,1,2),
        (3,4,5),
        (6,7,8),
        (0,3,6),
        (1,4,7),
        (2,5,8),
        (0,4,8),
        (2,4,6)
    ]

    for a, b, c in win:
        if board[a] == board[b] == board[c] == "x":
            return 1
        elif board[a] == board[b] == board[c] == "o":
            return -1
    return 0

board = [" "] * 9
player = "x"

for turn in range(9):
    display(board)
    print("Player", player)

    position = int(input("Enter position (1-9): ")) - 1

    if position < 0 or position > 8 or board[position] != " ":
        print("Invalid position! Try again.")
        continue

    board[position] = player

    score = heuristic(board)

    if score == 1:
        display(board)
        print("Player X wins!")
        break
    elif score == -1:
        display(board)
        print("Player O wins!")
        break

    player = "o" if player == "x" else "x"

else:
    display(board)
    print("It's a draw!")

    
    
