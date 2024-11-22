import pygame
import random
from constants import *

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

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, 5, 5))