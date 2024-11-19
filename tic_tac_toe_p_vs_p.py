def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Winning conditions
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],  # Row 1
        [board[1][0], board[1][1], board[1][2]],  # Row 2
        [board[2][0], board[2][1], board[2][2]],  # Row 3
        [board[0][0], board[1][0], board[2][0]],  # Column 1
        [board[0][1], board[1][1], board[2][1]],  # Column 2
        [board[0][2], board[1][2], board[2][2]],  # Column 3
        [board[0][0], board[1][1], board[2][2]],  # Diagonal 1
        [board[2][0], board[1][1], board[0][2]]   # Diagonal 2
    ]
    return [player, player, player] in win_conditions

def tic_tac_toe_pvp():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    moves = 0

    while moves < 9:
        print_board(board)
        current_player = players[moves % 2]
        print(f"Player {current_player}'s turn.")

        try:
            row, col = map(int, input("Enter row and column (0, 1, 2): ").split())
            if board[row][col] != " ":
                print("Spot already taken. Try again.")
                continue
            board[row][col] = current_player
            moves += 1
        except (ValueError, IndexError):
            print("Invalid input. Please enter numbers between 0 and 2.")
            continue

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            return

    print_board(board)
    print("It's a draw!")

if __name__ == "__main__":
    tic_tac_toe_pvp()
