import pygame
from sys import exit
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((1468,911),0,32)

pygame.display.set_caption("Hello")
background=pygame.image.load("image01.png").convert()
plane = pygame.image.load("image03.png").convert()
bullet = pygame.image.load("image04.png").convert_alpha()

font = pygame.font.SysFont("arial",40)
font_height = font.get_linesize()
event_text=[]

bullet_x,bullet_y = 0,0
move_x,move_y =0,0

text_surface = font.render("This is a test",True,(0,0,255))
text_x = 0
text_y = (911 - text_surface.get_height())/2
while True:
    screen.blit(background,(0,0))
    x,y = pygame.mouse.get_pos()
    x -= plane.get_width()/2
    y -= plane.get_height()/2
    screen.blit(plane,(x,y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            background = pygame.image.load('image02.jpg').convert()
        if event.type == pygame.KEYDOWN and(event.key == pygame.K_LEFT or event.unicode =='a'):
            move_x = -1
        if event.type == pygame.KEYDOWN and(event.key == pygame.K_RIGHT or event.unicode =='d'):
            move_x = 1
        if event.type == pygame.KEYDOWN and(event.key == pygame.K_UP or event.unicode =='w'):
            move_y = -1
        if event.type == pygame.KEYDOWN and(event.key == pygame.K_DOWN or event.unicode =='s'):
            move_y = 1
        if event.type == pygame.KEYUP :
            move_x = 0
            move_y = 0
    bullet_x += move_x
    bullet_y += move_y
    screen.blit(bullet,(bullet_x,bullet_y))
    text_x -= 1
    if text_x < -text_surface.get_width():
        text_x = 1468 - text_surface.get_width()
    screen.blit(text_surface,(text_x,text_y))

    pygame.display.update()
