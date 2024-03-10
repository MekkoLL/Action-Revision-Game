import pygame
from sprites import *
import sys
import pygame.math as math
from config import *


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((DISPLAYW, DISPLAYH))
        pygame.display.set_caption('Action!')
        self.clock = pygame.time.Clock()
        self.run = True
        self.play()



    def play(self):
        initial_pos = math.Vector2(int(DISPLAYW / 4), int(DISPLAYH / 4))
        self.play = True
        self.sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemy = pygame.sprite.LayeredUpdates()
        self.player = Player(self, initial_pos)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.play = False
                self.run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.left_pressed = True
                if event.key == pygame.K_RIGHT:
                    self.player.right_pressed = True
                if event.key == pygame.K_UP:
                    self.player.up_pressed = True
                if event.key == pygame.K_DOWN:
                    self.player.down_pressed = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.player.left_pressed = False
                if event.key == pygame.K_RIGHT:
                    self.player.right_pressed = False
                if event.key == pygame.K_UP:
                    self.player.up_pressed = False
                if event.key == pygame.K_DOWN:
                   self.player.down_pressed = False

    def update(self):
        self.sprites.update()

    def draw(self):
        self.sprites.draw(self.window)
        self.clock.tick(FPS)
        pygame.display.update()

    def main(self):
        background = pygame.image.load('Grass.png')
        while self.play:
            self.events()
            self.window.fill([255, 255, 255])
            self.window.blit(background, [0, 0])
            self.draw()
            self.update()
        self.run = False

    def game_over(self):
        pass

    def menu(self):
        pass


game = Game()
game.menu()

while game.run:
    game.main()
    game.game_over()
pygame.quit()
sys.exit()
