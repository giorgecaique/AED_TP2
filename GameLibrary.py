import pygame, sys
from Library import *
from DataStructures import *
from Process import *

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
    List = pygame.sprite.Group()
    speed = 3
    direction = "up"
    def __init__(self, x, y, widht, height, image_string):
        BaseClass.__init__(self, x, y, widht, height, image_string)
        MillenniumFalcon.List.add(self)

    def WallControl(self, WIDHT, HEIGHT):
        if self.rect.x < 0:
            Exit()
        elif self.rect.x + self.widht > WIDHT - 220:
            Exit()
        if self.rect.y < 0:
            Exit()
        elif self.rect.y + self.height > HEIGHT - 190:
            Exit()

    def Motion(self, WIDHT, HEIGHT):
        self.WallControl(WIDHT, HEIGHT)

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
    def __init__(self, x, y, widht, height, image_string):
        BaseClass. __init__(self, x, y, widht, height, image_string)

class SpaceFuel(Bullet):
    def __init__(self, x, y, widht, height, image_string):
        Bullet.__init__(self, x, y, widht, height, image_string)

class Asteroid(Bullet):
    def __init__(self, x, y, widht, height, image_string):
        Bullet.__init__(self, x, y, widht, height, image_string)
