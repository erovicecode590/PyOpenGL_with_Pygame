#=============================================================
# title              : Draw a rotating Cube
# description        : Create a cube with python and OpenGL
# author             : Alan Ramirez
# date               : date
# usage              : python main.py
# python_version     : 3.6.2
#=============================================================

import pygame as pg
import OpenGL
import sys

from pygame.locals import *
from settings import *
from objects import *
from OpenGL.GL import *
from OpenGL.GLU import *

class Game:
    def __init__(self):
        pg.init()
        self.running = True
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode(DISPLAY, DOUBLEBUF|OPENGL)
        gluPerspective(45, (DISPLAY[0]/DISPLAY[1]), 0.1, 50.0)
        glTranslate(0.0, 0.0, -5)

    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def update(self):
        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    def draw(self):
        Cube()
        pg.display.flip()
        pg.time.wait(10)

def start_game():
    g = Game()
    while g.running:
        g.run()
    pg.quit()
    sys.exit()

if __name__ == '__main__':
    start_game()
