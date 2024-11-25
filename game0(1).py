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

# initialize the board
board = initialize_board()


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

'''
# set up the mode choice page
def mode_page():
    # button area
    three_button = pygame.Rect(150, 100, 300, 80)
    four_button = pygame.Rect(150, 200, 300, 80)
    five_button = pygame.Rect(150, 300, 300, 80)
    five_3player_button = pygame.Rect(150,400, 300, 80)
    # button text
    three_text = font.render("3*3", True, WHITE)
    four_text = font.render("4*4", True, WHITE)
    five_text = font.render("5*5 - 2 players", True, WHITE)
    five_3player_text = font.render('5*5 - 3 players', True, WHITE)

    while True:
        screen.fill(BG_COLOR)

        #draw button
        pygame.draw.rect(screen, BLUE, three_button)
        pygame.draw.rect(screen, BLACK, four_button)
        pygame.draw.rect(screen, ORANGE, five_button)
        pygame.draw.rect(screen, YELLOW, five_3player_button)

        # center button text
        screen.blit(three_text, (
            three_button.x + (three_button.width - three_text.get_width()) // 2,
            three_button.y + (three_button.height - three_text.get_height()) // 2,
        ))
        screen.blit(four_text, (
            four_button.x + (four_button.width - four_text.get_width()) // 2,
            four_button.y + (four_button.height - four_text.get_height()) // 2,
        ))
        screen.blit(five_text, (
            five_button.x + (five_button.width - five_text.get_width()) // 2,
            five_button.y + (five_button.height - five_text.get_height()) // 2,
        ))
        screen.blit(five_3player_text, (
            five_3player_button.x + (five_3player_button.width - five_3player_text.get_width()) // 2,
            five_3player_button.y + (five_3player_button.height - five_3player_text.get_height()) // 2,
        ))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return "QUIT"
            if event.type == pygame.MOUSEBUTTONDOWN:
                global game_mode
                if three_button.collidepoint(event.pos):
                    global result
                    game_mode = "3*3"
                    change_size()
                    game()
                elif four_button.collidepoint(event.pos):
                    game_mode = "4*4"
                    change_size()
                    game()
                    #return "SETTINGS"
                elif five_button.collidepoint(event.pos):
                    game_mode = "5*5"
                    change_size()
                    game()
                elif five_3player_button.collidepoint(event.pos):
                    game_mode = "3player"
                    change_size()
                    game()

        pygame.display.flip()'''
        


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
        #set screen color
        screen.fill(WHITE)

        #draw button
        pygame.draw.rect(screen, BLUE, start_button)
        pygame.draw.rect(screen, ORANGE, settings_button)

        # put start text to centre of the button
        x_start_button = start_button.x + (start_button.width - start_text.get_width()) // 2
        y_start_button = start_button.y + (start_button.height - start_text.get_height()) // 2
        screen.blit(start_text, (x_start_button, y_start_button))

        #put the settings text to the centre of the button
        x_settings_button = settings_button.x + (settings_button.width - settings_text.get_width()) // 2
        y_settings_button = settings_button.y + (settings_button.height - settings_text.get_height()) // 2
        screen.blit(settings_text, (x_settings_button, y_settings_button))

        #event
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
    back_button = pygame.Rect(screen_center_x - button_width // 2, initial_y + button_height + button_spacing, button_width, button_height)
    music_button = pygame.Rect(screen_center_x - button_width // 2, initial_y + 2 * (button_height + button_spacing), button_width, button_height)

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
        
    def change_size():
        global BOARD_COLS, BOARD_ROWS, SQUARE_SIZE, board
        if game_mode == "3*3":
            BOARD_ROWS = 3
            BOARD_COLS = 3
        elif game_mode == "4*4":
            BOARD_ROWS = 4
            BOARD_COLS = 4
        elif game_mode == "5*5":
            BOARD_ROWS = 5
            BOARD_COLS = 5
        elif game_mode == "3player":
            BOARD_ROWS = 5
            BOARD_COLS = 5

        SQUARE_SIZE = WIDTH // BOARD_COLS
        board = initialize_board()


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

    # Button positions
    normal_mode_button = pygame.Rect(screen_center_x - button_width // 2, initial_y, button_width, button_height)
    special_mode_button = pygame.Rect(screen_center_x - button_width // 2, initial_y + button_height + button_spacing, button_width, button_height)
    back_button = pygame.Rect(screen_center_x - button_width // 2, initial_y + 2 * (button_height + button_spacing), button_width, button_height)

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
        pygame.Rect(screen_center_x - button_width // 2, initial_y + i * (button_height + button_spacing), button_width, button_height)
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
                for j, button in enumerate(buttons[:-1]):  # Other buttons
                    if button.collidepoint(event.pos):
                        print(f"Selected {labels[j]}")

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
    back_button = pygame.Rect(screen_center_x - button_width // 2, modes[-1][1] + button_height + button_spacing, button_width, button_height)

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
                        print(f"Selected {modes[i][0]}")
                if back_button.collidepoint(event.pos):
                    return

        pygame.display.flip()
# set up the game page
def draw_grid():
    #draw horizontal lines
    for i in range(1, BOARD_ROWS):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (0, i * SQUARE_SIZE),
            (WIDTH, i * SQUARE_SIZE),
            LINE_WIDTH
        )
    #draw vertical lines
    for i in range(1, BOARD_COLS):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (i * SQUARE_SIZE, 0),
            (i * SQUARE_SIZE, HEIGHT),
            LINE_WIDTH
        )


def draw_chips():
    """
    draw normal chips and big chips
    """
    chip_font = pygame.font.Font(None, CHIP_FONT)

    # normal chips
    chip_x_surf = chip_font.render("x", True, CROSS_COLOR)
    chip_o_surf = chip_font.render("o", True, CIRCLE_COLOR)

    # big chips
    big_chip_x_surf = chip_font.render("X", True, CROSS_COLOR)
    big_chip_o_surf = chip_font.render("O", True, CIRCLE_COLOR)

    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            center = (col * SQUARE_SIZE + SQUARE_SIZE / 2, row * SQUARE_SIZE + SQUARE_SIZE / 2)
            if board[row][col] == "x":
                chip_x_rect = chip_x_surf.get_rect(center=center)
                screen.blit(chip_x_surf, chip_x_rect)
            elif board[row][col] == "o":
                chip_o_rect = chip_o_surf.get_rect(center=center)
                screen.blit(chip_o_surf, chip_o_rect)
            elif board[row][col] == "X":
                big_chip_x_rect = big_chip_x_surf.get_rect(center=center)
                screen.blit(big_chip_x_surf, big_chip_x_rect)
            elif board[row][col] == "O":
                big_chip_o_rect = big_chip_o_surf.get_rect(center=center)
                screen.blit(big_chip_o_surf, big_chip_o_rect)


def use_big_chip(board, row, col, chip):

    if 0 <= row < len(board) and 0 <= col < len(board[row]):
        # set the position to big chips
        board[row][col] = chip.upper()
        print(f"Placed big chip {chip.upper()} at ({row}, {col})")
    else:
        print("Invalid row or col.")


def restart_game():
    global board, player1_big_chip_used, player2_big_chip_used
    board = initialize_board()
    player1_big_chip_used = False
    player2_big_chip_used = False


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
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                row = y // SQUARE_SIZE
                col = x // SQUARE_SIZE

                # Check if you can place common pieces
                if is_valid(board, row, col):
                    mark_square(board, row, col, chip)  # 放置棋子
                    draw_chips()

                    # Check victory condition
                    if check_if_winner(board, chip):
                        print(f"Player {player} wins!")
                        restart_game()
                        return

                    # check tie
                    elif board_is_full(board):
                        print("It's a tie!")
                        restart_game()
                        return

                    # switch player
                    player = 2 if player == 1 else 1
                    chip = 'o' if chip == 'x' else 'x'

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
                            restart_game()
                            return
                    else:
                        print("Cannot put big chip here.")
                player = 2 if player == 1 else 1
                chip = 'o' if chip == 'x' else 'x'

        pygame.display.flip()


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

if __name__ == "__main__":
    main()
