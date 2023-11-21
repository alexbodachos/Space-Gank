import pygame
import sys
from math import atan2, cos, sin, sqrt

class FollowCursorGame:
    def __init__(self):
        # Initialize Pygame
        pygame.init()

        # Screen dimensions
        self.screen_width, self.screen_height = 800, 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Follow Cursor")

        # Colors
        self.white = (255, 255, 255)
        self.red = (255, 0, 0)

        # Player attributes
        self.player_radius = 20
        self.player_color = self.red
        self.player_x, self.player_y = self.screen_width // 2, self.screen_height // 2
        self.player_speed = 5

        self.clock = pygame.time.Clock()

        self.running = True

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def calculate_movement(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        dx, dy = mouse_x - self.player_x, mouse_y - self.player_y
        distance = sqrt((dx ** 2) + (dy ** 2))

        if distance > self.player_speed:
            angle = atan2(dy, dx)
            self.player_x += self.player_speed * cos(angle)
            self.player_y += self.player_speed * sin(angle)
        else:
            self.player_x, self.player_y = mouse_x, mouse_y

    def run_game(self):
        while self.running:
            self.screen.fill(self.white)

            self.handle_events()
            self.calculate_movement()

            # Draw the player
            pygame.draw.circle(self.screen, self.player_color, (int(self.player_x), int(self.player_y)),
                               self.player_radius)

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()

# Create an instance of the game and run it
game = FollowCursorGame()
game.run_game()
