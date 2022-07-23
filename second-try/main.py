from turtle import back, backward
import pygame
from backend import Backend
from layout import Layout

pygame.init()

width = 640
height = 480
screen = pygame.display.set_mode((width, height))
nome_programa = pygame.display.set_caption('Calculator')

backend = Backend()
layout = Layout()

while True:
    screen.fill('white')
    backend.running()

    text = layout.text(backend.text, 20, 'red')
    screen.blit(text, (200,200))

    pygame.display.flip()