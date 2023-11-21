import pygame
import random
from game_par import *
from background import draw_background
from player import Player
import sys

# initialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Alone in space")

# Set frame rate
clock = pygame.time.Clock()

# Main loop
running = True
background = screen.copy()
draw_background(background)

# Draw Player
player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

# Load font to count seconds
count_font = pygame.font.Font

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

