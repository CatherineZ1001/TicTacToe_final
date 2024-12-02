import pygame, sys
from tictactoe import *
from game_page import *

#create the setting page
def settings_page(screen):
    """
    display the settings page with mode button, back button, and music button.
    """
    #set size of button and spacing
    button_width = 300
    button_height = 60
    spacing = 20
    #set y of the first button, the normal mode button
    y = 150
    #set font of text
    font = pygame.font.Font(None, 30) #use default font and size 30 for text

    #place buttons
    x = 300 - button_width // 2 #put the buttons to the center in one column, x of buttons are the same
    normal_modes_button = pygame.Rect(x, y, button_width, button_height)
    #y of special mode button = y + button_height + spacing
    special_modes_button = pygame.Rect(x, y + button_height + spacing,
                                       button_width, button_height)
    #y of music button = y + 2*(button_height + spacing)
    music_button = pygame.Rect(x, y + 2*(button_height + spacing),
                              button_width, button_height)
    #y of back button = y + 3*(button_height + spacing)
    back_button = pygame.Rect(x, y + 3*(button_height + spacing),
                               button_width, button_height)

    #draw button text with white color
    normal_modes_text = font.render("Normal Game Modes", True, WHITE)
    special_modes_text = font.render("Special Game Modes", True, WHITE)
    music_text = font.render("Music", True, WHITE)
    back_text = font.render("Back to Menu", True, WHITE)

    while True:
        screen.fill(BG_COLOR)

        #draw buttons with different colors
        pygame.draw.rect(screen, BLUE, normal_modes_button)
        pygame.draw.rect(screen, PURPLE, special_modes_button)
        pygame.draw.rect(screen, ORANGE, music_button)
        pygame.draw.rect(screen, BLACK, back_button)

        #center the text on buttons
        #x of normal mode text = normal_modes_button.x + (button_width - normal_modes_text.get_width()) // 2
        #y of normal mode text = normal_modes_button.y + (button_height - normal_modes_text.get_height()) // 2
        screen.blit(normal_modes_text, (normal_modes_button.x + (button_width - normal_modes_text.get_width()) // 2,
                                normal_modes_button.y + (button_height - normal_modes_text.get_height()) // 2))

        #x of special mode text = special_modes_button.x + (button_width - special_modes_text.get_width()) // 2
        #y of special mode text = special_modes_button.y + (button_height - normal_modes_text.get_height()) // 2
        screen.blit(special_modes_text, (special_modes_button.x + (button_width - special_modes_text.get_width()) // 2,
                        special_modes_button.y + (button_height - normal_modes_text.get_height()) // 2))

        #x of music text = music_button.x + (button_width - music_text.get_width()) // 2
        #y of music text = music_button.y + (button_height - music_text.get_height()) // 2
        screen.blit(music_text, (music_button.x + (button_width - music_text.get_width()) // 2,
                                 music_button.y + (button_height - music_text.get_height()) // 2))

        #x of back text = back_button.x + (button_width - back_text.get_width()) // 2
        #y of back text = back_button.y + (button_height - back_text.get_height()) // 2
        screen.blit(back_text, (back_button.x + (button_width - back_text.get_width()) // 2,
                        back_button.y + (button_height - back_text.get_height()) // 2))
        #event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit() #quit game
            if event.type == pygame.MOUSEBUTTONDOWN:
                if normal_modes_button.collidepoint(event.pos): #open normal mode page
                    normal_modes_page(screen)
                elif special_modes_button.collidepoint(event.pos): #open special mode page
                    special_modes_page(screen)
                elif music_button.collidepoint(event.pos): #stop or restart music
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.stop()
                    else:
                        pygame.mixer.music.play(-1) #loop music indefinitely
                elif back_button.collidepoint(event.pos): #check if back button is clicked
                    return

        pygame.display.flip()


def normal_modes_page(screen):
    """
    display the Normal Mode page with 3x3, 4x4, and 5x5 buttons,and the back button.
    """
    #draw the buttons
    global BOARD_SIZE, SQUARE_SIZE
    button_labels = ["3x3", "4x4", "5x5", "Back to Modes"]
    font = pygame.font.Font(None, 30)

    button_width = 300 #set button width to 300
    button_height = 60  #set button height to 60
    spacing = 20  #set spacing to 20
    screen_center_x = 300
    initial_y = 150  # Starting y-coordinate for the first button

    # Generate button positions
    buttons = [
        pygame.Rect(screen_center_x - button_width // 2, initial_y + i * (button_height + spacing), button_width,
                    button_height)
        for i in range(len(button_labels))
    ]

    while True:
        screen.fill(BG_COLOR)

        # Draw the buttons and labels
        for i, button in enumerate(buttons):
            color = BLUE if i < len(button_labels) - 1 else BLACK  # Blue for mode buttons, black for the back button
            pygame.draw.rect(screen, color, button)

            # Render text and center it on the button
            text = font.render(button_labels[i], True, WHITE)
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
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if buttons[-1].collidepoint(event.pos):  #Back button
                    return
                if buttons[0].collidepoint(event.pos):  #3*3 button
                    board = initialize_board(3)
                    chip = 'x'
                    game_page(screen, board, chip, 3, 200)
                if buttons[1].collidepoint(event.pos):  #4*4 button
                    board = initialize_board(4)
                    chip = 'x'
                    game_page(screen, board, chip, 4, 150)
                if buttons[2].collidepoint(event.pos):  #5*5 button
                    board = initialize_board(5)
                    chip = 'x'
                    game_page(screen, board, chip, 5, 120)

        pygame.display.flip()


def special_modes_page(screen):
    """
    Display the Special Mode page with 5x5 for 3 players and Big X and O
    """
    labels = ["Big X and O", "5x5 for 3 Players", "Back to Menu"]
    button_width = 300
    button_height = 60
    button_spacing = 20
    screen_center_x = 300
    initial_y = 190
    font = pygame.font.Font(None, 50)

    # Generate button positions
    buttons = [
        pygame.Rect(screen_center_x - button_width // 2, initial_y + i * (button_height + button_spacing), 
                    button_width, button_height)
        for i in range(len(labels))
    ]

    while True:
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

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if buttons[0].collidepoint(event.pos):
                    board = initialize_board(3)
                    chip = 'x'
                    game_page(screen, board, chip, 3, 200, Big_X_and_O = True)
                elif buttons[1].collidepoint(event.pos): # 3player button
                    board = initialize_board(5)
                    three_players_game_page(screen, board)
                elif buttons[-1].collidepoint(event.pos):
                    return
                
        pygame.display.flip()
