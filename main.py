import pygame, sys
from constants import *
from tictactoe import *
import random
import sqlite3
import asyncio


def initialize_game_settings():
    global width
    global height
    global line_width
    global win_line_width
    global board_rows
    global board_cols
    global square_size
    global circle_radius
    global circle_width
    global cross_width
    global space
    global red
    global bg_color
    global line_color
    global circle_color
    global cross_color
    global chip_font
    global game_over_font
    global green
    global blue
    global yellow
    global pink
    global orange
    global purple
    try:
        connection = sqlite3.connect('../gameDb')

        cursor = connection.cursor()

        data = cursor.execute('SELECT width, height, line_width, win_line_width, '
                              'board_rows, board_cols, square_size, circle_radius, '
                              'circle_width, cross_width,space , red, bg_color, '
                              'line_color, circle_color, cross_color, chip_font, '
                              'game_over_font, green, blue, yellow, pink, orange, '
                              'purple FROM game_settings;')
        for row in data:
            print(row)
            width = row[0]
            height = row[1]
            line_width = row[2]
            win_line_width = row[3]
            board_rows = row[4]
            board_cols = row[5]
            square_size = row[6]
            circle_radius = row[7]
            circle_width = row[8]
            cross_width = row[9]
            space = row[10]
            red = row[11]
            bg_color = row[12]
            line_color = row[13]
            circle_color = row[14]
            cross_color = row[15]
            chip_font =row[16]
            game_over_font = row[17]
            green = row[18]
            blue = row[19]
            yellow = row[20]
            pink = row[21]
            orange = row[22]
            purple = row[23]
            # print(f'Data now {width} and {height} and {line_width}')

    # Handle errors
    except sqlite3.Error as error:
        print('Error occurred - ', error)

    # Close DB Connection irrespective of success
    # or failure
    finally:

        if connection:
            connection.close()
            print('SQLite Connection closed')

width = height = line_width = win_line_width = board_rows = board_cols = square_size = circle_radius = circle_width = cross_width = space = chip_font = game_over_font = 0
red = bg_color = line_color = circle_color = cross_color = green = blue = yellow = pink = orange = purple = ''
initialize_game_settings()
# print(f'DB Data now {width} and {height} and {line_width}')

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tic Tac Toe!")


#To draw X and Os
chip_font = pygame.font.Font(None, chip_font)

#initializing the board
board = initialize_board()

class Confetti:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = random.choice([-1,1]) * random.randint(0,1)
        self.dy = random.choice([-1,1]) * random.randint(0,1)
        self.color = random.choice([red, orange, yellow, green, blue, purple, pink])
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
    for i in range(1,board_rows):
        pygame.draw.line(
            screen,
            line_color,
            (0, i * square_size),
            (width, i * square_size),
            line_width
        )
    #draw vertical lines
    for i in range(1, board_cols):
        pygame.draw.line(
            screen,
            line_color,
            (i * square_size, 0),
            (i * square_size, height),
            line_width
        )

def draw_chips():
    chip_x_surf = chip_font.render("x", 0, cross_color)
    chip_o_surf = chip_font.render("o", 0, circle_color)

    for row in range(board_rows):
        for col in range(board_cols):
            if board[row][col] == "x":
                chip_x_rect = chip_x_surf.get_rect(center = (col * square_size + square_size/2, row * square_size + square_size/2))
                screen.blit(chip_x_surf, chip_x_rect)

            elif board[row][col] == "o":
                chip_o_rect = chip_o_surf.get_rect(center = (col * square_size + square_size/2, row * square_size + square_size/2))
                screen.blit(chip_o_surf, chip_o_rect)

def restart_game():
    #restart game by re-initializng board and resetting turn
    global board, current_player, chip
    board = initialize_board()
    current_player = 1
    chip = 'x' #player 1 is x



    # game loop
    screen.fill(bg_color)
    draw_grid()
    draw_chips()

player = 1
chip = 'x'
game_continue = True

async def main():
    while True:

        # game loop
        screen.fill(bg_color)
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
                row = y//square_size
                col = x//square_size


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
                            confetti_list.append(Confetti(random.randint(0, width), random.randint(0, height)))

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
        await asyncio.sleep(0)

asyncio.run(main())
