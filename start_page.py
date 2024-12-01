import pygame, sys
from constants import *

#create the start page
def start_page(screen):
    """
    display start page with start button and settings button
    """
    #place start button and settings button
    start_button = pygame.Rect(150, 200, 300, 100)
    settings_button = pygame.Rect(150, 350, 300, 100)
    #draw text of start button and settings button
    font = pygame.font.Font(None, 50)
    start_text = font.render("Start Game", True, WHITE)
    settings_text = font.render("Settings", True, WHITE)

    while True:
        #set screen color
        screen.fill(WHITE)

        #draw start button and settings button
        pygame.draw.rect(screen, BLUE, start_button)
        pygame.draw.rect(screen, ORANGE, settings_button)

        #put 'Start Game' to centre of the start button
        x_start_button = start_button.x + (start_button.width - start_text.get_width()) // 2
        y_start_button = start_button.y + (start_button.height - start_text.get_height()) // 2
        screen.blit(start_text, (x_start_button, y_start_button))

        #put the 'Settings' to the centre of the settings button
        x_settings_button = settings_button.x + (settings_button.width - settings_text.get_width()) // 2
        y_settings_button = settings_button.y + (settings_button.height - settings_text.get_height()) // 2
        screen.blit(settings_text, (x_settings_button, y_settings_button))

        #event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):#click 'Start Game' button to start game.py
                    return "START_GAME"
                elif settings_button.collidepoint(event.pos):#click 'Settings' button directing to settings
                    return "SETTINGS"

        pygame.display.update()