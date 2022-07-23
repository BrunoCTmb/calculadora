import pygame, sys
from pygame.locals import *
from layout import Layout

pygame.init()

width = 600
height = 600
screen = pygame.display.set_mode((width, height))
window_name = pygame.display.set_caption('Calculadora')
color = 'red'
while True:
    screen.fill((40,40,40))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if ret.collidepoint(mouse):
                color = 'green'
            else:
                color = 'red'

    mouse = pygame.mouse.get_pos()
    
    ret = pygame.draw.rect(screen, (color), (200,200,50,50))
    pygame.display.flip()
