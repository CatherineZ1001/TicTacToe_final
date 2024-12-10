import random
import matplotlib.pyplot as plt
from tictactoe import initialize_board, available_square, mark_square, check_if_winner, board_is_full

# Game settings (change the board size here)
BOARD_SIZE = 5

# Results tracker
results = {'Player x': 0, 'Player o': 0, 'Tie': 0}
board_results_when_win = {'Player x': [], 'Player o': []}
first_o_counts = {f'({r + 1}, {c + 1})': 0 for r in range(BOARD_SIZE) for c in range(BOARD_SIZE)}
# Winning square counts
win_square_counts = {
    'x': {f'({r + 1}, {c + 1})': 0 for r in range(BOARD_SIZE) for c in range(BOARD_SIZE)},
    'o': {f'({r + 1}, {c + 1})': 0 for r in range(BOARD_SIZE) for c in range(BOARD_SIZE)}
}

def automated_game():
    """
    Automates one game of normal Tic Tac Toe and returns the result.
    """
    global the_first_o_position
    the_first_o_position = None
    board = initialize_board(BOARD_SIZE)
    chip = 'x'
    round = 1

    while True:
        # Automate moves
        empty_squares = [(r, c) for r in range(BOARD_SIZE) for c in range(BOARD_SIZE) if available_square(board, r, c)]
        if not empty_squares:
            break

        row, col = random.choice(empty_squares)
        mark_square(board, row, col, chip)
        
        # Keep track of the grid where the first o is placed
        if (round == 2) and (board[BOARD_SIZE//2][BOARD_SIZE//2] == 'x'):
            the_first_o_position = [row, col]

        # Check for winner
        if check_if_winner(board, chip):
            board_results_when_win[f'Player {chip}'].append(board)
            return f"Player {chip}"

        # Check for tie
        if board_is_full(board):
            return "Tie"

        # Switch player
        chip = 'o' if chip == 'x' else 'x'
        round += 1

def run_simulations(num_games = 1000):
    """
    Runs multiple games and records results.
    """
    for _ in range(num_games):
        result = automated_game()
        # Record results and the positions of first o placed when o wins
        results[result] += 1
        if (result == 'Player o') and not (the_first_o_position is None):
            first_o_counts[f'({the_first_o_position[0] + 1}, {the_first_o_position[1] + 1})'] += 1

    # Store the board when x wins    
    for board in board_results_when_win['Player x']:
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if board[i][j] == 'x':
                    win_square_counts['x'][f'({i + 1}, {j + 1})'] += 1
    # Store the board when o wins  
    for board in board_results_when_win['Player o']:
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if board[i][j] == 'o':
                    win_square_counts['o'][f'({i + 1}, {j + 1})'] += 1

    # Print the results
    print("Simulation Results:")
    for key, value in results.items():
        print(f"{key}: {value}")
    for player, counts in win_square_counts.items():
        print(f"{player}: {counts}")
    print(first_o_counts)

if __name__ == "__main__":
    run_simulations(10000)  # Run __ times of simulation


# Graphics
# Draw the bar chart of how many times each player wins and tie
players = list(results.keys())
values = list(results.values())
plt.bar(players, values, color = ['darkorange', 'blue', 'gray'])
plt.ylabel('Number of Wins')
plt.title(f'Tic Tac Toe ({BOARD_SIZE}*{BOARD_SIZE}) Simulation Results')
plt.show()


# Generate heatmap for boards when x wins and o wins respectively
heatmap_data_x = [[win_square_counts['x'][f'({r + 1}, {c + 1})'] for c in range(BOARD_SIZE)] for r in range(BOARD_SIZE)]
heatmap_data_o = [[win_square_counts['o'][f'({r + 1}, {c + 1})'] for c in range(BOARD_SIZE)] for r in range(BOARD_SIZE)]
fig, ax = plt.subplots(1, 2, figsize=(12, 6))

# The heatmap for player x
cax_x = ax[0].imshow(heatmap_data_x, cmap='hot', interpolation='nearest')
ax[0].set_title('Heatmap of Wins for Player X')
# x and y ticks represent board size
ax[0].set_xticks(range(BOARD_SIZE))
ax[0].set_yticks(range(BOARD_SIZE))
ax[0].set_xticklabels([f'Col {c + 1}' for c in range(BOARD_SIZE)])
ax[0].set_yticklabels([f'Row {r + 1}' for r in range(BOARD_SIZE)])
# The colorbar shows intensity level
fig.colorbar(cax_x, ax=ax[0])
# Annotate each cell with value
for i in range(BOARD_SIZE):
    for j in range(BOARD_SIZE):
        ax[0].annotate(f'{heatmap_data_x[i][j]}', xy=(j, i), ha='center', va='center', color='paleturquoise')
        
# The heatmap for player o
cax_o = ax[1].imshow(heatmap_data_o, cmap='hot', interpolation='nearest')
ax[1].set_title('Heatmap of Wins for Player O')
# x and y ticks represent board size
ax[1].set_xticks(range(BOARD_SIZE))
ax[1].set_yticks(range(BOARD_SIZE))
# The row and column labels
ax[1].set_xticklabels([f'Col {c + 1}' for c in range(BOARD_SIZE)])
ax[1].set_yticklabels([f'Row {r + 1}' for r in range(BOARD_SIZE)])
# The colorbar shows intensity level
fig.colorbar(cax_o, ax=ax[1])
# Annotate each cell with value
for i in range(BOARD_SIZE):
    for j in range(BOARD_SIZE):
        ax[1].annotate(f'{heatmap_data_o[i][j]}', xy=(j, i), ha='center', va='center', color='paleturquoise')

# Display heatmap
plt.show()


# Create the heatmap for the positions of the first o placed when o wins
position = [[first_o_counts[f'({r + 1}, {c + 1})'] for c in range(BOARD_SIZE)] for r in range(BOARD_SIZE)]
plt.imshow(position, cmap='hot', interpolation='nearest')
plt.title(f"The Position of the First o\nWhen o Wins in a {BOARD_SIZE}*{BOARD_SIZE} Grid")
# x and y ticks represent board size
plt.gca().set_xticks(range(BOARD_SIZE))
plt.gca().set_yticks(range(BOARD_SIZE))
# The row and column labels
plt.gca().set_xticklabels([f'Col {c + 1}' for c in range(BOARD_SIZE)])
plt.gca().set_yticklabels([f'Row {r + 1}' for r in range(BOARD_SIZE)])
# The colorbar shows intensity level
plt.colorbar(label='Intensity')
# Annotate each cell with value
for i in range(BOARD_SIZE):
    for j in range(BOARD_SIZE):
        plt.annotate(f'{position[i][j]}', xy=(j, i), ha='center', va='center', color='paleturquoise')

# Display heatmap
plt.show()