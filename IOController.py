from BulletList import *
from LogQueue import *

def writeFileRank(scoreResult):
    with open('gameRank.txt', 'a') as f:
        f.write(str(scoreResult)+'\n')

def readFileRank():
    with open('gameRank.txt', 'r') as f:
        resultList = []
        for line in f:
            resultList.append(int(line))
        return resultList

def writeFileLog():
    with open('gameLog.txt', 'w') as f:
        logQueue = getLogQueue()
        for i in range(0, logQueue.counter):
            f.write(logQueue.remove().data + '\n')

def readFileLog():
    with open('gameLog.txt', 'r') as f:
        for line in f:
            item = Item(line)
        return logQueue
