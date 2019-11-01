import sys
import pygame
import time

def draw(img, x,y):
    gameDisplay.blit(img, (x,y))

pygame.init()

display_w = 800
display_h = 700

gameDisplay = pygame.display.set_mode((display_w,display_h))
pygame.display.set_caption('Gbat & Jane')

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()
love  = False

W = 100
H = 100
valX = 100
valY = 100
valDirX = 1
valDirY = 1
valImg = pygame.image.load('val.png')
valImg = pygame.transform.scale(valImg, (W, H))

hellenX = 350
hellenY = 450
hellenDirX = 1
hellenDirY = 1
hellenImg = pygame.image.load('hellen.jpg')
hellenImg = pygame.transform.scale(hellenImg, (W, H))
w = 760
h = 730
osDoisImg = pygame.image.load('OsDois.jpg')
osDoisImg = pygame.transform.scale(osDoisImg, (w, h))
vel = 10

while not love:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    gameDisplay.fill(white)
    draw(valImg, valX, valY)
    draw(hellenImg, hellenX, hellenY)
    pygame.display.update()

    dt = clock.tick(50)

    valX += valDirX * vel
    valY += valDirY * vel

    if valX <= 0 or valX >= (display_w - W):
        valDirX *= -1
    if valY <= 0 or valY >= (display_h - H):
        valDirY *= -1

    hellenX += hellenDirX * vel
    hellenY += hellenDirY * vel

    if hellenX <= 0 or hellenX >= (display_w - W):
        hellenDirX *= -1
    if hellenY <= 0 or hellenY >= (display_h - H):
        hellenDirY *= -1

    rectHellen = pygame.Rect(hellenX, hellenY, W, H)
    rectVal = pygame.Rect(valX, valY, W, H)

    if rectHellen.colliderect(rectVal):
        love = True

draw(osDoisImg, 0, 0)
pygame.display.update()
time.sleep(5)
pygame.quit()

