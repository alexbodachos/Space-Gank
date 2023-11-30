import pygame
import random
from game_par import *
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.image.load("../assets/sprites/monster2.png").convert()
        self.image.set_colorkey((255, 255, 255))
        self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speed = MAX_SPEED
        self.rect.center = (x, y)

    def update(self):
        # update the x position of the fish
        self.x -= self.speed
        self.rect.x = self.x

    def draw(self, surf):
        surf.blit(self.image, self.rect)

enemies = pygame.sprite.Group()