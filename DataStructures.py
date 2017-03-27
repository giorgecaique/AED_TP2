import pygame, sys
from Library import *

class BulletList:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def Add(newItem):
        self.Last.pointer = newItem
        self.Last = newItem

    def Find(value):
        temp = self.first
        while temp != None:
            if(temp.data == value.data):
                return value
            temp = value.pointer
        return temp

    def Remove(value):
        temp = self.first
        while(temp.pointer != None):
            if temp.pointer.data == value:
                temp2 = temp.pointer
                temp.pointer = temp2.pointer
                temp2.pointer = None
                return temp2
            temp = temp.pointer
        return temp
