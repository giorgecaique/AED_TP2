import pygame, sys
from GameLibrary import *

def process(millenniumFalcon):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            millenniumFalcon.image = pygame.image.load("Resources/mf_Up.png")
            millenniumFalcon.ChangeDirection("up")
        elif keys[pygame.K_DOWN]:
            millenniumFalcon.image = pygame.image.load("Resources/mf_Down.png")
            millenniumFalcon.ChangeDirection("down")
        elif keys[pygame.K_LEFT]:
            millenniumFalcon.image = pygame.image.load("Resources/mf_Left.png")
            millenniumFalcon.ChangeDirection("left")
        elif keys[pygame.K_RIGHT]:
            millenniumFalcon.image = pygame.image.load("Resources/mf_Right.png")
            millenniumFalcon.ChangeDirection("right")

def Exit():
    pygame.quit()
    sys.exit()
