import pygame
import random
from game_par import *
from background import draw_background, add_enemies
from player import Player
from enemy_player import Enemy_Player
from enemy import Enemy, enemies
from assets import *
import time
import sys

# initialize pygame
pygame.init()

def intro_screen(screen):
    intro_text1 = intro_font.render("Welcome to Space Gank!", True, (214, 11, 11))
    intro_text2 = intro_font.render("Objective: Survive", True, (214, 11, 11))
    intro_text3 = intro_font.render("Press Space", True, (214, 11, 11))
    text_rect1 = intro_text1.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    text_rect2 = intro_text2.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + TILE_SIZE))
    text_rect3 = intro_text3.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + TILE_SIZE * 2))

    # load custom images for intro
    star = pygame.image.load("../assets/sprites/star.png")
    planet1 = pygame.image.load("../assets/sprites/planet1.png").convert()
    comet = pygame.image.load("../assets/sprites/comet.png").convert()
    spaceship = pygame.image.load("../assets/sprites/Spaceship.png").convert()

    # set color_key
    planet1.set_colorkey((255, 255, 255))
    comet.set_colorkey((255, 255, 255))
    spaceship.set_colorkey((255, 255, 255))

    running_intro = True
    screen.fill((0, 0, 0))  # Fill screen with black
    for i in range(45):
        x = random.randint(0, SCREEN_WIDTH)
        y = random.randint(0, SCREEN_HEIGHT)
        screen.blit(star, (x, y))
        screen.blit(intro_text1, text_rect1)
        screen.blit(intro_text2, text_rect2)
        screen.blit(intro_text3, text_rect3)
        screen.blit(planet1, (TILE_SIZE * 9, TILE_SIZE * 3))
        screen.blit(comet, (TILE_SIZE * 2, TILE_SIZE * 7))
        screen.blit(spaceship, (TILE_SIZE * 2.5, TILE_SIZE * 2.95))
    pygame.display.flip()
    while running_intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Alone in space")

# Call intro screen
intro_screen(screen)

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

# Draw enemies on the screen
add_enemies(3)

# set number of lives
lives = NUM_LIVES

# start time
start_time = pygame.time.get_ticks() // 1000

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

    # update enemies
    enemies.update()

    # adding and removing enemies from the screen
    for enemy in enemies:  # loop through our fish in the sprite group
        if enemy.rect.x < -enemy.rect.width:  # once the fish leaves the screen it is removed
            enemies.remove(enemy)
            enemies.add(Enemy(random.randint(SCREEN_WIDTH, SCREEN_WIDTH * 2),
                              random.randint(0, SCREEN_HEIGHT - TILE_SIZE * 2 - 3)))

    # check for collisions between player sprite and enemy group sprites
    result = pygame.sprite.spritecollide(player, enemies, True)
    if result:
        lives -= len(result)
        add_enemies(len(result))

    # check for collision with player sprite and enemy player sprite
    result = pygame.sprite.collide_rect(player, enemy_player)
    if result:
        lives -= 3

    # flip player sprite
    player.flip()

    # draw player on screen
    player.draw(screen)

    # draw enemy player on screen
    enemy_player.draw(screen)

    # draw enemies on screen
    enemies.draw(screen)

    # running time
    running_time = pygame.time.get_ticks() // 1000

    # calculate time
    game_time = (running_time - start_time)

    # draw time text
    timer = count_font.render(f"{game_time}", True, (0, 0, 0))
    screen.blit(timer, (10, 10))

    # draw title 2 text
    title = title_font2.render("Space Gank", False, (255, 255, 255))
    screen.blit(title, (SCREEN_WIDTH / 2 - title.get_width() / 2, TILE_SIZE / 2))

    # draw title 1 text
    title = title_font1.render("Space Gank", False, (0,0,0))
    screen.blit(title, (SCREEN_WIDTH / 2 - title.get_width() / 2, TILE_SIZE / 2))

    # Load lives picture
    life_icon = pygame.image.load("../assets/sprites/life_icon.png").convert()
    life_icon.set_colorkey((255, 255, 255))

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
# Alexis Schneider with intro screen