import pygame as pg
import sys
from pygame.locals import *

class Back:
    def __init__(self):
        self.terminal_text = ''   #texto inicial do terminal da calculadora
        self.input_mode = True    #situacao do input: ativo ou desativado
        self.mx = 0
        self.my = 0
        self.total = 0      #valor total da operacao que inicia com 0
        self.valor_atual = []
        self.sinal = ''

    def running(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                self.input_mode = True
                self.terminal_text = ''

                self.mx, self.my = pg.mouse.get_pos()
                print(f'[{self.mx}, {self.my}]')

            elif event.type == pg.KEYDOWN and self.input_mode == True:
                if event.key == pg.K_BACKSPACE:
                    terminal_text = terminal_text[:-1]
                if event.key == pg.K_RETURN:
                    self.input_mode = False
                else:
                    if event.unicode.isnumeric():  #se o que foi digitado for numerico 
                        self.terminal_text += event.unicode

                    elif event.unicode == '+' or event.unicode == '-' or event.unicode == '*' or event.unicode == '/':   # se o que foi digitado for algum sinal das 4 operacoes
                        self.sinal = ''
                        self.sinal = event.unicode 

                        self.valor_atual.clear()       #sempre que o loop voltar ao inicio a lista limpa para trocar posicoes
                        self.text2 = int(self.terminal_text)   #converter string para inteiro

                        self.valor_atual.append(self.total)   #adiciona o valor digitado na primeira posicao
                        self.valor_atual.append(self.text2)   #adiciona o valor digitado na segunda posicao
                        #self.total += self.valor_atual[1]     #fazer soma
                        

                        print(self.operacoes()) 
                        self.terminal_text = ''      #resetar o texto mostrado no terminal da calculadora
                        
                    print(self.valor_atual)
                    
        return self.terminal_text

    def return_pos(self):
        return self.mx, self.my

    def operacoes(self):
        if self.sinal == '+':
            return self.total += self.valor_atual[1]
        elif self.sinal == '-':
            return self.total - self.valor_atual[1]
        elif self.sinal == '*':
            return self.total * self.valor_atual[1]
        elif self.sinal == '/':
            return self.total / self.valor_atual[1]

    def run(self):
        pass