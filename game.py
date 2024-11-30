import pygame, sys
import random
import pygame.mixer
from constants import *
from tictactoe import *
from Confetti import *

pygame.init()
pygame.mixer.init()

# set screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Let's play our Tic Tac Toe!")

# set up the BGM
def music():
    pygame.mixer.init()
    try:
        pygame.mixer.music.load("8-bit-retro-game-music-233964.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
    except pygame.error as e:
        print(f"Cannot load BGM...：{e}")


# initialize character
font = pygame.font.Font(None, 50)
small_font = pygame.font.Font(None, 36)

chip_font = pygame.font.Font(None, CHIP_FONT)
game_over_font = pygame.font.Font(None, GAME_OVER_FONT)

# Default grid size
GRID_SIZE = 3
SQUARE_SIZE = WIDTH // GRID_SIZE

def available_square(board, row, col):
    """
    Checks if the specified square on the board is available.
    """
    return board[row][col] == ""

def mark_square(board, row, col, chip):
    """
    Marks the specified square on the board with the player's chip.
    """
    board[row][col] = chip


# Initialize the board based on the grid size
def initialize_board(grid_size):
    return [["" for _ in range(grid_size)] for _ in range(grid_size)]

board = initialize_board(GRID_SIZE)
player = 1
chip = 'x'
game_over = False
winner = 0

def draw_grid():
    # Draw horizontal lines
    for i in range(1, GRID_SIZE):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (0, i * SQUARE_SIZE),
            (WIDTH, i * SQUARE_SIZE),
            LINE_WIDTH
        )

    # Draw vertical lines
    for i in range(1, GRID_SIZE):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (i * SQUARE_SIZE, 0),
            (i * SQUARE_SIZE, HEIGHT),
            LINE_WIDTH
        )

def draw_chips():
    chip_x_surf = chip_font.render("x", 0, CROSS_COLOR)
    chip_o_surf = chip_font.render("o", 0, CIRCLE_COLOR)

    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if board[row][col] == "x":
                chip_x_rect = chip_x_surf.get_rect(
                    center=(col * SQUARE_SIZE + SQUARE_SIZE / 2, row * SQUARE_SIZE + SQUARE_SIZE / 2)
                )
                screen.blit(chip_x_surf, chip_x_rect)
            elif board[row][col] == "o":
                chip_o_rect = chip_o_surf.get_rect(
                    center=(col * SQUARE_SIZE + SQUARE_SIZE / 2, row * SQUARE_SIZE + SQUARE_SIZE / 2)
                )
                screen.blit(chip_o_surf, chip_o_rect)

