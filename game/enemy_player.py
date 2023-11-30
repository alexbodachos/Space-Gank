import pygame
from game_par import *

class Enemy_Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.forward_image = pygame.image.load("../assets/sprites/monster1.png").convert()
        self.forward_image.set_colorkey((255, 255, 255))
        self.image = self.forward_image
        self.reverse_image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x, y)
        self.x_speed = 0
        self.y_speed = 0

    def move_up(self):
        self.y_speed = -1 * ENEMY_PLAYER_SPEED
    def move_down(self):
        self.y_speed = ENEMY_PLAYER_SPEED

    def move_left(self):
        self.x_speed = -1 * ENEMY_PLAYER_SPEED
        self.image = self.reverse_image

    def move_right(self):
        self.x_speed = ENEMY_PLAYER_SPEED
        self.image = self.forward_image

    def stop(self):
        self.x_speed = 0
        self.y_speed = 0

    def update(self):
        self.x += self.x_speed
        self.y += self.y_speed
        self.rect.x = self.x
        self.rect.y = self.y
        if self.x <= 0:
            self.x = 0
        if self.x >= 832:
            self.x = 832
        if self.y <= 0:
            self.y = 0
        if self.y >= 640:
            self.y = 640

    def draw(self, screen):
        screen.blit(self.image, self.rect)