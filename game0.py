import pygame, sys
from constants import *
from tictactoe import *
import random
import pygame
import pygame.mixer
pygame.mixer.init()


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe!")

#
#
#
#
#
import pygame

pygame.init()

# size and color
WIDTH, HEIGHT = 600, 600
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
ORANGE = (236, 106, 44)
BG_COLOR = WHITE

# set screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe!")

# initialize character
font = pygame.font.Font(None, 50)
small_font = pygame.font.Font(None, 36)

# bgm
BGM_PATH = "8-bit-retro-game-music-233964.mp3"

def start_page():
    """
    display start page
    """
    # button area
    start_button = pygame.Rect(150, 200, 300, 100)
    settings_button = pygame.Rect(150, 350, 300, 100)

    running = True
    while running:
        screen.fill(WHITE)

        #draw button
        pygame.draw.rect(screen, BLUE, start_button)
        pygame.draw.rect(screen, ORANGE, settings_button)

        # text color
        start_text = font.render("Start Game", True, WHITE)
        settings_text = font.render("Settings", True, WHITE)

        # center button text
        screen.blit(start_text, (
            start_button.x + (start_button.width - start_text.get_width()) // 2,
            start_button.y + (start_button.height - start_text.get_height()) // 2,
        ))
        screen.blit(settings_text, (
            settings_button.x + (settings_button.width - settings_text.get_width()) // 2,
            settings_button.y + (settings_button.height - settings_text.get_height()) // 2,
        ))

        #event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return "QUIT"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    return "START_GAME"
                elif settings_button.collidepoint(event.pos):
                    return "SETTINGS"

        pygame.display.flip()


#
BG_COLOR = WHITE

def settings_page():
    """
    display settings page
    """
    global BG_COLOR

    color_button = pygame.Rect(150, 200, 300, 80)
    back_button = pygame.Rect(150, 320, 300, 80)
    music_button = pygame.Rect(150, 440, 300, 80)

    running = True
    while running:
        screen.fill(BG_COLOR)

        pygame.draw.rect(screen, BLUE, color_button)
        pygame.draw.rect(screen, BLACK, back_button)
        pygame.draw.rect(screen, ORANGE, music_button)

        # button text
        color_text = font.render("Change Color", True, WHITE)
        back_text = font.render("Back to Menu", True, WHITE)
        music_text = font.render("Music", True, WHITE)

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
                    BG_COLOR = (0, 255, 0) if BG_COLOR == WHITE else WHITE
                elif back_button.collidepoint(event.pos):
                    return "BACK"
                elif music_button.collidepoint(event.pos):
                    # change music
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.stop()
                    else:
                        pygame.mixer.music.play(-1)

        pygame.display.flip()


"""
def game():
    
    
    
    running = True
    while running:
        screen.fill(BG_COLOR)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
"""
def music():
    pygame.mixer.init()
    try:
        pygame.mixer.music.load(BGM_PATH)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
    except pygame.error as e:
        print(f"Cannot load BGM...：{e}")

def main():

    while True:
        music()
        result = start_page()
        if result == "START_GAME":
            game()
        if result == "SETTINGS":
            settings_page()
        elif result == "QUIT":
            break

    pygame.quit()
    sys.exit()




#
#
#
#
#


#To draw X and Os
chip_font = pygame.font.Font(None, CHIP_FONT)

#initializing the board
board = initialize_board()

class Confetti:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = random.choice([-1,1]) * random.randint(0,1)
        self.dy = random.choice([-1,1]) * random.randint(0,1)
        self.color = random.choice([RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE, PINK])
        self.gravity = 0.001

    def update(self):
        self.x += self.dx
        self.y += self.dy
        self.dy += self.gravity

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, 5,5))

confetti_list = []


def draw_grid():
    #draw horizontal lines
    for i in range(1,BOARD_ROWS):
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

    # game loop
    screen.fill(BG_COLOR)
    draw_grid()
    draw_chips()


def game():
    player = 1
    chip = 'x'
    game_continue = True

    while True:

        # game loop
            screen.fill(BG_COLOR)
            draw_grid()
            draw_chips()

            for confetti in confetti_list:
                confetti.update()
                confetti.draw()
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

                        pygame.display.update()
                        pygame.time.delay(1000)

                        restart_game()


                    elif board_is_full(board):
                        print("It's a tie!")
                        pygame.display.update()
                        pygame.time.delay(1000)

                        restart_game()

                    #switch players after every move
                    player = 2 if player == 1 else 1
                    chip = 'o' if chip == 'x' else 'x'


            pygame.display.update()

if __name__ == "__main__":
    main()