import pygame, sys
from Library import *
from BulletList import *
from Process import *
from IOController import *
from LogQueue import *

class BaseClass(pygame.sprite.Sprite):
    allsprites = pygame.sprite.Group()
    def __init__(self, x, y, widht, height, image_string):
        pygame.sprite.Sprite.__init__(self)
        BaseClass.allsprites.add(self)
        self.image = pygame.image.load(image_string)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.widht = widht
        self.height = height

class MillenniumFalcon(BaseClass):
    speed = 5
    direction = "up"
    def __init__(self, x, y, widht, height, image_string):
        BaseClass.__init__(self, x, y, widht, height, image_string)

    def WallControl(self, WIDHT, HEIGHT, score):
        if self.rect.x < 0:
            item = Item('game over - wall contact')
            logInsert(item)
            Exit(score)
        elif self.rect.x > WIDHT - self.widht:
            item = Item('game over - wall contact')
            logInsert(item)
            Exit(score)
        if self.rect.y < 0:
            item = Item('game over - wall contact')
            logInsert(item)
            Exit(score)
        elif self.rect.y > HEIGHT - self.height:
            item = Item('game over - wall contact')
            logInsert(item)
            Exit(score)

    def Motion(self, WIDHT, HEIGHT, score):
        self.WallControl(WIDHT, HEIGHT, score)

        if self.direction == "up":
            self.rect.y -= self.speed
        elif self.direction == "down":
            self.rect.y += self.speed
        elif self.direction == "left":
            self.rect.x -= self.speed
        elif self.direction == "right":
            self.rect.x += self.speed

    def IncreaseSpeed(self, speed):
        self.speed += speed

    def ChangeDirection(self, direction):
        self.direction = direction

class Bullet(BaseClass):
    bulletList = BulletList()
    def __init__(self, x, y, widht, height, image_string):
        BaseClass. __init__(self, x, y, widht, height, image_string)
        item = Item(self)
        Bullet.bulletList.Add(item)

    def kill(self):
        BaseClass.allsprites.remove(self)
        self.rect.x = -1
        self.rect.y = -1
        item = Item('eated '+ str(self.__class__.__name__))
        logInsert(item)

class SpaceFuel(Bullet):
    def __init__(self, x, y, widht, height, image_string):
        Bullet.__init__(self, x, y, widht, height, image_string)

    def Create(self):
        fuel = SpaceFuel(randint(0,1366), randint(0, 768), 30, 30, "Resources/fuel.png")

class Asteroid(Bullet):
    def __init__(self, x, y, widht, height, image_string):
        Bullet.__init__(self, x, y, widht, height, image_string)

def texts(screen, timer):
    pygame.font.init()
    font = pygame.font.SysFont("04b",30)
    scoretext = font.render("Timer: "+str(timer), 1,(255,255,255))
    screen.blit(scoretext, (1100, 50))
