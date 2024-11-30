import pygame
import random #generate random values
from constants import * #import the colors

class Confetti:
    def __init__(self, x, y):#initialize confetti particles
        #Horizontal position of confetti
        self.x = x
        #vertical position of confetti
        self.y = y
        #random horizontal & vertical movements
        self.dx = random.choice([-1,1]) * random.randint(0,1)
        self.dy = random.choice([-1,1]) * random.randint(0,1)
        #assigns color
        self.color = random.choice([RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE, PINK])
        #gives gravity effect of particles going down the screen
        self.gravity = 0.001

    def update(self):
        #updated x and y using velocity
        self.x += self.dx
        self.y += self.dy
        self.dy += self.gravity

    def draw(self, screen):
        #draws rectangle at certain position
        pygame.draw.rect(screen, self.color, (self.x, self.y, 5, 5))