import pygame
import random
from game_par import *
from background import draw_background
from player import Player
from enemy_player import Enemy_Player
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

# Draw enemy player
enemy_player = Enemy_Player(TILE_SIZE, TILE_SIZE)

# Load font to count seconds
count_font = pygame.font.Font("../assets/fonts/game-of-squids/Game Of Squids.ttf", 48)

# Load game title font 1
title_font1 = pygame.font.Font("../assets/fonts/space-age/space age.ttf", 60)

# Load game title font 2
title_font2 = pygame.font.Font("../assets/fonts/space-age/space age.ttf", 62)

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
        elif event.type == pygame.MOUSEMOTION:
            player.movement()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("You pressed the key up key")
                enemy_player.move_up()
            if event.key == pygame.K_DOWN:
                print("You pressed the key down key")
                enemy_player.move_down()
            if event.key == pygame.K_LEFT:
                print("You pressed the key left key")
                enemy_player.move_left()
            if event.key == pygame.K_RIGHT:
                print("You pressed the key right key")
                enemy_player.move_right()
        elif event.type == pygame.KEYUP:
            enemy_player.stop()

    # draw background to back of screen
    screen.blit(background,(0,0))

    # update player position
    player.update()

    # update enemy player position
    enemy_player.update()

    # flip player sprite
    player.flip()

    # draw player on screen
    player.draw(screen)

    # draw enemy player on screen
    enemy_player.draw(screen)

    # calculate time
    running_time = (pygame.time.get_ticks()) // 1000

    # draw time text
    timer = count_font.render(f"{running_time}", True, (0, 0, 0))
    screen.blit(timer, (10, 10))

    # draw title 2 text
    title = title_font2.render("Space Gank", False, (255, 255, 255))
    screen.blit(title, (SCREEN_WIDTH / 2 - title.get_width() / 2, TILE_SIZE / 2))

    # draw title 1 text
    title = title_font1.render("Space Gank", False, (0,0,0))
    screen.blit(title, (SCREEN_WIDTH / 2 - title.get_width() / 2, TILE_SIZE / 2))

    # draw life icon backdrop
    pygame.draw.rect(screen, black, (0, 576, 96, 32))

    # draw life icons
    for i in range(lives):
        screen.blit(life_icon, (i * TILE_SIZE / 2, SCREEN_HEIGHT - TILE_SIZE))

    # flip screen
    pygame.display.flip()

    # set frame rate
    clock.tick(60)

# quit pygame
pygame.quit()

# TODO Helping Hand
# Ryan Flaherty with clock
# Ryan Flaherty with background dirt spawn