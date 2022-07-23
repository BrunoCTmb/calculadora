#divisão de botoes:
'''
o tamanho do fundo dos botoes tera uma reduçao de -50, pois serao 5 espacos com o tamanho de '10' que serao para dar espaços entre os botoes e a borda do fundo. 
'''


import pygame
from backend import Back

backend = Back()

class Layout:
    def __init__(self):
        self.color1 = 0
        self.color2 = 1

    def terminal(self,surf):     
        borda = pygame.draw.rect(surf, (120,120,120), (50,50, 500,100))
        terminal = pygame.draw.rect(surf, (70,70,70), (55,55,490,90))


    def buttons(self,surf):
        background = pygame.draw.rect(surf, (120,120,120), (50,200, 350,350))
        
        pos_x = 50+10   #posicao x inicial do primeiro botao
        pos_y = 200+10  #posicao y inicial do primeiro botao
        pos = 0    #variavel para diferenciar cada botao com um numero
        lista_buttons = ['nada' for c in range(9)]  #lista que armazena os botoes criados
        lista_colors = ['white' for c in range(9)]

        for linha in range(3):
            for coluna in range(3):
                button = pygame.draw.rect(surf, (lista_colors[pos]), (pos_x,pos_y,103,103))
                pos_x += 113   
                lista_buttons[pos] = button
                pos += 1

            pos_x = 50+10
            pos_y += 113

        return lista_colors

    def text(self, txt,size,color):
        font = pygame.font.SysFont('arial', size, False, False)
        texto = f'{txt}'
        final_text = font.render(texto, True, color)
        return final_text

    def run(self,surf):
        self.terminal(surf)
        self.buttons(surf)