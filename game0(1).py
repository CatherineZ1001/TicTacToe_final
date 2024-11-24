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
pygame.display.set_caption("Tic Tac Toe!")

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

    running = True
    while running:
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
                if three_button.collidepoint(event.pos):
                    pass
                elif four_button.collidepoint(event.pos):
                    pass
                    #return "SETTINGS"
                elif five_button.collidepoint(event.pos):
                    pass
                elif five_3player_button.collidepoint(event.pos):
                    pass

        pygame.display.flip()



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
    display settings page
    """
    global BG_COLOR

    # button initialization
    color_button = pygame.Rect(150, 200, 300, 80)
    back_button = pygame.Rect(150, 320, 300, 80)
    music_button = pygame.Rect(150, 440, 300, 80)
    
    # button text
    color_text = font.render("Change Color", True, WHITE)
    back_text = font.render("Back to Menu", True, WHITE)
    music_text = font.render("Music", True, WHITE)

    running = True
    while running:
        screen.fill(BG_COLOR)

        pygame.draw.rect(screen, BLUE, color_button)
        pygame.draw.rect(screen, BLACK, back_button)
        pygame.draw.rect(screen, ORANGE, music_button)

        screen.blit(color_text, (color_button.x + 50, color_button.y + 20))
        screen.blit(back_text, (back_button.x + 50, back_button.y + 20))
        screen.blit(music_text, (music_button.x + 50, music_button.y + 20))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return "QUIT"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if color_button.collidepoint(event.pos):
                    # change bg color
                    BG_COLOR = GREEN if BG_COLOR == WHITE else WHITE
                elif back_button.collidepoint(event.pos):
                    return "BACK"
                elif music_button.collidepoint(event.pos):
                    # change music
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.stop()
                    else:
                        pygame.mixer.music.play(-1)

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
    #To draw X and Os
    chip_font = pygame.font.Font(None, CHIP_FONT)
    
    chip_x_surf = chip_font.render("x", 0, CROSS_COLOR)
    chip_o_surf = chip_font.render("o", 0, CIRCLE_COLOR)

    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == "x":
                chip_x_rect = chip_x_surf.get_rect(center = (col * SQUARE_SIZE + SQUARE_SIZE/2, row * SQUARE_SIZE + SQUARE_SIZE/2))
                screen.blit(chip_x_surf, chip_x_rect)

            elif board[row][col] == "o":
                chip_o_rect = chip_o_surf.get_rect(center = (col * SQUARE_SIZE + SQUARE_SIZE/2, row * SQUARE_SIZE + SQUARE_SIZE/2))
                screen.blit(chip_o_surf, chip_o_rect)

def restart_game():
    result = start_page()

    #restart game by re-initializng board and resetting turn
    global board, current_player, chip
    board = initialize_board()
    current_player = 1
    chip = 'x' #player 1 is x
    
'''
    # game loop
    screen.fill(BG_COLOR)
    draw_grid()
    draw_chips()'''

def game_page():
    player = 1
    chip = 'x'
    confetti_list = []

    while True:

        # game loop
            screen.fill(BG_COLOR)
            draw_grid()
            draw_chips()
                
            #event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    row = y//SQUARE_SIZE
                    col = x//SQUARE_SIZE


                    #check if square is empty
                    if is_valid(board, row, col):
                        #mark square with current chip
                        mark_square(board, row, col, chip)

                        #draw updated board
                        draw_chips()

                    #check for winner
                    if check_if_winner(board, chip):
                        print(f"Player {player} wins!")

                        for _ in range(100):
                            confetti_list.append(Confetti(random.randint(0, WIDTH), random.randint(0, HEIGHT)))
                        for confetti in confetti_list:
                            confetti.update()
                            confetti.draw(screen)
                            
                        #pygame.display.flip()
                        #pygame.time.delay(1000)
                        restart_game()
                        
                        return 'START_GAME'


                    elif board_is_full(board):
                        print("It's a tie!")
                        #pygame.display.update()
                        #pygame.time.delay(10000)

                        restart_game()
                        return 'START_GAME'

                    #switch players after every move
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
