import OpenGL

from OpenGL.GL import *
from OpenGL.GLU import *
from settings import *

# Vertices for Cube (x, y, z)
vertices = (
    (-1, 1, 0), (-1, -1, 0), (1, -1, 0), (1, 1, 0), # Bottom of cube counter clockwise from topleft corner
    (-1, 1, 2), (-1, -1, 2), (1, -1, 2), (1, 1, 2) # Top of cube counter clockwise from topleft corner
)

edges = (
    (0, 1), (0, 4), (0, 3), (1, 2), (1, 5), (4,5),
    (2, 3), (2, 6), (4, 7), (5, 6), (3, 7), (6, 7)
)

# Define colors with respect to RGB between 0 and 1.
'''colors = (
    (RED, BLUE, BLUE, BLUE),
    (RED, BLUE, BLUE, BLUE),
    (RED, BLUE, BLUE, BLUE),
    (BLUE, BLUE, BLUE, BLUE),
    (BLUE, BLUE, BLUE, BLUE),
    (BLUE, BLUE, BLUE, BLUE)
)'''

surfaces = (
    (0, 1, 2, 3),
    (0, 1, 5, 4),
    (0, 3, 7, 4),
    (4, 5, 6, 7),
    (2, 3, 7, 6),
    (1, 2, 6, 5)
)

def Cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

    glBegin(GL_QUADS)
    surface_index = 0
    for surface in surfaces:
        for vertex in surface:
            if vertex == 0:
                glColor3fv(RED)
            elif vertex == 1:
                glColor3fv(WHITE)
            elif vertex == 2:
                glColor3fv(BLUE)
            elif vertex == 3:
                glColor3fv(GREEN)
            elif vertex == 4:
                glColor3fv(BLUE)
            elif vertex == 5:
                glColor3fv(GREEN)
            elif vertex == 6:
                glColor3fv(RED)
            elif vertex == 7:
                glColor3fv(WHITE)

            glVertex3fv(vertices[vertex])
        surface_index += 1
    glEnd()
