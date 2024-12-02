import pygame.mixer

# set up the BGM
def music():
    pygame.mixer.init() #initialize the audio system to play music
    try:
        pygame.mixer.music.load("8-bit-retro-game-music-233964.mp3")
        pygame.mixer.music.set_volume(0.5) #set volume
        pygame.mixer.music.play(-1) #music will loop infinitely if not stopped manually
    except pygame.error as e: #handle pygame error
        print(f"Cannot load BGM...：{e}")
