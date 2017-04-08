import pygame, sys
from IOController import *
from matplotlib import pyplot as plt

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

def Exit(score):
    writeFileRank(score)
    logQueuePrinter()
    Statistic()
    EndGameScreen(score)

def EndGameScreen(score):
    pygame.init()
    WIDHT, HEIGHT = 500, 500
    screen = pygame.display.set_mode((WIDHT, HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.font.init()
        font = pygame.font.SysFont("04b",30)
        scoretext = font.render("Score:"+str(score), 1,(255,255,255))
        screen.blit(scoretext, (WIDHT / 2, HEIGHT / 2))
        pygame.display.flip()

def Statistic():
    resultList= readFileRank()
    scores = []
    t = 0
    for i in resultList:
        scores.append(t)
        t += 1
    plt.plot(scores, resultList, color='green', marker='o', linestyle='solid')
    plt.title("Score Rank")
    plt.ylabel("Score")
    plt.show()
