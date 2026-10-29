
def print_board(board):
    for i in range(3):
        print(" " + " | ".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("---+---+---")

def check_winner(board):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ":
            return board[combo[0]]
    return None

def is_full(board):
    return " " not in board

def play_game():
    board = [" " for _ in range(9)]
    current_player = "X"

    while True:
        print_board(board)
        move = input(f"Player {current_player}, enter your move (1-9): ")

        try:
            move = int(move) - 1
            if move < 0 or move > 8 or board[move] != " ":
                print("Invalid move. Try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")
            continue

        board[move] = current_player

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break
        elif is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    print("Welcome to Tic-Tac-Toe!")
    play_game()
