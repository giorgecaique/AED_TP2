import pygame, sys
from Library import *

class BulletList:
    def __init__(self, first = None, last = None):
        self.first = Item()
        self.last = self.first

    def Add(self, newItem):
        self.last.pointer = newItem
        self.last = newItem

    def Find(self, value):
        temp = self.first
        while temp != None:
            if(temp.data == value.data):
                return value
            temp = value.pointer
        return temp

    def CollisionDetection(self, item, timer):
        temp = self.first
        while temp.pointer != None:
            temp2 = temp.pointer
            if item.data.rect.colliderect(temp2.data.rect):
                if str(temp2.data.__class__.__name__) == "Asteroid":
                    timer -= 2
                elif str(temp2.data.__class__.__name__) == "SpaceFuel":
                    timer += 2
                item.data.IncreaseSpeed(1)
                temp2.data.kill()
                self.Remove(temp2)
            temp = temp.pointer
        return timer

    def Remove(self, item):
        temp = self.first
        while(temp.pointer != None):
            if temp.pointer == item:
                temp2 = temp.pointer
                temp.pointer = temp2.pointer
                temp2.pointer = None
                return temp2
            temp = temp.pointer
        return temp

class LogQueue:
    def __init__(self, first = None, last = None):
        self.first = Item()
        self.last = first

    def add(self, item):
        if item != None:
            self.last.pointer = item
            self.last = item

    def remove(self):
        if self.first.pointer != None:
            temp = self.first.pointer
            self.first.pointer = temp.pointer
            return pointer
        return None

    def printer(self):
        temp = self.first
        while temp.pointer != None:
            print temp.pointer.data
