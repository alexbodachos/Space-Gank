import pygame
import sys
from math import atan2, cos, sin, sqrt

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Follow Cursor")

# Colors
white = (255, 255, 255)
red = (255, 0, 0)

# Player attributes
player_radius = 20
player_color = red
player_x, player_y = screen_width // 2, screen_height // 2
player_speed = 5

clock = pygame.time.Clock()

running = True
while running:
    screen.fill(white)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the position of the mouse cursor
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Calculate the distance between the player and the cursor
    dx, dy = mouse_x - player_x, mouse_y - player_y
    distance = ((dx ** 2) + (dy ** 2)) ** 0.5

    # Move the player towards the cursor
    if distance > player_speed:
        angle = atan2(dy, dx)
        player_x += player_speed * cos(angle)
        player_y += player_speed * sin(angle)
        print(player_x, player_y)
    else:
        player_x, player_y = mouse_x, mouse_y

    # Draw the player
    pygame.draw.circle(screen, player_color, (int(player_x), int(player_y)), player_radius)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
