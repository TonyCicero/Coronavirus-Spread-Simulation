import sim
import sys, pygame
pygame.init()
WINDOW_SIZE = [1024, 720]
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Corona Virus Simulation")
done = False
clock = pygame.time.Clock()

BLACK = (0,0,0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

GRIDSIZE = 10

WIDTH = 10;
HEIGHT = 10;
MARGIN = 10;
RADIUS = 5;

GRIDSPLIT = 250

grid_A=[]

TownA = []
TownB = []


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(BLACK)

    for row in range(10):
        for column in range(10):
            color = WHITE
            pygame.draw.rect(screen, color, [(MARGIN+WIDTH)*column+MARGIN,
                                             (MARGIN+HEIGHT)*row+MARGIN,
                                             WIDTH,
                                             HEIGHT])
            pygame.draw.circle(screen, color, [(MARGIN+WIDTH)*column+MARGIN,
                                             ((MARGIN+HEIGHT)*row+MARGIN) + GRIDSPLIT],RADIUS)
            clock.tick(60)
            pygame.display.flip()

pygame.quit()
                                             
