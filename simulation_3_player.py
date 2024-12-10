import random
import matplotlib.pyplot as plt
from tictactoe import initialize_board, available_square, mark_square, board_is_full, three_players_check_if_winner

# Game settings
WIDTH, HEIGHT = 600, 600
BOARD_SIZE = 5

# Results tracker
results = {'Player x': 0, 'Player o': 0, 'Player a': 0, 'Tie': 0}
board_results_when_win = {'Player x': [], 'Player o': [], 'Player a': []}

# Winning square counts
win_square_counts = {
    'x': {f'({r + 1}, {c + 1})': 0 for r in range(BOARD_SIZE) for c in range(BOARD_SIZE)},
    'o': {f'({r + 1}, {c + 1})': 0 for r in range(BOARD_SIZE) for c in range(BOARD_SIZE)},
    'a': {f'({r + 1}, {c + 1})': 0 for r in range(BOARD_SIZE) for c in range(BOARD_SIZE)}
}

def automated_game():
    """
    Automates one game of 3-player Tic Tac Toe and returns the result.
    """
    board = initialize_board(BOARD_SIZE)
    players = ['x', 'o', 'a']
    current_index = 0

    while True:
        chip = players[current_index]

        # Automate moves
        empty_squares = [(r, c) for r in range(BOARD_SIZE) for c in range(BOARD_SIZE) if available_square(board, r, c)]
        if not empty_squares:
            break

        row, col = random.choice(empty_squares)
        mark_square(board, row, col, chip)

        # Check for winner
        if three_players_check_if_winner(board, chip):
            board_results_when_win[f'Player {chip}'].append(board)
            return f"Player {chip}"

        # Check for tie
        if board_is_full(board):
            return "Tie"

        # Switch player
        current_index = (current_index + 1) % len(players)


def run_simulations(num_games=1000):
    """
    Runs multiple games of 3-player Tic Tac Toe and records results.
    """
    for _ in range(num_games):
        result = automated_game()
        results[result] += 1

    for player, boards in board_results_when_win.items():
        chip = player.split()[-1].lower()
        for board in boards:
            for i in range(BOARD_SIZE):
                for j in range(BOARD_SIZE):
                    if board[i][j] == chip:
                        win_square_counts[chip][f'({i + 1}, {j + 1})'] += 1

    print("Simulation Results:")
    for key, value in results.items():
        print(f"{key}: {value}")
    for player, counts in win_square_counts.items():
        print(f"{player}: {counts}")

    #bar graph results
    players = list(results.keys())
    values = list(results.values())
    plt.bar(players, values, color = ['darkorange', 'blue', 'lime', 'gray'])
    plt.ylabel('Number of Wins')
    plt.title('Tic Tac Toe Simulation Results')
    plt.show()

    # generate heatmap for players
    heatmap_data_x = [[win_square_counts['x'][f'({r + 1}, {c + 1})'] for c in range(BOARD_SIZE)] for r in range(BOARD_SIZE)]
    heatmap_data_o = [[win_square_counts['o'][f'({r + 1}, {c + 1})'] for c in range(BOARD_SIZE)] for r in range(BOARD_SIZE)]
    heatmap_data_a = [[win_square_counts['a'][f'({r + 1}, {c + 1})'] for c in range(BOARD_SIZE)] for r in range(BOARD_SIZE)]

    # create figure and subplots
    fig, ax = plt.subplots(1, 3, figsize=(18, 6))

    # heatmap for player x
    cax_x = ax[0].imshow(heatmap_data_x, cmap='hot', interpolation='nearest')
    ax[0].set_title('Heatmap of Wins for Player X')
    #x and y ticks represent board size
    ax[0].set_xticks(range(BOARD_SIZE))
    ax[0].set_yticks(range(BOARD_SIZE))
    #row and column labels
    ax[0].set_xticklabels([f'Col {c + 1}' for c in range(BOARD_SIZE)])
    ax[0].set_yticklabels([f'Row {r + 1}' for r in range(BOARD_SIZE)])
    #colorbar shows intensity level
    fig.colorbar(cax_x, ax=ax[0])
    #annotate each cell with value
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            ax[0].annotate(f'{heatmap_data_x[i][j]}', xy=(j, i), ha='center', va='center', color='paleturquoise')

    # heatmap for player o
    cax_o = ax[1].imshow(heatmap_data_o, cmap='hot', interpolation='nearest')
    ax[1].set_title('Heatmap of Wins for Player O')
    #x and y ticks represent board size
    ax[1].set_xticks(range(BOARD_SIZE))
    ax[1].set_yticks(range(BOARD_SIZE))
    #row and column labels
    ax[1].set_xticklabels([f'Col {c + 1}' for c in range(BOARD_SIZE)])
    ax[1].set_yticklabels([f'Row {r + 1}' for r in range(BOARD_SIZE)])
    #colorbar shows intensity level
    fig.colorbar(cax_o, ax=ax[1])
    #annotate each cell with value
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            ax[1].annotate(f'{heatmap_data_o[i][j]}', xy=(j, i), ha='center', va='center', color='paleturquoise')

    #heatmap for player a
    cax_a = ax[2].imshow(heatmap_data_a, cmap = 'hot', interpolation = 'nearest')
    ax[2].set_title('Heatmap of Wins for Player A')
    #x and y ticks represent board size
    ax[2].set_xticks(range(BOARD_SIZE))
    ax[2].set_yticks(range(BOARD_SIZE))
    #row and column labels
    ax[2].set_xticklabels(f'Col {c + 1}' for c in range(BOARD_SIZE))
    ax[2].set_yticklabels(f'Row {r + 1}' for r in range(BOARD_SIZE))
    #colorbar shows intensity level
    fig.colorbar(cax_a, ax = ax[2])
    #annotate each cell with value
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            ax[2].annotate(f'{heatmap_data_a[i][j]}', xy=(j, i), ha='center', va='center', color='paleturquoise')

    # display heatmap
    plt.show()


if __name__ == "__main__":
    run_simulations(10000)  # Run __ simulations