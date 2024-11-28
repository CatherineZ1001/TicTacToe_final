'''
[
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"],
]

'''

def initialize_board():
    # 1st approach
    global BOARD_COLS, BOARD_ROWS
    return [["-" for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

def mark_square(board, row, col, chip_type):
    board[row][col] = chip_type

def board_is_full(board):
    return all(all(cell != "" for cell in row) for row in board)

def check_if_winner(board, chip):
    """
    Checks if the given chip has formed a winning line.
    """
    # Check rows
    for row in board:
        if all(cell == chip for cell in row):
            return True

    # Check columns
    for col in range(len(board)):
        if all(row[col] == chip for row in board):
            return True

    # Check diagonals
    if all(board[i][i] == chip for i in range(len(board))):
        return True
    if all(board[i][len(board) - 1 - i] == chip for i in range(len(board))):
        return True

    return False
    
'''
def check_if_winner(board, chip_type):
    """Check for a winning condition on the board."""
    winning_length = 3 if BOARD_ROWS <= 3 else 4 if BOARD_ROWS == 4 else 5

    # Check rows for a win
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS - winning_length + 1):
            if all(board[row][col + offset] == chip_type for offset in range(winning_length)):
                return True

    # Check columns for a win
    for col in range(BOARD_COLS):
        for row in range(BOARD_ROWS - winning_length + 1):
            if all(board[row + offset][col] == chip_type for offset in range(winning_length)):
                return True

    # Check diagonals (top-left to bottom-right)
    for row in range(BOARD_ROWS - winning_length + 1):
        for col in range(BOARD_COLS - winning_length + 1):
            if all(board[row + offset][col + offset] == chip_type for offset in range(winning_length)):
                return True

    # Check diagonals (top-right to bottom-left)
    for row in range(BOARD_ROWS - winning_length + 1):
        for col in range(winning_length - 1, BOARD_COLS):
            if all(board[row + offset][col - offset] == chip_type for offset in range(winning_length)):
                return True

    return False
'''
    
    def is_valid(board, row, col):
    return  0 <= row < BOARD_ROWS and 0 <= col < BOARD_COLS and board[row][col] == '-'

'''def check_if_winner(board, chip_type):
    # check all rows
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == chip_type:
            return True

    # check all columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == chip_type:
            return True

    if board[0][0] == board[1][1] == board[2][2] == chip_type:
        return True
    if board[0][2] == board[1][1] == board[2][0] == chip_type:
        return True

    return False'''

'''# row: row index, col: col index
def is_valid(board, row, col):
    if 0 <= row <= BOARD_ROWS and 0 <= col <= BOARD_COLS and board[row][col] == '-':
        return True
    return False'''

'''def print_board(board):
    for row in board:    # row: ["-", "-", "-"]
        for col in row:
            print(col, end=" ")
        print()'''


'''def available_square(board, row, col):
    return board[row][col] == '-'
    '''

'''if __name__ == "__main__":
    # main logic
    print("Player 1: x\nPlayer 2: o\n")
    board = initialize_board()
    print_board(board)

    player = 1
    chip = 'x'
    game_continue = True

    while game_continue:
        print(f"Player {player}'s Turn ({chip}):")
        row = int(input("Enter a row number (0, 1, or 2): "))
        col = int(input("Enter a column number (0, 1, or 2): "))

        while not is_valid(board, row, col):
            if row < 0 or col < 0 or row > 2 or col > 2:
                print("This position is off the bounds of the board! Try again.")
            elif board[row][col] != '-':
                print("Someone has already made a move at this position! Try again.")
            row = int(input("Enter a row number (0, 1, or 2): "))
            col = int(input("Enter a column number (0, 1, or 2): "))

        mark_square(board, row, col, chip)
        print_board(board)

        if check_if_winner(board, chip):
            print(f"\nPlayer {player} has won!")
            game_continue = False
        else:
            if board_is_full(board):
                print("\nIt's a tie!")
                game_continue = False


        # alternating between players
        player = 2 if player == 1 else 1
        chip = 'o' if chip == 'x'else 'x'
        '''
