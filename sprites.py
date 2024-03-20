import pygame
import pygame.math as math
import random

import pygame.sprite

from config import *



class Base_character(pygame.sprite.Sprite):
    def __init__(self, game, pos):
        pygame.sprite.Sprite.__init__(self)
        self.pos = pos
        self.game = game


    def update(self):
        pass

    def move(self):
        pass


# Class that controls the player
class Player(Base_character):

    def __init__(self, game, pos):
        super().__init__(game, pos)
        self.pos = pos
        self.game = game
        self._layer = PLAYER_LAYER
        self.image = pygame.Surface([21, 24])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y
        self.velX = 0
        self.velY = 0
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.speed = 5

    def update(self):
        self.move()
        self.rect.x += self.velX
        self.rect.y += self.velY

        self.velX = 0
        self.velY = 0

        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.x >= DISPLAYW:
            self.rect.x = DISPLAYW - 25

        if self.rect.y <= 0:
            self.rect.y = 0
        elif self.rect.y >= DISPLAYH:
            self.rect.y = DISPLAYH - 25

    def move(self):
        self.velX = 0
        self.velY = 0
        if self.left_pressed and not self.right_pressed:
            self.velX = -self.speed
        if self.right_pressed and not self.left_pressed:
            self.velX = self.speed
        if self.up_pressed and not self.down_pressed:
            self.velY = -self.speed
        if self.down_pressed and not self.up_pressed:
            self.velY = self.speed

        self.pos.x += self.velX
        self.pos.y += self.velY

        if self.pos.x < 0:
            self.pos.x = 0
        elif self.pos.x > DISPLAYW:
            self.pos.x = DISPLAYW
        if self.pos.y < 0:
            self.pos.y = 0
        elif self.pos.y > DISPLAYH:
            self.pos.y = DISPLAYH

        self.rect = pygame.Rect(int(self.pos.x), int(self.pos.y), 32, 32)



class Treasure(Base_character):
        def __init__(self, game):
            super().__init__(game)
            self.game = game
            self._layer = TREASURE_LAYER
            self.image = pygame.Surface([20, 20])
            self.image.fill(YELLOW)
            self.rect = self.image.get_rect()
            self.x = random.randrange(0, DISPLAYW, 1)
            self.y = random.randrange(0, DISPLAYH, 1)

            self.rect = pygame.Rect(int(self.x), int(self.y), 20, 20)








