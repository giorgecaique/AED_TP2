import pygame, sys
import random
from GameLibrary import *
from Process import *
from BulletList import *
from IOController import *
from LogQueue import *

pygame.init()
pygame.font.init()
WIDHT, HEIGHT = 1366, 720
screen = pygame.display.set_mode((WIDHT, HEIGHT))
background = pygame.image.load("Resources/background.jpg")
clock = pygame.time.Clock()

fps = 30
fiveSecondInterval = fps * 5
tenSecondInterval = fps * 10
totalframes = 0
timer = 5
timeLimit = 5
score = 0

bulletList = BulletList()

millenniumFalcon = MillenniumFalcon(random.randint(100, 1100), random.randint(100, 650), 70, 70, "Resources/mf_Up.png")
millenniumFalconItem = Item(millenniumFalcon)
def CreateBullets():
    i = 0
    asteroid = Asteroid(random.randint(100,1100), random.randint(100, 650), 30, 30, "Resources/asteroid.png")
    item = Item(asteroid)
    Bullet.bulletList.Add(item)
    item = Item('created Asteroid')
    logInsert(item)
    while i < 5:
        fuel = SpaceFuel(random.randint(100,1100), random.randint(100, 650), 30, 30, "Resources/atomic.png")
        i += 1
        item = Item(fuel)
        Bullet.bulletList.Add(item)
        item = Item('created SpaceFuel')
        logInsert(item)

CreateBullets()

#------------ Main Program Loop ------------
while True:
    #PROCESSES
    process(millenniumFalcon)
    #PROCESSES

    #LOGIC
    timer =  Bullet.bulletList.CollisionDetection(millenniumFalconItem, timer)
    if timer > timeLimit:
        timer = timeLimit
    millenniumFalcon.Motion(WIDHT, HEIGHT, score )

    totalframes += 1

    if totalframes % 30 == 0:
        timer -= 1
        score += 1

    if timer <= 0:
        item = Item('game over - time zero')
        logInsert(item)
        Exit(score)

    timer_screen = timer
    if totalframes % fiveSecondInterval == 0:
        millenniumFalcon.IncreaseSpeed(5)
        CreateBullets()

    if totalframes % tenSecondInterval == 0:
        if(timeLimit > 1):
            timeLimit -= 1
    #LOGIC

    #DRAW
    screen.blit(background, (0, 0))
    BaseClass.allsprites.draw(screen)
    texts(screen, timer_screen)
    pygame.display.flip()
    #DRAW

    clock.tick(fps)
#------------ Main Program Loop ------------
