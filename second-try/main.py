import pygame
from backend import Backend
from layout import Layout
from t1 import Click

pygame.init()

width = 600
height = 600
screen = pygame.display.set_mode((width, height))
nome_programa = pygame.display.set_caption('Calculator')

backend = Backend()
layout = Layout()
click = Click()

while True:
    screen.fill((70,70,70))
    backend.running()

    layout.run(screen)

    text = layout.text(backend.text, 60, 'black')
    screen.blit(text, (65,86))

    pygame.display.flip()