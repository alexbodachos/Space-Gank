import pygame
from game_par import *
from player_sprite import player_sprite1, player_sprite2, player_sprite3, player_sprite4
from math import atan2, cos, sin, sqrt

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.forward_image = player_sprite1
        self.forward_image.set_colorkey((0, 0, 0))
        self.image = self.forward_image
        self.reverse_image = pygame.transform.flip(self.image, True, False)
        self.player_x = x
        self.player_y = y
        self.rect = self.player_x, self.player_y
        self.speed = 5

    def movement(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        dx = mouse_x - self.player_x
        dy = mouse_y - self.player_y
        distance = sqrt((dx ** 2) + (dy ** 2))

        if distance > self.speed:
            angle = atan2(dy, dx)
            self.player_x += self.speed * cos(angle)
            self.player_y += self.speed * sin(angle)
        else:
            self.player_x, self.player_y = mouse_x, mouse_y

    def update(self):
        self.rect = self.player_x, self.player_y
        if self.player_x <= 0:
            self.player_x = 0
        if self.player_x >= (SCREEN_WIDTH - TILE_SIZE):
            self.player_x = (SCREEN_WIDTH - TILE_SIZE)
        if self.player_y <= 0:
            self.player_y = 0
        if self.player_y >= (SCREEN_HEIGHT - TILE_SIZE * 2):
            self.player_y = (SCREEN_HEIGHT - TILE_SIZE * 2)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
