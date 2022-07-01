import pygame, sys
from pygame.locals import *
from layout import Layout

pygame.init()

width = 600
height = 600

screen = pygame.display.set_mode((width, height))
window_name = pygame.display.set_caption('Calculadora')

screen.fill((40,40,40))

layout = Layout()




while True:
    layout.run(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            if mx > 300:
                layout.buttons(screen)[5] = 'green'
                print(layout.buttons(screen)[5])

            #print(mx, my)
            #print(layout.buttons(screen)[1])

    pygame.display.flip()