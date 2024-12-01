def initialize_board(GRID_SIZE):
    return [["-" for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

def mark_square(board, row, col, chip_type):
    board[row][col] = chip_type

def board_is_full(board):
    return all(all(cell != "-" for cell in row) for row in board)

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

def three_players_check_if_winner(board, chip):
    flag = False
    for i in range(0, 3):
        for j in range(0, 3):
            sub_board = [row[j:(j+3)] for row in board[i:(i+3)]]
            if check_if_winner(sub_board, chip):
                flag = True
                break
    
    return flag

def available_square(board, row, col):
    return board[row][col] == '-'

