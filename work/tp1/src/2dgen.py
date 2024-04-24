import pygame
from lsystem import *
from lsystems.lsystem2d import *
from drawing.line import Line


WIDTH = 1900
HEIGHT = 1000

WHITE = pygame.Color(255, 255, 255)
BLACK = pygame.Color(0, 0, 0)



def draw(x, y, n, lsys):   
    gen = generation(lsys.axiom, lsys.rules, n)
    lp = axiomtoline2d(gen, (x, y), lsys) 
    for l in lp:
        sx, sy = l.end1
        ex, ey = l.end2
        pygame.draw.aaline(screen, BLACK, (sx, HEIGHT - sy), (ex, HEIGHT - ey), n)


if __name__ == "__main__":
    pygame.init()
    done = False
    choice  = None
    lsys = None
    while choice not in [str(i) for i in range(1, 10)]:
        print("Choose one\n1) Koch curve\n2) Koch rectangle curve\n3) Sierpinski triangle\n4) Tree 1\n5) Tree 2\n6) Tree 3\n7) Tree 4\n8) Tree 5\n9) Tree 6\n")
        choice = input()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill(WHITE)
    match int(choice):
        case 1: 
            lsys = koch
        case 2:
            lsys = koch90
        case 3: 
            lsys = sierpinski
        case 4:
            lsys = tree0
        case 5: 
            lsys = tree1
        case 6:
            lsys = tree2
        case 7: 
            lsys = tree3
        case 8:
            lsys = tree4
        case 9: 
            lsys = tree5
    draw(lsys.x0, lsys.y0, 5, lsys)
    while not done:
        pygame.display.update()
        for event in pygame.event.get():
            # Close the window by pressing the x button.
            if event.type == pygame.QUIT:
                done = True
    pygame.time.wait(10)
