import OpenGL

from OpenGL.GL import *
from OpenGL.GLU import *

# Vertex Array Object (VAO)
verticies = (
    (1, -1, -1), (1, 1, -1),
    (-1, 1, -1), (-1, -1, -1),
    (1, -1, 1),  (1, 1, 1),
    (-1, -1, 1), (-1, 1, 1)
)

edges = (
    (0, 1), (0, 3), (0, 4),
    (2, 1), (2, 3), (2, 7),
    (6, 3), (6, 4), (6, 7),
    (5, 1), (5, 4), (5, 7),
)

# Define colors with respect to RGB between 0 and 1.
colors = (
    (1, 0, 0), (0, 1, 0), (0, 0, 1),
    (0, 1, 0), (1, 1, 1), (0, 1, 1),
    (1, 0, 0), (0, 1, 0), (0, 0, 1),
    (1, 0, 0), (1, 1, 1), (0, 1, 1)
)

surfaces = (
    (0, 1, 2, 3), (3, 2, 7, 6), (6, 7, 5, 4),
    (4, 5, 1, 0), (1, 5, 7, 2), (4, 0, 3, 6)
)

def Cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()

    glBegin(GL_QUADS)
    for surface in surfaces:
        x = 0
        for vertex in surface:
            x += 1
            glColor3fv(colors[x])
            glVertex3fv(verticies[vertex])
    glEnd()
