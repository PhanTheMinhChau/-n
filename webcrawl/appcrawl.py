import pygame
import os
import go

pygame.init()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption('Crawl website')
white = (255,255,255)
BLACK = (0,0,0)
VV = (204,204,255)

a = 30
font = pygame.font.Font('fonts.ttf', 50)
font1 = pygame.font.SysFont('sans', 25)

text5 = font.render("CRAWL", True, BLACK)
gameDisplay = pygame.display.set_mode((1000, 600))
os.chdir(os.getcwd())
Img = pygame.image.load('vtv.png')
carImg = pygame.transform.scale(Img, (320,200))
url1 = "https://vtvgo.vn"
url2 = "https://vietnamnet.vn"
url3 = "https://baomoi.com"
b = 1

while True:
    screen.fill(VV)
    gameDisplay.blit(carImg, (60, 4))
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if a <= 2:
        a = 2
    if b == 4:
        b = 1
    if b == 1:
        url = url1
    if b == 2:
        url = url2
    if b == 3:
        url = url3
    text1 = font1.render(url, True, BLACK)
    text2 = font.render("Đồ án crawler website", True, BLACK)
    text3 = font1.render("thoi gian crawl:", True, BLACK)
    text4 = font1.render(str(a)+"(s)", True, BLACK)
    text6 = font1.render("+", True, BLACK)
    text7 = font1.render("-", True, BLACK)
    text8 = font1.render("^", True, BLACK)
    
    pygame.draw.rect(screen, VV, (500, 0 , 500, 600))
    pygame.draw.rect(screen, white, (300, 240, 30, 30))
    pygame.draw.rect(screen, white, (350, 240, 30, 30))
    pygame.draw.rect(screen, white, (170, 230, 80, 50))
    pygame.draw.rect(screen, white, (100, 390, 300, 90))
    pygame.draw.rect(screen, white, (855, 95, 30, 30))
    
    screen.blit(text1, (500, 100))
    screen.blit(text2, (500, 20))
    screen.blit(text3, (30, 230))
    screen.blit(text4, (180, 240))
    screen.blit(text5, (180, 400))
    screen.blit(text6, (310, 240))
    screen.blit(text7, (360, 240))  
    screen.blit(text8, (865, 100))
    
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_UP:
               a = a+2
           if event.key == pygame.K_DOWN:
               a = a-2
           if event.key == pygame.K_RETURN:
               f = open("data.txt", "w")
               f.writelines(str(a))
               f.close()
               f = open("data.txt", "a")
               f.writelines("\n" + url)
               f.close()
               go.gocr()
               pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
           if event.button == 1 and mouse_x <400 and mouse_x >100 and mouse_y <480 and mouse_y > 390:
               f = open("data.txt", "w")
               f.writelines(str(a))
               f.close()
               f = open("data.txt", "a")
               f.writelines("\n" + url)
               f.close()
               go.gocr()
               pygame.quit()
           if event.button == 1 and mouse_x < 330 and mouse_x > 300 and mouse_y < 270 and mouse_y > 240:
                a = a+2
           if event.button == 1 and mouse_x <380 and mouse_x >350 and mouse_y <270 and mouse_y > 240:
                a = a-2
           if event.button == 1 and mouse_x <885 and mouse_x >855 and mouse_y <125 and mouse_y > 95:
               b = b+1
            
    pygame.display.flip()