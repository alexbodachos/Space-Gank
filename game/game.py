import pygame
import random
from game_par import *
from background import draw_background
from player import Player
import time
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
count_font = pygame.font.Font("../assets/fonts/game-of-squids/Game Of Squids.ttf", 48)

# Load game title fond
title_font = pygame.font.Font("../assets/fonts/space-age/space age.ttf", 56)

# Load background music
b_sound = pygame.mixer.Sound("../assets/sounds/background.mp3")

# Load lives picture
life_icon = pygame.image.load("../assets/sprites/life_icon.png").convert()
life_icon.set_colorkey((255,255,255))

# set number of lives
lives = NUM_LIVES

# set up the timer
start_time = pygame.time.get_ticks()

while running and lives > 0:
    pygame.mixer.Sound.play(b_sound)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            player.movement()

    # draw background to back of screen
    screen.blit(background,(0,0))

    # draw player on screen
    player.draw(screen)

    # calculate time
    running_time = (pygame.time.get_ticks() - start_time) //1000

    # draw time text
    timer = count_font.render(f"{running_time}", True, (0, 0, 0))
    screen.blit(timer, (10, 10))

    # flip screen
    pygame.display.flip()

    # set frame rate
    clock.tick(60)

# quit pygame
pygame.quit()

