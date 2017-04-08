import sys
from Library import *

class LogQueue:
    def __init__(self, first = None, last = None, counter = 0):
        self.first = Item()
        self.last = self.first
        self.counter = counter

    def add(self, item):
        if item != None:
            self.last.pointer = item
            self.last = item
            self.counter += 1

    def remove(self):
        if self.first.pointer != None:
            temp = self.first.pointer
            self.counter -= 1
            if temp != self.last:
                self.first.pointer = temp.pointer
                return temp
            else:
                self.first.pointer = None
                self.last = self.first
                return temp
        return None

    def printer(self):
        temp = self.first
        for i in range(0, self.counter):
            print self.remove().data

# LogQueue Controller
logQueue = LogQueue()

def logInsert(item):
    logQueue.add(item)

def logRemove():
    return logQueue.remove()

def getLogQueue():
    return logQueue

def logQueuePrinter():
    logQueue.printer()
