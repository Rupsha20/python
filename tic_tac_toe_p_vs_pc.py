import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
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

def player_move(board, player):
    while True:
        try:
            row, col = map(int, input(f"Player {player}, enter row and column (0, 1, 2): ").split())
            if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == " ":
                return (row, col)
            print("Spot already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter numbers between 0 and 2.")

def computer_move(board):
    empty_spots = [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]
    return random.choice(empty_spots)

def tic_tac_toe_pvc():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    moves = 0

    while moves < 9:
        print_board(board)
        current_player = players[moves % 2]
        if current_player == "O":  # Computer's turn
            row, col = computer_move(board)
            print(f"Computer chooses: row {row}, col {col}")
        else:  # Player's turn
            row, col = player_move(board, current_player)
        
        board[row][col] = current_player
        moves += 1

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            return

    print_board(board)
    print("It's a draw!")

if __name__ == "__main__":
    tic_tac_toe_pvc()
