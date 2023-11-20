import pygame
import random
import sys

pygame.init()

# screen dimensions
SCREEN_WIDTH = 832
SCREEN_HEIGHT = 640
TILE_SIZE = 64

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Alone in space")

# Function to draw background
def draw_background(screen):

    # load tiles
    ground = pygame.image.load("assets/sprites/crater1.png").convert()
    lava1 = pygame.image.load("assets/sprites/lava1.png").convert()
    lava2 = pygame.image.load("assets/sprites/lava2.png").convert()

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

# Main loop
running = True
background = screen.copy()
draw_background(background)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # draw background to back of screen
    screen.blit(background,(0,0))

    # flip screen
    pygame.display.flip()

# quit pygame
pygame.quit()

