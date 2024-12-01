import pygame, sys
import pygame.mixer
from constants import *
from tictactoe import *
from Confetti import *
from music import *
from start_page import *
from game_page import *
from settings_page import *

# initialization
pygame.init()
pygame.mixer.init()
# set screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Let's play our Tic Tac Toe!")
music()

def main():
    while True:
        page = start_page(screen)
        if page == "START_GAME":
            board = initialize_board(BOARD_SIZE)
            chip = 'x'
            game_page(screen, board, chip, BOARD_SIZE, SQUARE_SIZE)
        elif page == "SETTINGS":
            settings_page(screen)
        elif page == "QUIT":
            break

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
