import pygame, sys
from GameLibrary import *
from Process import *

pygame.init()
WIDHT, HEIGHT = 1366, 720
screen = pygame.display.set_mode((WIDHT, HEIGHT))
background = pygame.image.load("Resources/background.jpg")
clock = pygame.time.Clock()
fps = 30
fiveSecondInterval = fps * 5
totalframes = 0

millenniumFalcon = MillenniumFalcon(1000, 200, 10, 10, "Resources/mf_Up.png")
asteroid = Asteroid(400, 300, 30, 30, "Resources/asteroid.png")
fuel = SpaceFuel(600, 450, 30, 30, "Resources/fuel.png")
#------------ Main Program Loop ------------
while True:
    #PROCESSES
    process(millenniumFalcon)
    #PROCESSES

    #LOGIC
    millenniumFalcon.Motion(WIDHT, HEIGHT)
    totalframes += 1

    if totalframes % fiveSecondInterval == 0:
        millenniumFalcon.IncreaseSpeed(10)
    #LOGIC

    #DRAW
    screen.blit(background, (0, 0))
    BaseClass.allsprites.draw(screen)
    pygame.display.flip()
    #DRAW

    clock.tick(fps)
#------------ Main Program Loop ------------
