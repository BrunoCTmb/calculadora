import pygame, sys
from pygame.locals import *
from layout import Layout
from backend import Back

pygame.init()

width = 600
height = 600

screen = pygame.display.set_mode((width, height))
window_name = pygame.display.set_caption('Calculadora')

screen.fill((40,40,40))

layout = Layout()
backend = Back()

while True:
    layout.run(screen)
    
    backend.running()   #caso ocorra um "quit, exit"

    text = layout.text(backend.running(), 20, 'red')
    screen.blit(text, (20,20))

    pygame.display.flip()