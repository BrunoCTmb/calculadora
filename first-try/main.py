import pygame, sys
from pygame.locals import *
from layout import Layout
from backend import Back

pygame.init()

width = 600
height = 600

screen = pygame.display.set_mode((width, height))
window_name = pygame.display.set_caption('Calculadora')

layout = Layout()
backend = Back()

backend.operacoes()

while True:
    screen.fill((40,40,40))
    layout.run(screen)
    
    backend.running()   #caso ocorra um "quit, exit"

    text = layout.text(backend.running(), 50, (150,150,150))
    screen.blit(text, (60,99))

    pygame.display.flip()
