import pygame
import pygame.math as math
import random
from config import *


# Class that controls the player
class Player(pygame.sprite.Sprite):
    def __init__(self, game, pos):
        self.pos = pos
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.Surface([20, 20])
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

    #def draw(self, win):
       # pygame.draw.rect(win, self.colour, self.rect)

    def update(self):
        self.move()
        self.rect.x += self.velX
        self.rect.y += self.velY

        self.velX = 0
        self.velY = 0

        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.x >= DISPLAYW:
            self.rect.x = DISPLAYW -25

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







