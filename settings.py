import pygame as pg

from pygame.locals import *

# Define window/display properties.
WIDTH   = 1280
HEIGHT  = 720
DISPLAY = (WIDTH, HEIGHT)
Y_FOV_ANGLE = 50 # Field of view angle with respect to y
ASPECT_RATIO = 2 # Aspect ratio = width/height
Z_NEAR = 1.0 # Distance from viewer to near clipping plane.
Z_FAR = 50.0 # Distance from viewer to far clipping plane.

FPS = 60 # Frames per second.

# Define Colors with
BLACK = (0, 0,0)
WHITE = (1, 1, 1)
RED = (1, 0, 0)
GREEN = (0, 1, 0)
BLUE = (0, 0, 1)
