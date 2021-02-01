import pygame
from time import sleep
from random import randint
import finish


pygame.init()
screen = pygame.display.set_mode((1000,600))
pygame.display.set_caption('Crawling... website')
white = (255,255,255)
BLACK = (0,0,0)
VV = (204,204,255)
GR = (64,224,208)

f = open("data.txt", "r")
input = int(f.readlines()[0])
f.closed

b= input +1
a, c, d = 0, b, 0
font = pygame.font.SysFont('sans', 50)

te = ""
te1 = "crawling"
te2 = "crawling."
te3 = "crawling.."
te4 = "crawling..."

gameDisplay = pygame.display.set_mode((1000,600))
Img = pygame.image.load('vtv.png')
carImg = pygame.transform.scale(Img, (320,200))

pygame.event.get()

while True:
    screen.fill(VV)
    text1 = font.render(te, True, BLACK)
    text2 = font.render(str(c)+"(s)", True, BLACK)
    i = randint(1, 4)
    pygame.draw.rect(screen, white, (240,410,550,40))
    pygame.draw.rect(screen, GR, (245,415,(540/(b))*d,30))
    screen.blit(text1, (350,220))
    screen.blit(text2, (550,220))
    gameDisplay.blit(carImg, (320,4))
    mouse_x, mouse_y = pygame.mouse.get_pos()
    
    if a%10 == 0:
        c = c-1
        d = d+1
    if a == b*10:
        finish.fin()
        pygame.quit()
    if i == 1:
        te = te1
    if i == 2:
        te = te2
    if i == 3:
        te = te3
    if i == 4:
        te = te4
    for event in pygame.event.get():
        pass
            
    sleep(0.0963)
    a = a+1
    
    pygame.display.flip()