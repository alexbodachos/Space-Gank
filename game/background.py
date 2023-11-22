import pygame
import random
from game_par import *

def draw_background(screen):

    # load tiles
    ground = pygame.image.load("../assets/sprites/crater1.png").convert()
    lava1 = pygame.image.load("../assets/sprites/lava1.png").convert()
    lava2 = pygame.image.load("../assets/sprites/lava2.png").convert()

    # use png transparency
    ground.set_colorkey((0,0,0))
    lava1.set_colorkey((0,0,0))
    lava2.set_colorkey((0,0,0))

    # fill the screen with the planet
    for x in range(0, SCREEN_WIDTH, TILE_SIZE):
        for y in range(0, SCREEN_HEIGHT, TILE_SIZE):
            screen.blit(ground, (x,y))

    for z in range(3):
        x = random.randint(0, SCREEN_WIDTH)
        y = random.randint(0, SCREEN_HEIGHT)
        screen.blit(lava1, (x,y))

    for z in range(3):
        x = random.randint(0, SCREEN_WIDTH)
        y = random.randint(0, SCREEN_HEIGHT)
        screen.blit(lava2, (x, y))