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
count_font = pygame.font.Font("../assets/fonts/game-of-squids/Game Of Squids.ttf")

# Load game title fond
title_font = pygame.font.Font("../assets/fonts/space-age/space age.ttf")

# Load background music
b_sound = pygame.mixer.Sound("../assets/sounds/background.mp3")

# Load lives picture
life_icon = pygame.image.load("../assets/sprites/life_icon.png").convert()
life_icon.set_colorkey((255,255,255))

# set number of lives
lives = NUM_LIVES

while running and lives > 0:
    pygame.mixer.Sound.play(b_sound)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # draw background to back of screen
    screen.blit(background,(0,0))

    # flip screen
    pygame.display.flip()

# quit pygame
pygame.quit()