def get_chip_font(square_size):
    """
    Returns a dynamically sized font based on the square size.
    """
    return pygame.font.Font(None, SQUARE_SIZE // 2)



# set up the start page
def start_page():
    """
    display start page
    """
    # button initialization
    start_button = pygame.Rect(150, 200, 300, 100)
    settings_button = pygame.Rect(150, 350, 300, 100)
    # button text
    start_text = font.render("Start Game", True, WHITE)
    settings_text = font.render("Settings", True, WHITE)

    running = True
    while running:
        # set screen color
        screen.fill(WHITE)

        # draw button
        pygame.draw.rect(screen, BLUE, start_button)
        pygame.draw.rect(screen, ORANGE, settings_button)

        # put start text to centre of the button
        x_start_button = start_button.x + (start_button.width - start_text.get_width()) // 2
        y_start_button = start_button.y + (start_button.height - start_text.get_height()) // 2
        screen.blit(start_text, (x_start_button, y_start_button))

        # put the settings text to the centre of the button
        x_settings_button = settings_button.x + (settings_button.width - settings_text.get_width()) // 2
        y_settings_button = settings_button.y + (settings_button.height - settings_text.get_height()) // 2
        screen.blit(settings_text, (x_settings_button, y_settings_button))

        # event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    return "START_GAME"
                elif settings_button.collidepoint(event.pos):
                    return "SETTINGS"

        pygame.display.update()


# set up the setting page
def settings_page():
    """
    Display the settings page with a Mode button, Back button, and Music button.
    """
    # Calculate button dimensions and spacing
    button_width = 300
    button_height = 60
    button_spacing = 20
    screen_center_x = screen.get_width() // 2
    initial_y = 200

    # Button positions
    mode_button = pygame.Rect(screen_center_x - button_width // 2, initial_y, button_width, button_height)
    back_button = pygame.Rect(screen_center_x - button_width // 2, initial_y + button_height + button_spacing,
                              button_width, button_height)
    music_button = pygame.Rect(screen_center_x - button_width // 2, initial_y + 2 * (button_height + button_spacing),
                               button_width, button_height)

    # Button text
    mode_text = font.render("Game Modes", True, WHITE)
    back_text = font.render("Back to Menu", True, WHITE)
    music_text = font.render("Music", True, WHITE)

    running = True
    while running:
        screen.fill(BG_COLOR)

        # Draw buttons
        pygame.draw.rect(screen, BLUE, mode_button)
        pygame.draw.rect(screen, BLACK, back_button)
        pygame.draw.rect(screen, ORANGE, music_button)

        # Center text on buttons
        screen.blit(mode_text, (mode_button.x + (button_width - mode_text.get_width()) // 2,
                                mode_button.y + (button_height - mode_text.get_height()) // 2))
        screen.blit(back_text, (back_button.x + (button_width - back_text.get_width()) // 2,
                                back_button.y + (button_height - back_text.get_height()) // 2))
        screen.blit(music_text, (music_button.x + (button_width - music_text.get_width()) // 2,
                                 music_button.y + (button_height - music_text.get_height()) // 2))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mode_button.collidepoint(event.pos):
                    mode_page()
                elif back_button.collidepoint(event.pos):
                    return
                elif music_button.collidepoint(event.pos):
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.stop()
                    else:
                        pygame.mixer.music.play(-1)

        pygame.display.flip()


def mode_page():
    """
    Display the game modes page with Normal Mode and Special Mode buttons.
    """
    # Button dimensions
    button_width = 300
    button_height = 60
    button_spacing = 20
    screen_center_x = screen.get_width() // 2
    initial_y = 200

    modes = [("Normal Mode", 200), ("Special Mode", 300), ("3-Player Mode", 400)]

    # Button positions
    normal_mode_button = pygame.Rect(screen_center_x - button_width // 2, initial_y, button_width, button_height)
    special_mode_button = pygame.Rect(screen_center_x - button_width // 2, initial_y + button_height + button_spacing,
                                      button_width, button_height)
    back_button = pygame.Rect(screen_center_x - button_width // 2, initial_y + 2 * (button_height + button_spacing),
                              button_width, button_height)

    # Button text
    normal_mode_text = font.render("Normal Mode", True, WHITE)
    special_mode_text = font.render("Special Mode", True, WHITE)
    back_text = font.render("Back to Settings", True, WHITE)

    running = True
    while running:
        screen.fill(BG_COLOR)

        # Draw buttons
        pygame.draw.rect(screen, BLUE, normal_mode_button)
        pygame.draw.rect(screen, ORANGE, special_mode_button)
        pygame.draw.rect(screen, BLACK, back_button)

        # Center text on buttons
        screen.blit(normal_mode_text, (normal_mode_button.x + (button_width - normal_mode_text.get_width()) // 2,
                                       normal_mode_button.y + (button_height - normal_mode_text.get_height()) // 2))
        screen.blit(special_mode_text, (special_mode_button.x + (button_width - special_mode_text.get_width()) // 2,
                                        special_mode_button.y + (button_height - special_mode_text.get_height()) // 2))
        screen.blit(back_text, (back_button.x + (button_width - back_text.get_width()) // 2,
                                back_button.y + (button_height - back_text.get_height()) // 2))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if normal_mode_button.collidepoint(event.pos):
                    normal_mode_page()
                elif special_mode_button.collidepoint(event.pos):
                    special_mode_page()
                elif back_button.collidepoint(event.pos):
                    return
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for label, y in modes:
                        if y <= event.pos[1] <= y + button_height:
                            if label == "3-Player Mode":
                                three_players()

        pygame.display.flip()


def normal_mode_page():
    """
    Display the Normal Mode page with 3x3, 4x4, and 5x5 buttons, along with a back button.
    """
    # Define the button labels
    labels = ["3x3", "4x4", "5x5", "Back to Modes"]

    # Calculate button dimensions dynamically based on the widest label
    button_width = max([font.size(label)[0] for label in labels]) + 60  # Add padding
    button_height = 60  # Consistent height for all buttons
    button_spacing = 20  # Spacing between buttons
    screen_center_x = screen.get_width() // 2
    initial_y = 200  # Starting y-coordinate for the first button

    # Generate button positions
    buttons = [
        pygame.Rect(screen_center_x - button_width // 2, initial_y + i * (button_height + button_spacing), button_width,
                    button_height)
        for i in range(len(labels))
    ]

    running = True
    while running:
        screen.fill(BG_COLOR)

        # Draw the buttons and labels
        for i, button in enumerate(buttons):
            color = BLUE if i < len(labels) - 1 else BLACK  # Blue for mode buttons, black for the back button
            pygame.draw.rect(screen, color, button)

            # Render text and center it on the button
            text = font.render(labels[i], True, WHITE)
            screen.blit(
                text,
                (
                    button.x + (button.width - text.get_width()) // 2,
                    button.y + (button.height - text.get_height()) // 2,
                ),
            )

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if buttons[-1].collidepoint(event.pos):  # Back button
                    return
                if buttons[0].collidepoint(event.pos):  # 3*3 button
                    reset_game(3)
                    game_page()
                if buttons[1].collidepoint(event.pos):  # 4*4 button
                    reset_game(4)
                    game_page()
                if buttons[2].collidepoint(event.pos):  # 5*5 button
                    reset_game(5)
                    game_page()

        pygame.display.flip()

def special_mode_page():
    """
    Display the Special Mode page with 5x5 for 3 players, Big X and O, and 3D Mode buttons.
    """
    modes = [("5x5 for 3 Players", 200), ("Big X and O", 300), ("3D Mode", 400)]
    button_width = max([font.size(label)[0] + 40 for label, _ in modes])  # Dynamic width based on longest label
    button_height = 60
    button_spacing = 20
    screen_center_x = screen.get_width() // 2

    buttons = [pygame.Rect(screen_center_x - button_width // 2, y, button_width, button_height) for _, y in modes]
    back_button = pygame.Rect(screen_center_x - button_width // 2, modes[-1][1] + button_height + button_spacing,
                              button_width, button_height)

    back_text = font.render("Back to Modes", True, WHITE)

    running = True
    while running:
        screen.fill(BG_COLOR)

        for i, (label, _) in enumerate(modes):
            pygame.draw.rect(screen, ORANGE, buttons[i])
            text = font.render(label, True, WHITE)
            screen.blit(text, (buttons[i].x + (buttons[i].width - text.get_width()) // 2,
                               buttons[i].y + (buttons[i].height - text.get_height()) // 2))

        pygame.draw.rect(screen, BLACK, back_button)
        screen.blit(back_text, (back_button.x + (back_button.width - back_text.get_width()) // 2,
                                back_button.y + (back_button.height - back_text.get_height()) // 2))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, button in enumerate(buttons):
                    if button.collidepoint(event.pos):
                        pass
                        #print(f"Selected {modes[i][0]}")
                if buttons[0].collidepoint(event.pos):  # 3player button
                    three_players()
                if back_button.collidepoint(event.pos):
                    return

        pygame.display.flip()


def use_big_chip(board, row, col, chip):
    if 0 <= row < len(board) and 0 <= col < len(board[row]):
        # set the position to big chips
        board[row][col] = chip.upper()
        print(f"Placed big chip {chip.upper()} at ({row}, {col})")
    else:
        print("Invalid row or col.")


def reset_game(new_grid_size):
    global GRID_SIZE, SQUARE_SIZE, board, player, chip, game_over, winner
    GRID_SIZE = new_grid_size
    SQUARE_SIZE = WIDTH // GRID_SIZE
    # chip_font = pygame.font.Font(None, SQUARE_SIZE // 2)
    board = initialize_board(GRID_SIZE)
    player = 1
    chip = 'x'
    game_over = False
    winner = 0
    screen.fill(BG_COLOR)
    draw_grid()

screen.fill(BG_COLOR)
draw_grid()



def game_page():
    global board  # Ensure that the board state is shared globally
    player = 1  # Current player, 1 or 2
    chip = 'x'  # Current chip, 'x' or 'o'
    player1_big_chip_used = False  # Player 1 Whether to use oversized pieces
    player2_big_chip_used = False  # Player 2 Whether to use oversized pieces

    while True:
        # Clear the screen and draw the board
        screen.fill(BG_COLOR)
        draw_grid()
        draw_chips()

        # Event processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Handle mouse click events (common piece placement)
            if event.type == pygame.MOUSEBUTTONDOWN:#and not game_over
                x, y = event.pos
                row = y // SQUARE_SIZE
                col = x // SQUARE_SIZE

                if available_square(board, row, col):
                    mark_square(board, row, col, chip)
                    if check_if_winner(board, chip):
                        game_over = True
                        winner = player
                    elif board_is_full(board):
                        game_over = True
                        winner = 0  # Indicates tie

                    # Alternate players
                    player = 2 if player == 1 else 1
                    chip = 'o' if chip == 'x' else 'x'

                draw_chips()

            # Handle keyboard press events (large piece placement)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_b:
                # Check if the current player still has large pieces
                if (player == 1 and not player1_big_chip_used) or (player == 2 and not player2_big_chip_used):
                    # Get mouse position
                    x, y = pygame.mouse.get_pos()
                    row = y // SQUARE_SIZE
                    col = x // SQUARE_SIZE

                    # Print debugging information
                    print(f"Player {player} tries to place a big chip at ({row}, {col})")

                    # Check that the position is within the board
                    if 0 <= row < BOARD_ROWS and 0 <= col < BOARD_COLS:
                        # Place a chip piece
                        use_big_chip(board, row, col, chip)

                        # Print checkerboard state
                        print(f"Updated board: {board}")

                        # Mark large pieces used
                        if player == 1:
                            player1_big_chip_used = True
                        else:
                            player2_big_chip_used = True

                        # Draw the board and refresh the display
                        draw_chips()

                        # Check whether large chips lead to victory
                        if check_if_winner(board, chip.upper()):
                            print(f"Player {player} wins with a big chip!")
                            reset_game()
                            return
                    else:
                        print("Cannot put big chip here.")
                player = 2 if player == 1 else 1
                chip = 'o' if chip == 'x' else 'x'

        pygame.display.flip()


def three_players():
    global screen

    players = ['x', 'o', 'a']
    current_player_index = 0
    current_player = players[current_player_index]

    def draw_chips_3(board):
        chip_x_surf = chip_font.render("x", 0, CROSS_COLOR)
        chip_o_surf = chip_font.render("o", 0, CIRCLE_COLOR)
        chip_v_surf = chip_font.render("v", 0, CIRCLE_COLOR)

        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                if board[row][col] == "x":
                    chip_x_rect = chip_x_surf.get_rect(
                        center=(col * SQUARE_SIZE + SQUARE_SIZE / 2, row * SQUARE_SIZE + SQUARE_SIZE / 2)
                    )
                    screen.blit(chip_x_surf, chip_x_rect)
                elif board[row][col] == "o":
                    chip_o_rect = chip_o_surf.get_rect(
                        center=(col * SQUARE_SIZE + SQUARE_SIZE / 2, row * SQUARE_SIZE + SQUARE_SIZE / 2)
                    )
                    screen.blit(chip_o_surf, chip_o_rect)
                elif board[row][col] == "v":
                    chip_v_rect = chip_v_surf.get_rect(
                        center=(col * SQUARE_SIZE + SQUARE_SIZE / 2, row * SQUARE_SIZE + SQUARE_SIZE / 2)
                    )
                    screen.blit(chip_v_surf, chip_v_rect)

    def switch_player():
        nonlocal current_player_index, current_player
        current_player_index = (current_player_index + 1) % 3
        current_player = players[current_player_index]

    def reset_game_3(new_grid_size):
        global GRID_SIZE, SQUARE_SIZE, board, player, chip, game_over, winner
        GRID_SIZE = new_grid_size
        SQUARE_SIZE = WIDTH // GRID_SIZE
        board = initialize_board(GRID_SIZE)
        current_player_index = 0
        player = 1
        chip = players[current_player_index]
        game_over = False
        winner = 0
        screen.fill(BG_COLOR)
        draw_grid()
        pygame.display.update()

    reset_game_3(5)  # 5x5 grid for 3 players mode
    game_over = False
    winner = 0
    draw_chips_3(board)

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                row = event.pos[1] // GRID_SIZE
                col = event.pos[0] // GRID_SIZE

                if is_valid(board, row, col):
                    mark_square(board, row, col, current_player)
                    draw_chips(board)
                    pygame.display.update()

                    if check_if_winner(board, current_player):
                        game_over = True
                        winner = current_player
                    elif board_is_full(board):
                        game_over = True

                    if not game_over:
                        switch_player()

    pygame.time.wait(3000)  # Display game over for 3 seconds


    # Inside your game loop, call switch_player() after every turn.

    # For example, updating the game loop
    player = 1
    chip = players[current_player_index]
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                row = event.pos[1] // SQUARE_SIZE
                col = event.pos[0] // SQUARE_SIZE

                if is_valid(board, row, col):
                    mark_square(board, row, col, current_player)
                    draw_chips(board)
                    pygame.display.update()

                    if check_if_winner(board, current_player):
                        game_over = True
                        winner = current_player
                    elif board_is_full(board):
                        game_over = True

                    if not game_over:
                        switch_player()

    pygame.time.wait(3000)  # Display game over for 3 seconds


    # Switch to the next player
    switch_player()
    chip = players[current_player_index]

    draw_chips_3(board)
    pygame.display.update()





# run the game
def main():
    while True:
        music()
        result = start_page()
        if result == "START_GAME":
            game_page()
        elif result == "SETTINGS":
            settings_page()
        elif result == "QUIT":
            break

    pygame.quit()
    sys.exit()

def draw_game_over():
    screen.fill(BG_COLOR)

    if winner != 0:
        end_text = f"Player {winner} wins!"
    else:
        end_text = "No one wins"

    end_surf = game_over_font.render(end_text, 0, LINE_COLOR)
    end_rect = end_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    screen.blit(end_surf, end_rect)

    restart_text = "Press R to restart the game or 3/4/5 to change grid size"
    restart_surf = game_over_font.render(restart_text, 0, LINE_COLOR)
    restart_rect = restart_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    screen.blit(restart_surf, restart_rect)

if game_over:
    pygame.display.update()
    pygame.time.delay(1000)
    confetti = Confetti()
    confetti.draw()
    draw_game_over()

    pygame.display.update()


if __name__ == "__main__":
    main()
