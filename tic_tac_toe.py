# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Function to check if a player has won
def check_win(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([spot == player for spot in board[i]]) or all([board[j][i] == player for j in range(3)]):
            return True
    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

# Function to check if the board is full
def is_board_full(board):
    return all([spot != " " for row in board for spot in row])

# Function to get the player's move
def get_move(player):
    while True:
        try:
            row = int(input(f"Player {player}, enter the row (1-3): ")) - 1
            col = int(input(f"Player {player}, enter the column (1-3): ")) - 1
            if row in range(3) and col in range(3):
                return row, col
            else:
                print("Invalid input. Please enter numbers between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

# Main function to play the game
def play_game():
    # Initialize the board
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    # Game loop
    while True:
        print_board(board)
        row, col = get_move(current_player)
        
        # Check if the move is valid
        if board[row][col] == " ":
            board[row][col] = current_player
            
            # Check if the current player has won
            if check_win(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            
            # Check if the board is full
            if is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break
            
            # Switch the player
            current_player = "O" if current_player == "X" else "X"
        else:
            print("That spot is already taken. Try again.")

# Start the game
play_game()
