import pygame, sys
from tictactoe import *
from Confetti import *

def game_page(screen, board, chip, size, s_size, Big_X_and_O = False):
    global BOARD_SIZE, SQUARE_SIZE 
    BOARD_SIZE = size
    SQUARE_SIZE = s_size
    player1_big_chip_used = False  #check whether player 1 have used the big chip
    player2_big_chip_used = False  #check whether player 2 have used the big chip

    while True:
        #draw the board on screen
        screen.fill(BG_COLOR)
        draw_grid(screen)
        draw_chips(screen, board)

        #event
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #quit game
                pygame.quit()
                sys.exit()

            #check clickings
            if event.type == pygame.MOUSEBUTTONDOWN: #and not game_over
                x, y = event.pos #check the position clicked
                row_num = y // SQUARE_SIZE #divides the y position by squaresize to calculate the row number clicked
                column = x // SQUARE_SIZE #divides the x position by squaresize to calculate the column number clicked

                if available_square(board, row, column): #check if the square d available
                    mark_square(board, row, column, chip) #mark chips that players placed

                    if check_if_winner(board, chip): #check if current player wins
                        return game_over_page(screen, chip) #show game over page if current player wins
                    elif board_is_full(board):#check if the board is full
                        return game_over_page(screen, chip, Tie = True) #if the board is full, show game over page with tie

                    #switch players
                    chip = 'o' if chip == 'x' else 'x'

            if Big_X_and_O == True: #check if big chip mode is on
                #click spce to use big chips!!!!!
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: #chck if space is clicked to use big chips
                    # Check if the current player still has the big chip
                    if (chip == 'x' and not player1_big_chip_used) or (chip == 'o' and not player2_big_chip_used):
                        #get the position clicked
                        x, y = pygame.mouse.get_pos()
                        row = y // SQUARE_SIZE
                        column = x // SQUARE_SIZE
                        #place chip
                        mark_square(board, row, column, chip)
                        #draw the board and display chip
                        draw_chips(screen, board, big_chip = True)
                        print(f"Placed big chip {chip.upper()} at ({row}, {column})")

                        #update the state whether the big chip is used
                        if chip == 'x':
                            player1_big_chip_used = True
                        else:
                            player2_big_chip_used = True

                        #check whether big chip lead to victory
                        if check_if_winner(board, chip): #if victory, show game over page with vistory
                            return game_over_page(screen, chip)
                        #check wether board is full
                        elif board_is_full(board): #if board is full, show game over page with tie
                            return game_over_page(screen, chip, Tie = True)
                        #switch players
                        chip = 'o' if chip == 'x' else 'x'

        pygame.display.flip()


def three_players_game_page(screen, board):
    global BOARD_SIZE, SQUARE_SIZE
    BOARD_SIZE = 5
    SQUARE_SIZE = 120
    players = ['x', 'o', 'a']
    current_player_index = 0
    current_player = players[current_player_index]

    def draw_chips_3(board):
        font = pygame.font.Font(None, 60)
        for row in range(5):
            for col in range(5):
                chip = board[row][col]
                if chip:
                    chip_color = CROSS_COLOR if chip == 'x' else CIRCLE_COLOR if chip == 'o' else GREEN
                    chip_surf = font.render(chip.upper(), True, chip_color)
                    chip_rect = chip_surf.get_rect(
                        center=(col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2))
                    screen.blit(chip_surf, chip_rect)

        pygame.display.update()

    while True:
        screen.fill(BG_COLOR)
        draw_grid(screen)
        draw_chips_3(board)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = event.pos
                clicked_row = mouseY // SQUARE_SIZE
                clicked_col = mouseX // SQUARE_SIZE

                if board[clicked_row][clicked_col] == '-':
                    mark_square(board, clicked_row, clicked_col, current_player)
                    
                    if three_players_check_if_winner(board, current_player):
                        return game_over_page(screen, current_player)
                    
                    if board_is_full(board):
                        return game_over_page(screen, current_player, Tie = True)
                    
                    current_player_index = (current_player_index + 1) % len(players)
                    current_player = players[current_player_index]

            pygame.display.flip()


def game_over_page(screen, chip, Tie = False):
    font = pygame.font.Font(None, 50)
    back_button = pygame.Rect(150, 350, 300, 100)
    back_text = font.render("Back to Menu", True, WHITE)
    
    if Tie == False:
        if chip == 'x':
            result_text = font.render(f'Player 1 (x) wins the game!', True, CROSS_COLOR)
        elif chip == 'o':
            result_text = font.render(f'Player 2 (o) wins the game!', True, CIRCLE_COLOR)
        elif chip == 'a':
            result_text = font.render(f'Player 3 (a) wins the game!', True, GREEN)
        
        confetti_list = []
        for _ in range(100):
            confetti_list.append(Confetti(random.randint(0, WIDTH), random.randint(0, HEIGHT)))
            
    else:
        result_text = font.render('It is a tie!', True, BLACK)
    result_text_rec = result_text.get_rect(center = (300, 200))
        
    while True:
        screen.fill(BG_COLOR)
        screen.blit(result_text, result_text_rec)
        pygame.draw.rect(screen, BLACK, back_button)
        screen.blit(back_text, (300 - back_text.get_width()/2, 400 - back_text.get_height()/2))
        
        if Tie == False:
            for confetti in confetti_list:
                confetti.update()
                confetti.draw(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(event.pos):
                    return
        
        pygame.display.update()


def draw_grid(screen):
    # Draw horizontal lines
    for i in range(1, BOARD_SIZE):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (0, i * SQUARE_SIZE),
            (WIDTH, i * SQUARE_SIZE),
            LINE_WIDTH
        )

    # Draw vertical lines
    for i in range(1, BOARD_SIZE):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (i * SQUARE_SIZE, 0),
            (i * SQUARE_SIZE, HEIGHT),
            LINE_WIDTH
        )


def draw_chips(screen, board, big_chip = False):
    chip_font = pygame.font.Font(None, 400) if big_chip == True else pygame.font.Font(None, 200)
    chip_x_surf = chip_font.render("x", 0, CROSS_COLOR)
    chip_o_surf = chip_font.render("o", 0, CIRCLE_COLOR)

    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == "x":
                chip_x_rect = chip_x_surf.get_rect(
                    center = (col * SQUARE_SIZE + SQUARE_SIZE / 2, row * SQUARE_SIZE + SQUARE_SIZE / 2)
                )
                screen.blit(chip_x_surf, chip_x_rect)
            elif board[row][col] == "o":
                chip_o_rect = chip_o_surf.get_rect(
                    center=(col * SQUARE_SIZE + SQUARE_SIZE / 2, row * SQUARE_SIZE + SQUARE_SIZE / 2)
                )
                screen.blit(chip_o_surf, chip_o_rect)
