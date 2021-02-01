import pygame
import os
from subprocess import Popen

def fin():
    pygame.init()
    screen = pygame.display.set_mode((1000,600))
    pygame.display.set_caption('Finish Crawl website')
    white = (255,255,255)
    BLACK = (0,0,0)
    VV = (204,204,255)
    RED = (255, 0, 0)
    
    add = os.getcwd()+"\\thư mục chứa file"
    n = len(next(os.walk(add))[2])
    size = 0
    
    f = open("data.txt", "r")
    time = int(f.readlines()[0])
    f.closed
    
    for dirpath, dirnames, filenames in (os.walk(os.getcwd()+"\\thư mục chứa file")):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            size += os.path.getsize(fp)
    
    font = pygame.font.SysFont('sans', 80)
    font1 = pygame.font.Font('fonts.ttf', 20)
    
    gameDisplay = pygame.display.set_mode((1000,600))
    Img = pygame.image.load('vtv.png')
    carImg = pygame.transform.scale(Img, (320,200))
    text1 = font.render("FINISH!", True, BLACK)
    text2 = font1.render("Nơi chứa các file html:", True, BLACK)
    text3 = font1.render("Tổng số file:", True, BLACK)
    text4 = font1.render("Dung lượng tổng:", True, BLACK)
    text8 = font1.render("tần suất:", True, BLACK)
    text5 = font1.render(str(n), True, RED)
    text6 = font1.render(add, True, RED)
    text7 = font1.render(str(round((size*(1/1048576)),3))+" (MB)", True, RED)
    text9 = font1.render(str(round((size/1024)/time, 3))+" (kb/s)", True, RED)
    text10 = font1.render("đi đến thư mục", True, RED)
    
    pygame.event.get()
    while True:
        screen.fill(VV)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        
        pygame.draw.rect(screen, white, (150, 490, 270, 50))
        
        screen.blit(text1, (580,50))
        screen.blit(text2, (50,220))
        screen.blit(text3, (50,280))
        screen.blit(text4, (50,340))
        screen.blit(text5, (260,280))
        screen.blit(text6, (260,220))
        screen.blit(text7, (260,340))
        screen.blit(text9, (260,400))
        screen.blit(text8, (50,400))
        screen.blit(text10, (210,500))
        
        gameDisplay.blit(carImg, (130,4))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
               if event.button == 1 and mouse_x <420 and mouse_x >150 and mouse_y <540 and mouse_y > 490:
                   Popen('explorer '+str(add))
        pygame.display.flip()