import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import pygame
from pygame.locals import *

from lsystem import *
from lsystems.lsystem3d import *


WIDTH = 1900
HEIGHT = 1200


WHITE = pygame.Color(255, 255, 255)
BLACK = pygame.Color(0, 0, 0)



def displaytree(lp, div, off):
    glLineWidth(3)
    glBegin(GL_LINES)
    for l, depth in lp:
        sx, sy, sz = l.end1
        ex, ey, ez = l.end2
        glColor3f((88 - min(80, 10*depth)) /320, (41 + min(160, 40 * depth))/320, 0)
        glVertex3fv((sx/div, sy/div-off, sz/div))
        glVertex3fv((ex/div, ey/div-off, ez/div))
    glEnd()



if __name__ == "__main__":
    pygame.init()
    choice  = None
    lsys = None
    while choice not in [str(i) for i in range(1, 3)]:
        print("Choose one\n1) Tree 1\n2) Tree 2\n")
        choice = input()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill(WHITE)
    match int(choice):
        case 1: 
            lsys = tree3d0
        case 2:
            lsys = tree3d1
    display = (1200,900)
    screen = pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    glClearColor(1, 1, 1, 0) 
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0,0.0, -5)
    lsys = tree3d0
    gen = generation(lsys.axiom, lsys.rules, 4)
    lp = axiomtoline3drand(gen, (0, 0, 0), lsys, 15)   
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        glRotatef(1, 0, 1, 0)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        displaytree(lp, 100, 2)
        pygame.display.flip()
        pygame.time.wait(20)

