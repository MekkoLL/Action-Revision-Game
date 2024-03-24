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
        initial_pos = math.Vector2(int(DISPLAYW / 4), int(DISPLAYH / 4))
        self.play = True
        self.moving_sprites = pygame.sprite.Group()
        self.player = Player(self, initial_pos[0], initial_pos[1])
        self.moving_sprites.add(self.player)
        self.static_sprites = pygame.sprite.Group()
        for i in range(15):
            self.treasure = Treasure(self, (random.randrange(0, DISPLAYW - 25, 6)), (random.randrange(0, DISPLAYH - 25, 6)))
            self.static_sprites.add(self.treasure)

    def events(self):
               for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.play = False
                self.run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    moving_sprites.left_pressed = True
                if event.key == pygame.K_RIGHT:
                    moving_sprites.right_pressed = True
                if event.key == pygame.K_UP:
                    moving_sprites.up_pressed = True
                if event.key == pygame.K_DOWN:
                    moving_sprites.down_pressed = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    moving_sprites.left_pressed = False
                if event.key == pygame.K_RIGHT:
                    moving_sprites.right_pressed = False
                if event.key == pygame.K_UP:
                    moving_sprites.up_pressed = False
                if event.key == pygame.K_DOWN:
                    moving_sprites.down_pressed = False

      def update(self):
        self.player.update()

        def draw(self):
        self.player.draw(self.window)
        for sprite in self.static_sprites:
            sprite.draw(self.window)
        self.clock.tick(FPS)
        pygame.display.update()
            
    def main(self):
        background = pygame.image.load('Grass.png')
        while self.play:
            self.events()
            self.window.fill([105, 218, 73])
            self.window.blit(background, [0, 0])
            self.draw()
            self.update()
        self.run = False

    def game_over(self):
        pass

    def menu(self):
        pass
     


def register_login():
    pass


game = Game()
game.menu()

while game.run:
    game.main()
    game.game_over()
pygame.quit()
sys.exit()
