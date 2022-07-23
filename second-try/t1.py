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
total = 0
num = 0
ocult = ''
sinal = '+'

class Text:
    def __init__(self):
        pass

    def text(self, txt,size,color):
        font = pygame.font.SysFont('arial', size, False, False)
        texto = f'{txt}'
        final_text = font.render(texto, True, color)
        return final_text

def soma():
    total += num
    return total



while True:
    screen.fill((40,40,40))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            input_active = True
            text = ''
            ocult = ''
            total = 0
        elif event.type == pygame.KEYDOWN and input_active:
            if event.key == pygame.K_RETURN:
                input_active = False
                if sinal == '+':
                    num = int(ocult)
                    total += num
                    ocult = ''
                elif sinal == '-':
                    num = int(ocult)
                    total -= num
                    ocult = ''                
                text += f' = {total}'
            elif event.key == pygame.K_BACKSPACE:
                text = text[:-1]
                ocult = ocult[:-1]
            else:
                if event.unicode.isnumeric() or event.unicode == '+' or event.unicode == '-' or event.unicode == '=': 
                    if text == '' and event.unicode == '+':  #nao pode comecar com sinal 
                        pass
                    elif len(text) > 0 and text[-1] == '+' and event.unicode == '+':  #digitar apenas um sinal 
                        pass
                    else:
                        if event.unicode == '+' or event.unicode == '-' or event.unicode == '=' and len(text) > 0:
                            sinal = event.unicode
                            if sinal == '+':
                                num = int(ocult)
                                total += num
                                ocult = ''
                            elif sinal == '-':
                                num = int(ocult)
                                total -= num
                                ocult = ''
                            print(total)
                            
                        elif event.unicode.isnumeric():
                            ocult += event.unicode
                        text += event.unicode


    texto = Text().text(text, 20, 'green')
    screen.blit(texto, (200,200))
        
    pygame.display.flip()
