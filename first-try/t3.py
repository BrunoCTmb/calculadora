import pygame, sys
from pygame.locals import *
from layout import Layout

pygame.init()

width = 600
height = 600
screen = pygame.display.set_mode((width, height))
window_name = pygame.display.set_caption('Calculadora')

text = ''
input_active = True

class Text:
    def __init__(self):
        pass

    def text(self, txt,size,color):
        font = pygame.font.SysFont('arial', size, False, False)
        texto = f'{txt}'
        final_text = font.render(texto, True, color)
        return final_text

    
    def isthing(self, valor):
        if valor == '+' or valor == '-' or valor == '*' or valor == '/':
            return True
        else:
            return False

while True:
    screen.fill((40,40,40))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            input_active = True
            text = ''
        elif event.type == pygame.KEYDOWN and input_active:
            if event.key == pygame.K_RETURN:
                input_active = False              
            elif event.key == pygame.K_BACKSPACE:
                text = text[:-1]
            else:
                if Text().isthing(event.unicode) or event.unicode.isnumeric():
                    text += event.unicode
                

    texto = Text().text(text, 20, 'green')
    screen.blit(texto, (200,200))
        
    pygame.display.flip()
