# jumpy platform game

import pygame as pg
import random
from settings import *


class Game:
    def __init__(self):
        #initilize game window, etc
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("My Game")
        self.clock = pg.time.Clock()
        self.running = True

    def new(self):
        # start a new game
        self.all_sprites = pg.sprite.Group()

    def run(self):
        # Game loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()


    def update(self):
        #Game loop: update
        self.all_sprites.update()

    def events(self):
        # Game loop: events
        for event in pg.event.get():
            # check for closing the window
            if event.type == pg.QUIT:
                if self.playing == False:
                    self.running = False

    def draw(self):
        #game loop: Draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        # *after drawing everything, flip the display
        pygame.display.flip()

    def show_start_screen(self):
        # game splash/start screen
        pass

    def show_go_screen(self):
        #show game over screen
        pass

g = Game()
g.show_start_screen()

while g.running:
    g.new()
    g.show_go_screen()

pg.quit()


